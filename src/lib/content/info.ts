const personalInfo = {
  name: "Laurens van der Tas",
  title: "Senior Cloud Data Platform & MLOps Engineer",
  email: "laurens.vandertas@gmail.com",
  location: "Rotterdam, South Holland, Netherlands",
  linkedin: "https://linkedin.com/in/lpvdt",
  github: "https://github.com/LPvdT",
  website: "https://lpvdt.github.io"
};

const skills = {
  programming: [
    { name: "Python", level: "expert" },
    { name: "R", level: "advanced" },
    { name: "Rust", level: "intermediate" },
    { name: "Scala", level: "intermediate" },
    { name: "Go", level: "intermediate" },
    { name: "TypeScript", level: "advanced" },
    { name: "React", level: "advanced" },
    { name: "Next.js", level: "advanced" },
    { name: "NestJS", level: "advanced" },
    { name: "Svelte", level: "intermediate" },
    { name: "FastAPI", level: "expert" },
    { name: "TensorFlow", level: "advanced" },
    { name: "PyTorch", level: "expert" },
    { name: "Bash", level: "expert" }
  ],
  dataEngineering: [
    { name: "Databricks", level: "expert" },
    { name: "MLflow", level: "expert" },
    { name: "dbt", level: "advanced" },
    { name: "Kafka", level: "advanced" },
    { name: "Flink", level: "intermediate" },
    { name: "PySpark", level: "expert" },
    { name: "Polars", level: "expert" },
    { name: "Databricks Workflows", level: "expert" },
    { name: "Airflow", level: "intermediate" },
    { name: "Dagster", level: "advanced" },
    { name: "DuckDB", level: "advanced" },
    { name: "ETL/ELT/CDC", level: "expert" },
    { name: "Database & Data Lakehouse Design", level: "expert" }
  ],
  cloudDevOps: [
    { name: "Kubernetes", level: "advanced" },
    { name: "Docker", level: "expert" },
    { name: "Terraform", level: "advanced" },
    { name: "Azure", level: "expert" },
    { name: "AWS", level: "advanced" },
    { name: "GCP", level: "intermediate" },
    { name: "GitHub Actions", level: "expert" },
    { name: "Azure Pipelines", level: "expert" },
    { name: "Helm", level: "intermediate" }
  ],
  advancedAnalytics: [
    { name: "Machine Learning (all algorithms)", level: "expert" },
    { name: "Deep Learning", level: "expert" },
    { name: "LLMs (fine-tuning, inference & deployment)", level: "advanced" },
    { name: "MLOps", level: "expert" },
    { name: "Econometric Modeling", level: "expert" },
    { name: "Time Series Analysis", level: "expert" },
    { name: "Reinforcement Learning", level: "intermediate" }
  ],
  tools: [
    { name: "Power BI", level: "advanced" },
    { name: "Grafana", level: "expert" },
    { name: "Tableau", level: "advanced" },
    { name: "Plotly", level: "advanced" },
    { name: "Stata", level: "advanced" },
    { name: "Git", level: "expert" },
    { name: "SQL/NoSQL", level: "expert" },
    { name: "*NIX", level: "expert" },
    { name: "APIs (REST/GraphQL)", level: "expert" }
  ]
};

const experiences = [
  {
    title: "Senior Cloud Data Platform & MLOps Engineer",
    company: "DELTA Fiber",
    period: "Sep 2024 -- Present",
    // TODO: Fix HTML rendering
    description: `Shaping the company's cloud-native data platform as a lead engineer and
    principal driver of its strategy, embedding modern MLOps practices to ensure
    scalability, reliability, and long-term value.
    Operating at the intersection
    of infrastructure, data engineering, and applied machine learning, I guide
    teams and stakeholders toward automated, production-ready solutions that
    deliver tangible impact across the organization.

    - Spearheaded the evolution of enterprise-wide data solutions, among
    which streaming solutions, increasing analytical efficiency and reducing
    deployment friction.

    - Architected and maintained AI-enabled systems, including ML models,
    APIs, and end-to-end data pipelines, ensuring robustness and operational
    reliability.

    - Implemented MLOps best practices: continuous integration/deployment
    for ML models, monitoring, alerting, and model lifecycle management to
    guarantee production stability.

    visualization platforms, expanding data accessibility and enabling faster,
    data-driven decision-making.
    `
  },
  {
    title: "Senior Machine Learning Engineer",
    company: "DELTA Fiber",
    period: "Nov 2021 -- Aug 2024",
    // TODO: Fix HTML rendering
    description: `Took ownership of the company's machine learning stack, ensuring models were
    not just experimental prototypes but reliable, monitored, and continuously
    improving production assets. Collaborated with business units to deliver
    insights and predictive capabilities that shaped strategic decision-making.

    - Led integration of machine learning models into production systems.
    - Built and maintained scalable pipelines and automated workflows.
    - Supported data-driven decision-making with advanced analytics and visualizations.
    `
  },
  {
    title: "Data Scientist/Engineer",
    company: "DELTA Fiber",
    period: "Nov 2018 -- Oct 2021",
    // TODO: Fix HTML rendering
    description: `
    Pioneered the company's advanced analytics journey by establishing its first
    modern data infrastructure and operational machine learning pipelines.
    Balanced the dual role of data scientist and engineer, laying the groundwork
    for scalable platforms that later became critical to the business.

    - Designed and deployed the first company-wide data warehouse and ETL processes.
    - Delivered initial advanced analytics solutions, including predictive models and automated APIs.
    - Established CI/CD practices for data science and engineering workflows.
    - Created scrapers, crawlers, and BI dashboards to improve operational visibility.
    `
  },
  {
    title: "Freelance Developer",
    company: "Private Clients",
    period: "Sep 2012 -- Aug 2018",
    // TODO: Fix HTML rendering
    description: `
    Independent developer combining econometric modelling with full-stack web
    solutions for a variety of clients. This role honed my ability to translate
    mathematical concepts into practical applications and gave me hands-on
    experience with diverse stacks, architectures, and deployment strategies.

    - Built and deployed full-stack web applications and APIs across multiple frameworks.
    - Developed econometric modelling solutions to support research and business cases.
    - Applied statistical modelling and data analysis in client-focused projects.
    - Gained experience with distributed systems, containerization, and
        automation before moving into large-scale enterprise environments.
    `
  },
  {
    title: "Commercial Insurance Agent",
    company: "Achmea",
    period: "2010 -- 2011",
    // TODO: Fix HTML rendering
    description: `
    Worked in sales and advisory for commercial insurance products.
    `
  }
];

const education = [
  {
    degree: "MSc Banking & Finance",
    institution: "Utrecht University",
    period: "2016 -- 2018",
    description:
      "Focus on quantitative finance, econometrics, and investment management. Thesis on machine learning (graded 9/10)."
  },
  {
    degree: "BSc Economics & Business Economics",
    institution: "Utrecht University",
    period: "2012 -- 2015",
    description:
      "Customized programme emphasizing econometrics, statistics, and finance. Thesis graded 9/10."
  },
  {
    degree: "International Business and Management Studies",
    institution: "Avans University of Applied Sciences",
    period: "2011",
    description: "Propaedeutic obtained (in half a year)."
  },
  {
    degree: "Pre-University Education (VWO)",
    institution: "Edison College",
    period: "2004 -- 2010",
    description: "Science & Technology Profile."
  }
];

const projects = [
  {
    name: "CSV Generator",
    description:
      "High performance CSV generator written in Python for generating huge datasets in seconds. Options for both Numpy and Faker.",
    technologies: ["Python", "GitHub Actions", "uv"],
    link: "https://github.com/LPvdT/csv-gen"
  },
  {
    name: "Scraping Pokemon",
    description: "Scraping of Pokemon data using Python, Scrapy, and uv.",
    technologies: ["Python", "Scrapy", "uv"],
    link: "https://github.com/LPvdT/scraping-pokemon"
  }
];

export default {
  personalInfo,
  skills,
  experiences,
  education,
  projects
};
