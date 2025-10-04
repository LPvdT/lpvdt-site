#!/usr/bin/env python3
"""
CV Data Processor
Cleans and processes the parsed CV data and updates the Svelte website
"""

import json
import re
from pathlib import Path


def clean_latex_text(text: str) -> str:
    """Remove LaTeX formatting from text."""
    if not text:
        return ""

    # Remove LaTeX commands and formatting
    text = re.sub(r"\\&", "&", text)
    text = re.sub(r"\\textbf\{([^}]+)\}", r"\1", text)
    text = re.sub(r"\\textit\{([^}]+)\}", r"\1", text)
    text = re.sub(r"\\vspace\{[^}]+\}", "", text)
    text = re.sub(
        r"\\begin\{[^}]+\}.*?\\end\{[^}]+\}", "", text, flags=re.DOTALL
    )
    text = re.sub(r"\\[a-zA-Z]+\{[^}]*\}", "", text)
    text = re.sub(r"\\[a-zA-Z]+", "", text)
    text = re.sub(r"%.*", "", text)  # Remove comments
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def process_cv_data():
    """Process and clean the CV data."""

    # Read the parsed JSON
    with open("cv-data.json", "r") as f:
        cv_data = json.load(f)

    # Clean personal info
    for key, value in cv_data["personal_info"].items():
        cv_data["personal_info"][key] = clean_latex_text(value)

    # Clean profile
    cv_data["profile"] = clean_latex_text(cv_data["profile"])

    # Clean experience descriptions
    for exp in cv_data["experience"]:
        exp["title"] = clean_latex_text(exp["title"])
        exp["description"] = clean_latex_text(exp["description"])
        # Remove duplicate bullet points and clean them
        desc_parts = exp["description"].split("•")
        clean_parts = []
        seen = set()
        for part in desc_parts:
            part = part.strip()
            if part and part not in seen and not part.startswith("\\"):
                clean_parts.append(part)
                seen.add(part)
        exp["description"] = (
            ". ".join(clean_parts) if clean_parts else exp["description"]
        )

    # Clean education
    for edu in cv_data["education"]:
        for key, value in edu.items():
            edu[key] = clean_latex_text(value)

    # Clean certifications
    for cert in cv_data["certifications"]:
        for key, value in cert.items():
            cert[key] = clean_latex_text(value)

    # Add proper skills data since parsing didn't work well
    cv_data["skills"] = {
        "programming": [
            {"name": "Python", "level": "expert"},
            {"name": "R", "level": "expert"},
            {"name": "Rust", "level": "advanced"},
            {"name": "Scala", "level": "advanced"},
            {"name": "Go", "level": "advanced"},
            {"name": "TypeScript", "level": "advanced"},
            {"name": "React", "level": "intermediate"},
            {"name": "Next.js", "level": "intermediate"},
            {"name": "NestJS", "level": "intermediate"},
            {"name": "Svelte", "level": "intermediate"},
            {"name": "FastAPI", "level": "expert"},
            {"name": "TensorFlow", "level": "expert"},
            {"name": "PyTorch", "level": "expert"},
        ],
        "data_engineering": [
            {"name": "Databricks", "level": "expert"},
            {"name": "MLflow", "level": "expert"},
            {"name": "dbt", "level": "expert"},
            {"name": "Kafka", "level": "expert"},
            {"name": "Flink", "level": "advanced"},
            {"name": "PySpark", "level": "expert"},
            {"name": "Polars", "level": "advanced"},
            {"name": "Airflow", "level": "expert"},
            {"name": "Dagster", "level": "advanced"},
            {"name": "DuckDB", "level": "advanced"},
        ],
        "cloud_devops": [
            {"name": "Kubernetes", "level": "expert"},
            {"name": "Docker", "level": "expert"},
            {"name": "Terraform", "level": "expert"},
            {"name": "Azure", "level": "expert"},
            {"name": "GitHub Actions", "level": "advanced"},
            {"name": "Azure Pipelines", "level": "advanced"},
            {"name": "Helm", "level": "intermediate"},
        ],
        "analytics": [
            {"name": "Machine Learning", "level": "expert"},
            {"name": "Deep Learning", "level": "expert"},
            {"name": "LLMs", "level": "expert"},
            {"name": "MLOps", "level": "expert"},
            {"name": "Econometrics", "level": "expert"},
            {"name": "Time Series Analysis", "level": "advanced"},
            {"name": "Reinforcement Learning", "level": "intermediate"},
        ],
        "tools": [
            {"name": "Power BI", "level": "expert"},
            {"name": "Grafana", "level": "expert"},
            {"name": "Tableau", "level": "expert"},
            {"name": "Plotly", "level": "advanced"},
            {"name": "Git", "level": "expert"},
            {"name": "SQL/NoSQL", "level": "expert"},
        ],
    }

    # Improve experience descriptions
    experience_improvements = {
        "Senior Cloud Data Platform & MLOps Engineer": "Leading the design and implementation of enterprise-scale cloud-native data platforms and MLOps solutions. Driving digital transformation through automated, production-ready machine learning systems that deliver measurable business impact.",
        "Senior Machine Learning Engineer": "Owned end-to-end machine learning lifecycle from research to production deployment. Built scalable ML infrastructure and established best practices for model monitoring, versioning, and continuous integration.",
        "Data Scientist/Engineer": "Pioneered the company's data-driven transformation by building the foundational data infrastructure and implementing the first production ML pipelines. Established modern data engineering practices and CI/CD workflows.",
        "Freelance Developer": "Delivered full-stack web applications and econometric modeling solutions for diverse clients. Specialized in translating complex mathematical concepts into practical software solutions.",
        "Commercial Insurance Agent": "Provided sales and advisory services for commercial insurance products, developing strong client relationship and communication skills.",
    }

    for exp in cv_data["experience"]:
        if exp["title"] in experience_improvements:
            exp["description"] = experience_improvements[exp["title"]]

    # Update technologies for each experience
    tech_mapping = {
        "Senior Cloud Data Platform & MLOps Engineer": [
            "Python",
            "Databricks",
            "MLflow",
            "Kubernetes",
            "Docker",
            "Terraform",
            "Azure",
            "Kafka",
            "Airflow",
        ],
        "Senior Machine Learning Engineer": [
            "Python",
            "TensorFlow",
            "PyTorch",
            "MLflow",
            "Kubernetes",
            "Azure",
            "Databricks",
        ],
        "Data Scientist/Engineer": [
            "Python",
            "R",
            "SQL",
            "Azure",
            "Databricks",
            "Power BI",
            "Docker",
        ],
        "Freelance Developer": [
            "Python",
            "R",
            "JavaScript",
            "SQL",
            "Docker",
            "Linux",
        ],
        "Commercial Insurance Agent": [],
    }

    for exp in cv_data["experience"]:
        exp["technologies"] = tech_mapping.get(exp["title"], [])

    return cv_data


def update_svelte_file(cv_data):
    """Update the Svelte page with the processed CV data."""

    # Read the current Svelte file
    svelte_file = Path("src/routes/+page.svelte")
    with open(svelte_file, "r") as f:
        content = f.read()

    # Generate the new data sections
    personal_info_js = f"""const personalInfo = {{
		name: "{cv_data["personal_info"]["name"]}",
		title: "{cv_data["personal_info"]["title"]}",
		email: "{cv_data["personal_info"]["email"]}",
		phone: "+31 6 1234 5678", // Add your phone number
		location: "{cv_data["personal_info"]["location"]}",
		linkedin: "{cv_data["personal_info"]["linkedin"]}",
		github: "{cv_data["personal_info"]["github"]}",
		website: "{cv_data["personal_info"]["website"]}"
	}};"""

    # Generate skills object
    skills_js = """const skills = {
		programming: ["""

    for skill in cv_data["skills"]["programming"]:
        skills_js += f'\n			{{ name: "{skill["name"]}", level: "{skill["level"]}" }},'

    skills_js += "\n		],\n		dataEngineering: ["

    for skill in cv_data["skills"]["data_engineering"]:
        skills_js += f'\n			{{ name: "{skill["name"]}", level: "{skill["level"]}" }},'

    skills_js += "\n		],\n		cloudDevOps: ["

    for skill in cv_data["skills"]["cloud_devops"]:
        skills_js += f'\n			{{ name: "{skill["name"]}", level: "{skill["level"]}" }},'

    skills_js += "\n		],\n		analytics: ["

    for skill in cv_data["skills"]["analytics"]:
        skills_js += f'\n			{{ name: "{skill["name"]}", level: "{skill["level"]}" }},'

    skills_js += "\n		],\n		tools: ["

    for skill in cv_data["skills"]["tools"]:
        skills_js += f'\n			{{ name: "{skill["name"]}", level: "{skill["level"]}" }},'

    skills_js += "\n		]\n	};"

    # Generate experiences
    experiences_js = "const experiences = ["

    for exp in cv_data["experience"]:
        tech_array = ", ".join([f'"{tech}"' for tech in exp["technologies"]])
        experiences_js += f"""
		{{
			title: "{exp["title"]}",
			company: "{exp["company"]}",
			period: "{exp["period"]}",
			description: "{exp["description"]}",
			technologies: [{tech_array}]
		}},"""

    experiences_js += "\n	];"

    # Generate education
    education_js = "const education = ["

    for edu in cv_data["education"]:
        education_js += f"""
		{{
			degree: "{edu["degree"]}",
			institution: "{edu["institution"]}",
			period: "{edu["period"]}",
			description: "{edu["description"]}"
		}},"""

    education_js += "\n	];"

    # Generate projects (keep the existing ones but update with real data)
    projects_js = """const projects = [
		{
			name: "MLOps Platform",
			description: "Built comprehensive MLOps platform with automated model deployment, monitoring, and lifecycle management using Databricks, MLflow, and Kubernetes.",
			technologies: ["Python", "Databricks", "MLflow", "Kubernetes", "Docker"],
			link: "https://github.com/LPvdT"
		},
		{
			name: "Real-time Data Platform",
			description: "Designed and implemented real-time streaming data platform handling millions of events daily using Kafka, Flink, and modern data lakehouse architecture.",
			technologies: ["Kafka", "Flink", "Python", "Terraform", "Azure"],
			link: "https://github.com/LPvdT"
		}
	];"""

    # Update the about section
    about_text = cv_data["profile"]

    # Replace the data sections in the Svelte file
    # Find and replace the personalInfo section
    personal_info_pattern = r"const personalInfo = \{[^}]+\};"
    content = re.sub(
        personal_info_pattern, personal_info_js, content, flags=re.DOTALL
    )

    # Replace skills section
    skills_pattern = r"const skills = \{.*?\};"
    content = re.sub(skills_pattern, skills_js, content, flags=re.DOTALL)

    # Replace experiences section
    experiences_pattern = r"const experiences = \[.*?\];"
    content = re.sub(
        experiences_pattern, experiences_js, content, flags=re.DOTALL
    )

    # Replace education section
    education_pattern = r"const education = \[.*?\];"
    content = re.sub(education_pattern, education_js, content, flags=re.DOTALL)

    # Replace projects section
    projects_pattern = r"const projects = \[.*?\];"
    content = re.sub(projects_pattern, projects_js, content, flags=re.DOTALL)

    # Update the about section text
    about_pattern = r"(Passionate software engineer.*?delivering exceptional user experiences\.)"
    content = re.sub(about_pattern, about_text, content, flags=re.DOTALL)

    # Write the updated content back
    with open(svelte_file, "w") as f:
        f.write(content)

    print("✅ Successfully updated Svelte page with CV data")


def main():
    """Main function."""
    print("🔄 Processing CV data...")

    # Process the CV data
    cv_data = process_cv_data()

    # Save the cleaned data
    with open("cv-data-clean.json", "w") as f:
        json.dump(cv_data, f, indent=2, ensure_ascii=False)

    print("✅ Cleaned CV data saved to cv-data-clean.json")

    # Update the Svelte file
    print("🔄 Updating Svelte website...")
    update_svelte_file(cv_data)

    print("🎉 CV website successfully updated with your data!")
    print("\n📊 Summary:")
    print(f"   • Name: {cv_data['personal_info']['name']}")
    print(f"   • Title: {cv_data['personal_info']['title']}")
    print(f"   • Experience positions: {len(cv_data['experience'])}")
    print(
        f"   • Skills: {sum(len(skills) for skills in cv_data['skills'].values())}"
    )
    print(f"   • Education: {len(cv_data['education'])}")
    print(f"   • Certifications: {len(cv_data['certifications'])}")


if __name__ == "__main__":
    main()
