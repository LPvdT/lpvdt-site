#!/usr/bin/env python3
"""
LaTeX CV Parser Script
Parses final-cv.tex and generates a JSON structure for the CV website
"""

import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List


def parse_personal_info(content: str) -> Dict[str, str]:
    """Extract personal information from LaTeX content."""
    personal_info = {}

    # Extract name
    name_match = re.search(r"\\name\{([^}]+)\}\{([^}]+)\}", content)
    if name_match:
        personal_info["name"] = f"{name_match.group(1)} {name_match.group(2)}"

    # Extract title
    title_match = re.search(r"\\title\{([^}]+)\}", content)
    if title_match:
        personal_info["title"] = title_match.group(1)

    # Extract address
    address_match = re.search(r"\\address\{([^}]+)\}", content)
    if address_match:
        personal_info["location"] = address_match.group(1)

    # Extract email
    email_match = re.search(r"\\email\{([^}]+)\}", content)
    if email_match:
        personal_info["email"] = email_match.group(1)

    # Extract homepage
    homepage_match = re.search(r"\\homepage\{([^}]+)\}", content)
    if homepage_match:
        personal_info["website"] = f"https://{homepage_match.group(1)}"

    # Extract LinkedIn
    linkedin_match = re.search(r"\\social\[linkedin\]\{([^}]+)\}", content)
    if linkedin_match:
        personal_info["linkedin"] = (
            f"https://linkedin.com/in/{linkedin_match.group(1)}"
        )

    # Extract GitHub
    github_match = re.search(r"\\social\[github\]\{([^}]+)\}", content)
    if github_match:
        personal_info["github"] = f"https://github.com/{github_match.group(1)}"

    return personal_info


def parse_profile(content: str) -> str:
    """Extract the profile section."""
    profile_match = re.search(
        r"\\section\{Profile\}(.*?)\\section\{", content, re.DOTALL
    )
    if profile_match:
        profile_text = profile_match.group(1).strip()
        # Clean up LaTeX formatting
        profile_text = re.sub(r"\\vspace\{[^}]+\}", "", profile_text)
        profile_text = re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", profile_text)
        profile_text = re.sub(r"\s+", " ", profile_text).strip()
        return profile_text
    return ""


def parse_experience(content: str) -> List[Dict[str, Any]]:
    """Extract work experience entries."""
    experiences = []

    # Find all cventry entries in the Experience section
    exp_section = re.search(
        r"\\section\{Experience\}(.*?)\\section\{", content, re.DOTALL
    )
    if not exp_section:
        return experiences

    exp_content = exp_section.group(1)

    # Pattern for cventry
    cventry_pattern = r"\\cventry\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{[^}]*\}\{(.*?)(?=\\cventry|\Z)"

    for match in re.finditer(cventry_pattern, exp_content, re.DOTALL):
        period = match.group(1)
        title = match.group(2)
        company = match.group(3)
        location = match.group(4)
        description_block = match.group(5)

        # Extract description and bullet points
        description_parts = []

        # Get the main description (before itemize)
        main_desc = re.search(
            r"\\vspace\{[^}]+\}(.*?)(?=\\vspace\{[^}]+\}\\begin\{itemize\}|\Z)",
            description_block,
            re.DOTALL,
        )
        if main_desc:
            desc_text = main_desc.group(1).strip()
            desc_text = re.sub(r"\\\\", " ", desc_text)
            desc_text = re.sub(r"\s+", " ", desc_text).strip()
            if desc_text:
                description_parts.append(desc_text)

        # Extract bullet points
        itemize_match = re.search(
            r"\\begin\{itemize\}(.*?)\\end\{itemize\}",
            description_block,
            re.DOTALL,
        )
        if itemize_match:
            items_content = itemize_match.group(1)
            items = re.findall(r"\\item\s+([^\\]+)", items_content)
            for item in items:
                item_text = re.sub(r"\s+", " ", item.strip())
                if item_text:
                    description_parts.append(f"• {item_text}")

        # Combine all description parts
        full_description = " ".join(description_parts)

        # Extract technologies from description
        technologies = []
        # Look for technology keywords in the description
        tech_keywords = [
            "Python",
            "R",
            "Rust",
            "Scala",
            "Go",
            "TypeScript",
            "JavaScript",
            "React",
            "Next.js",
            "NestJS",
            "Svelte",
            "FastAPI",
            "TensorFlow",
            "PyTorch",
            "Databricks",
            "MLflow",
            "dbt",
            "Kafka",
            "Flink",
            "PySpark",
            "Airflow",
            "Kubernetes",
            "Docker",
            "Terraform",
            "Azure",
            "AWS",
            "GCP",
            "Machine Learning",
            "MLOps",
            "CI/CD",
            "SQL",
            "NoSQL",
            "ETL",
            "ELT",
        ]

        for tech in tech_keywords:
            if tech.lower() in full_description.lower():
                technologies.append(tech)

        experiences.append({
            "title": title,
            "company": company,
            "location": location,
            "period": period,
            "description": full_description,
            "technologies": list(set(technologies)),  # Remove duplicates
        })

    return experiences


def parse_skills(content: str) -> Dict[str, List[Dict[str, str]]]:
    """Extract skills from the LaTeX content."""
    skills = {
        "programming": [],
        "data_engineering": [],
        "cloud_devops": [],
        "analytics": [],
        "visualization": [],
        "other": [],
    }

    # Find skills section
    skills_section = re.search(
        r"\\section\{Skills\}(.*?)\\section\{", content, re.DOTALL
    )
    if not skills_section:
        return skills

    skills_content = skills_section.group(1)

    # Extract different skill categories
    skill_entries = re.findall(
        r"\\cventry\{\}\{\\textbf\{([^}]+)\}\}.*?\{([^}]+)\}\{(.*?)\}",
        skills_content,
        re.DOTALL,
    )

    for category, _, items_text in skill_entries:
        # Extract items from the itemize block
        itemize_match = re.search(
            r"\\begin\{itemize\}(.*?)\\end\{itemize\}", items_text, re.DOTALL
        )
        if itemize_match:
            items_content = itemize_match.group(1)
            items = re.findall(r"\\item\s+([^\\]+)", items_content)

            # Parse individual skills from the text
            for item in items:
                # Split by commas and clean up
                skill_list = [s.strip() for s in item.split(",")]

                category_lower = category.lower()
                target_category = "other"

                if "programming" in category_lower:
                    target_category = "programming"
                elif (
                    "data engineering" in category_lower
                    or "mlops" in category_lower
                ):
                    target_category = "data_engineering"
                elif "ci/cd" in category_lower or "iac" in category_lower:
                    target_category = "cloud_devops"
                elif "analytics" in category_lower:
                    target_category = "analytics"
                elif "visualization" in category_lower:
                    target_category = "visualization"

                for skill in skill_list:
                    # Clean up skill name
                    skill = re.sub(r"\\textbf\{([^}]+)\}", r"\1", skill)
                    skill = re.sub(r"\\textit\{[^}]*\}", "", skill)
                    skill = re.sub(r"\*", "", skill)
                    skill = skill.strip()

                    if skill and skill not in [
                        s["name"] for s in skills[target_category]
                    ]:
                        # Determine skill level based on formatting
                        level = "advanced"
                        if "\\textbf{" in item and skill in item:
                            level = "expert"
                        elif skill in [
                            "Python",
                            "Machine Learning",
                            "Databricks",
                            "MLflow",
                            "Kubernetes",
                            "Docker",
                            "Terraform",
                        ]:
                            level = "expert"

                        skills[target_category].append({
                            "name": skill,
                            "level": level,
                        })

    return skills


def parse_education(content: str) -> List[Dict[str, str]]:
    """Extract education entries."""
    education = []

    # Find education section
    edu_section = re.search(
        r"\\section\{Education\}(.*?)\\section\{", content, re.DOTALL
    )
    if not edu_section:
        return education

    edu_content = edu_section.group(1)

    # Pattern for education cventry
    cventry_pattern = r"\\cventry\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{[^}]*\}\{(.*?)(?=\\cventry|\Z)"

    for match in re.finditer(cventry_pattern, edu_content, re.DOTALL):
        period = match.group(1)
        degree = match.group(2)
        institution = match.group(3)
        location = match.group(4)
        description_block = match.group(5)

        # Extract description
        description_parts = []
        itemize_match = re.search(
            r"\\begin\{itemize\}(.*?)\\end\{itemize\}",
            description_block,
            re.DOTALL,
        )
        if itemize_match:
            items_content = itemize_match.group(1)
            items = re.findall(r"\\item\s+([^\\]+)", items_content)
            for item in items:
                item_text = re.sub(r"\\textbf\{([^}]+)\}", r"\1", item)
                item_text = re.sub(r"\\textit\{([^}]+)\}", r"\1", item_text)
                item_text = re.sub(r"\s+", " ", item_text.strip())
                if item_text:
                    description_parts.append(item_text)

        education.append({
            "degree": degree,
            "institution": institution,
            "location": location,
            "period": period,
            "description": " ".join(description_parts),
        })

    return education


def parse_certifications(content: str) -> List[Dict[str, str]]:
    """Extract certifications."""
    certifications = []

    # Find certifications section
    cert_section = re.search(
        r"\\section\{Certifications\}(.*?)$", content, re.DOTALL
    )
    if not cert_section:
        return certifications

    cert_content = cert_section.group(1)

    # Pattern for certification cventry
    cventry_pattern = r"\\cventry\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{[^}]*\}\{[^}]*\}\{([^}]*)\}"

    for match in re.finditer(cventry_pattern, cert_content):
        year = match.group(1)
        name = match.group(2)
        issuer = match.group(3)
        description = match.group(4) if match.group(4) else ""

        # Clean up description
        description = re.sub(r"\\textit\{([^}]+)\}", r"\1", description)

        certifications.append({
            "name": name,
            "issuer": issuer,
            "year": year,
            "description": description,
        })

    return certifications


def main():
    """Main function to parse the LaTeX CV and generate JSON."""
    try:
        # Read the LaTeX file
        latex_file = Path("final-cv.tex")
        if not latex_file.exists():
            print(f"Error: {latex_file} not found!")
            sys.exit(1)

        with open(latex_file, "r", encoding="utf-8") as f:
            content = f.read()

        print("Parsing LaTeX CV...")

        # Parse different sections
        cv_data = {
            "personal_info": parse_personal_info(content),
            "profile": parse_profile(content),
            "experience": parse_experience(content),
            "skills": parse_skills(content),
            "education": parse_education(content),
            "certifications": parse_certifications(content),
            "projects": [
                {
                    "name": "MLOps Platform",
                    "description": "Built comprehensive MLOps platform with automated model deployment, monitoring, and lifecycle management using Databricks, MLflow, and Kubernetes.",
                    "technologies": [
                        "Python",
                        "Databricks",
                        "MLflow",
                        "Kubernetes",
                        "Docker",
                    ],
                    "link": "https://github.com/LPvdT",
                },
                {
                    "name": "Real-time Data Platform",
                    "description": "Designed and implemented real-time streaming data platform handling millions of events daily using Kafka, Flink, and modern data lakehouse architecture.",
                    "technologies": [
                        "Kafka",
                        "Flink",
                        "Python",
                        "Terraform",
                        "Azure",
                    ],
                    "link": "https://github.com/LPvdT",
                },
            ],
        }

        # Generate JSON file
        output_file = Path("cv-data.json")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(cv_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Successfully parsed CV data to {output_file}")
        print(f"📊 Extracted:")
        print(f"   • Personal info: {len(cv_data['personal_info'])} fields")
        print(f"   • Experience: {len(cv_data['experience'])} positions")
        print(
            f"   • Skills: {sum(len(skills) for skills in cv_data['skills'].values())} skills"
        )
        print(f"   • Education: {len(cv_data['education'])} degrees")
        print(
            f"   • Certifications: {len(cv_data['certifications'])} certifications"
        )

        return cv_data

    except Exception as e:
        print(f"❌ Error parsing CV: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
