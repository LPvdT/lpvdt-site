<script lang="ts">
  // TODO: Check all content in development
  import { Download, Mail, MapPin, ExternalLink, Globe } from "lucide-svelte";
  import Section from "$lib/components/Section.svelte";
  import SkillTag from "$lib/components/SkillTag.svelte";
  import ExperienceCard from "$lib/components/ExperienceCard.svelte";
  import ScrollToTop from "$lib/components/ScrollToTop.svelte";

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

        - Led development of scalable scrapers, crawlers, and interactive
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
</script>

<svelte:head>
  <title>Laurens van der Tas - Professional CV</title>
</svelte:head>

<main class="min-h-screen">
  <!-- Hero Section -->
  <section
    class="relative overflow-hidden bg-gradient-to-br from-indigo-600 via-purple-600 to-blue-700 text-white"
  >
    <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent"></div>
    <div class="absolute inset-0">
      <div
        class="animate-float absolute top-10 left-10 h-2 w-2 rounded-full bg-white/20"
      ></div>
      <div
        class="animate-float absolute right-20 bottom-20 h-3 w-3 rounded-full bg-white/10"
        style="animation-delay: 2s"
      ></div>
      <div
        class="animate-float absolute top-1/2 left-1/4 h-1 w-1 rounded-full bg-white/30"
        style="animation-delay: 4s"
      ></div>
    </div>
    <div class="relative mx-auto max-w-4xl px-6 py-20">
      <div class="text-center">
        <div
          class="animate-scale-in animate-delay-200 mx-auto mb-8 flex h-32 w-32 items-center justify-center rounded-full bg-white/90 opacity-0 shadow-2xl ring-4 ring-white/20 backdrop-blur-sm"
        >
          <span class="gradient-text text-4xl font-bold">LT</span>
        </div>

        <h1
          class="animate-slide-in-up animate-delay-300 mb-4 font-bold tracking-tight opacity-0"
          style="font-size: clamp(2.5rem, 5vw, 4rem); line-height: 1.1;"
        >
          {personalInfo.name}
        </h1>

        <p
          class="animate-slide-in-up animate-delay-400 mb-8 font-medium tracking-wide text-blue-100/90 opacity-0"
          style="font-size: clamp(1.125rem, 2.5vw, 1.5rem);"
        >
          {personalInfo.title}
        </p>

        <div
          class="animate-fade-in animate-delay-500 mb-8 flex flex-wrap justify-center gap-6 opacity-0"
        >
          <a
            href="mailto:{personalInfo.email}"
            class="flex items-center gap-2 text-blue-100/90 transition-all duration-300 hover:scale-105 hover:text-white"
          >
            <Mail size={20} />
            <span class="hidden font-medium sm:inline">{personalInfo.email}</span>
          </a>
          <div class="flex items-center gap-2 text-blue-100/90">
            <MapPin size={20} />
            <span class="font-medium">{personalInfo.location}</span>
          </div>
        </div>

        <div
          class="animate-fade-in animate-delay-600 flex justify-center gap-4 opacity-0"
        >
          <!-- TODO: Update ExternalLink icon to something better -->
          <a
            href={personalInfo.linkedin}
            target="_blank"
            class="glass group rounded-full p-3 transition-all duration-300 hover:scale-110 hover:bg-white/30"
            aria-label="LinkedIn Profile"
          >
            <ExternalLink
              size={24}
              class="transition-transform duration-300 group-hover:rotate-12"
            />
          </a>
          <a
            href={personalInfo.github}
            target="_blank"
            class="glass group rounded-full p-3 transition-all duration-300 hover:scale-110 hover:bg-white/30"
            aria-label="GitHub Profile"
          >
            <ExternalLink
              size={24}
              class="transition-transform duration-300 group-hover:rotate-12"
            />
          </a>
          <a
            href={personalInfo.website}
            target="_blank"
            class="glass group rounded-full p-3 transition-all duration-300 hover:scale-110 hover:bg-white/30"
            aria-label="Personal Website"
          >
            <Globe
              size={24}
              class="transition-transform duration-300 group-hover:rotate-12"
            />
          </a>
          <a
            href="/Laurens-van-der-Tas-CV.pdf"
            target="_blank"
            class="glass group rounded-full p-3 transition-all duration-300 hover:scale-110 hover:bg-white/30"
            aria-label="Download CV"
          >
            <Download size={24} class="group-hover:animate-bounce-subtle" />
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Main Content -->
  <div class="mx-auto max-w-4xl px-6 py-12">
    <!-- About Section -->
    <div id="about">
      <Section title="About" animationDelay={100}>
        <div class="card p-6">
          <p class="text-secondary text-lg leading-relaxed">
            Senior Data Platform & MLOps Engineer with a track record of building data
            systems from the ground up and guiding them into fully automated,
            production-grade platforms. My career began at the intersection of
            econometrics and software engineering as a freelance developer, progressed
            into data science and advanced analytics, and has since evolved into leading
            machine learning and MLOps initiatives at scale. I bring a unique blend of
            engineering craftsmanship and quantitative expertise, backed by an MSc with
            a solid econometric background. Whether designing architectures,
            operationalizing ML, or mentoring teams, I focus on turning complex data
            problems into solutions that deliver long-term value. Academic excellence
            (both theses graded 9/10) underscores a commitment to precision, while
            open-source contributions and continuous learning reflect my drive to stay
            ahead in a rapidly changing field.
          </p>
        </div>
      </Section>
    </div>
    <!-- Skills Section -->
    <div id="skills">
      <Section title="Skills" animationDelay={200}>
        <div class="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Programming</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.programming as skill, i}
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100} />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Data Engineering & MLOps</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.dataEngineering as skill, i}
                <SkillTag
                  skill={skill.name}
                  level={skill.level}
                  delay={i * 100 + 200}
                />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Cloud & DevOps</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.cloudDevOps as skill, i}
                <SkillTag
                  skill={skill.name}
                  level={skill.level}
                  delay={i * 100 + 300}
                />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Analytics & ML</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.advancedAnalytics as skill, i}
                <SkillTag
                  skill={skill.name}
                  level={skill.level}
                  delay={i * 100 + 400}
                />
              {/each}
            </div>
          </div>

          <div class="card p-6 md:col-span-2 lg:col-span-2">
            <h3 class="text-primary mb-4 font-semibold">Tools & Platforms</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.tools as skill, i}
                <SkillTag
                  skill={skill.name}
                  level={skill.level}
                  delay={i * 100 + 500}
                />
              {/each}
            </div>
          </div>
        </div>
      </Section>
    </div>

    <!-- Experience Section -->
    <div id="experience">
      <Section title="Work Experience" animationDelay={300}>
        <div class="space-y-6">
          {#each experiences as experience, i}
            <ExperienceCard
              title={experience.title}
              company={experience.company}
              period={experience.period}
              description={experience.description}
              delay={i * 200}
            />
          {/each}
        </div>
      </Section>
    </div>

    <!-- Projects Section -->
    <div id="projects">
      <Section title="Featured Projects" animationDelay={400}>
        <div class="grid gap-6 md:grid-cols-2">
          {#each projects as project, i}
            <div
              class="animate-slide-in-right card p-6 opacity-0"
              style="animation-delay: {i * 200}ms"
            >
              <h3 class="text-primary mb-2 text-lg font-semibold">
                {project.name}
              </h3>
              <p class="text-secondary mb-4">{project.description}</p>
              <div class="mb-4 flex flex-wrap gap-2">
                {#each project.technologies as tech}
                  <span
                    class="bg-tertiary border-primary text-secondary hover:bg-secondary rounded-md border px-2.5 py-1 text-xs font-medium transition-colors"
                  >
                    {tech}
                  </span>
                {/each}
              </div>
              <a
                href={project.link}
                target="_blank"
                class="text-accent hover:text-accent group inline-flex items-center gap-2 font-medium transition-all duration-300 hover:scale-105"
              >
                <ExternalLink
                  size={16}
                  class="transition-transform duration-300 group-hover:rotate-12"
                />
                View Project
              </a>
            </div>
          {/each}
        </div>
      </Section>
    </div>

    <!-- Education Section -->
    <div id="education">
      <Section title="Education" animationDelay={500}>
        {#each education as edu, i}
          <div
            class="animate-slide-in-left card p-6 opacity-0"
            style="animation-delay: {i * 200}ms"
          >
            <div
              class="mb-3 flex flex-col sm:flex-row sm:items-start sm:justify-between"
            >
              <div>
                <h3 class="text-primary text-lg font-semibold">{edu.degree}</h3>
                <p class="text-accent font-medium">{edu.institution}</p>
              </div>
              <span class="text-muted mt-1 text-sm sm:mt-0">{edu.period}</span>
            </div>
            <p class="text-secondary">{edu.description}</p>
          </div>
        {/each}
      </Section>
    </div>
  </div>

  <!-- Footer -->
  <footer class="bg-secondary border-primary transition-theme mt-16 border-t py-8">
    <div class="mx-auto max-w-4xl px-6 text-center">
      <p class="text-muted">
        &copy; {new Date().getFullYear()} &nbsp;{personalInfo.name}. All rights
        reserved.
      </p>
    </div>
  </footer>

  <ScrollToTop />
</main>
