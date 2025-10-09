<script lang="ts">
  import { Download, Mail, MapPin, ExternalLink, Globe } from 'lucide-svelte';
  import Section from '$lib/components/Section.svelte';
  import SkillTag from '$lib/components/SkillTag.svelte';
  import ExperienceCard from '$lib/components/ExperienceCard.svelte';
  import ScrollToTop from '$lib/components/ScrollToTop.svelte';

  // TODO: CV Data - Replace with your actual information
  const personalInfo = {
    name: 'Laurens van der Tas',
    title: 'Senior Cloud Data Platform & MLOps Engineer',
    email: 'laurens.vandertas@gmail.com',
    location: 'Rotterdam, South Holland, Netherlands',
    linkedin: 'https://linkedin.com/in/lpvdt',
    github: 'https://github.com/LPvdT',
    website: 'https://lpvdt.github.io',
  };

  const skills = {
    programming: [
      { name: 'Python', level: 'expert' },
      { name: 'R', level: 'expert' },
      { name: 'Rust', level: 'advanced' },
      { name: 'Scala', level: 'advanced' },
      { name: 'Go', level: 'advanced' },
      { name: 'TypeScript', level: 'advanced' },
      { name: 'React', level: 'intermediate' },
      { name: 'Next.js', level: 'intermediate' },
      { name: 'NestJS', level: 'intermediate' },
      { name: 'Svelte', level: 'intermediate' },
      { name: 'FastAPI', level: 'expert' },
      { name: 'TensorFlow', level: 'expert' },
      { name: 'PyTorch', level: 'expert' },
    ],
    dataEngineering: [
      { name: 'Databricks', level: 'expert' },
      { name: 'MLflow', level: 'expert' },
      { name: 'dbt', level: 'expert' },
      { name: 'Kafka', level: 'expert' },
      { name: 'Flink', level: 'advanced' },
      { name: 'PySpark', level: 'expert' },
      { name: 'Polars', level: 'advanced' },
      { name: 'Airflow', level: 'expert' },
      { name: 'Dagster', level: 'advanced' },
      { name: 'DuckDB', level: 'advanced' },
    ],
    cloudDevOps: [
      { name: 'Kubernetes', level: 'expert' },
      { name: 'Docker', level: 'expert' },
      { name: 'Terraform', level: 'expert' },
      { name: 'Azure', level: 'expert' },
      { name: 'GitHub Actions', level: 'advanced' },
      { name: 'Azure Pipelines', level: 'advanced' },
      { name: 'Helm', level: 'intermediate' },
    ],
    analytics: [
      { name: 'Machine Learning', level: 'expert' },
      { name: 'Deep Learning', level: 'expert' },
      { name: 'LLMs', level: 'expert' },
      { name: 'MLOps', level: 'expert' },
      { name: 'Econometrics', level: 'expert' },
      { name: 'Time Series Analysis', level: 'advanced' },
      { name: 'Reinforcement Learning', level: 'intermediate' },
    ],
    tools: [
      { name: 'Power BI', level: 'expert' },
      { name: 'Grafana', level: 'expert' },
      { name: 'Tableau', level: 'expert' },
      { name: 'Plotly', level: 'advanced' },
      { name: 'Git', level: 'expert' },
      { name: 'SQL/NoSQL', level: 'expert' },
    ],
  };

  const experiences = [
    {
      title: 'Senior Cloud Data Platform & MLOps Engineer',
      company: 'DELTA Fiber',
      period: 'Sep 2024 -- Present',
      description:
        'Leading the design and implementation of enterprise-scale cloud-native data platforms and MLOps solutions. Driving digital transformation through automated, production-ready machine learning systems that deliver measurable business impact.',
      technologies: [
        'Python',
        'Databricks',
        'MLflow',
        'Kubernetes',
        'Docker',
        'Terraform',
        'Azure',
        'Kafka',
        'Airflow',
      ],
    },
    {
      title: 'Senior Machine Learning Engineer',
      company: 'DELTA Fiber',
      period: 'Nov 2021 -- Aug 2024',
      description:
        'Owned end-to-end machine learning lifecycle from research to production deployment. Built scalable ML infrastructure and established best practices for model monitoring, versioning, and continuous integration.',
      technologies: [
        'Python',
        'TensorFlow',
        'PyTorch',
        'MLflow',
        'Kubernetes',
        'Azure',
        'Databricks',
      ],
    },
    {
      title: 'Data Scientist/Engineer',
      company: 'DELTA Fiber',
      period: 'Nov 2018 -- Oct 2021',
      description:
        "Pioneered the company's data-driven transformation by building the foundational data infrastructure and implementing the first production ML pipelines. Established modern data engineering practices and CI/CD workflows.",
      technologies: ['Python', 'R', 'SQL', 'Azure', 'Databricks', 'Power BI', 'Docker'],
    },
    {
      title: 'Freelance Developer',
      company: 'Private Clients',
      period: 'Sep 2012 -- Aug 2018',
      description:
        'Delivered full-stack web applications and econometric modeling solutions for diverse clients. Specialized in translating complex mathematical concepts into practical software solutions.',
      technologies: ['Python', 'R', 'JavaScript', 'SQL', 'Docker', 'Linux'],
    },
    {
      title: 'Commercial Insurance Agent',
      company: 'Achmea',
      period: '2010 -- 2011',
      description:
        'Provided sales and advisory services for commercial insurance products, developing strong client relationship and communication skills.',
      technologies: [],
    },
  ];

  const education = [
    {
      degree: 'MSc Banking & Finance',
      institution: 'Utrecht University',
      period: '2016 -- 2018',
      description:
        'Focus on quantitative finance, econometrics, and investment management. Thesis on machine learning',
    },
    {
      degree: 'BSc Economics & Business Economics',
      institution: 'Utrecht University',
      period: '2012 -- 2015',
      description:
        'Customized programme emphasizing econometrics, statistics, and finance. Thesis graded',
    },
    {
      degree: 'International Business and Management Studies',
      institution: 'Avans University of Applied Sciences',
      period: '2011',
      description: 'Propaedeutic obtained',
    },
    {
      degree: 'Pre-University Education (VWO)',
      institution: 'Edison College',
      period: '2004 -- 2010',
      description: 'Science',
    },
  ];

  const projects = [
    {
      name: 'MLOps Platform',
      description:
        'Built comprehensive MLOps platform with automated model deployment, monitoring, and lifecycle management using Databricks, MLflow, and Kubernetes.',
      technologies: ['Python', 'Databricks', 'MLflow', 'Kubernetes', 'Docker'],
      link: 'https://github.com/LPvdT',
    },
    {
      name: 'Real-time Data Platform',
      description:
        'Designed and implemented real-time streaming data platform handling millions of events daily using Kafka, Flink, and modern data lakehouse architecture.',
      technologies: ['Kafka', 'Flink', 'Python', 'Terraform', 'Azure'],
      link: 'https://github.com/LPvdT',
    },
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
      <div class="animate-float absolute top-10 left-10 h-2 w-2 rounded-full bg-white/20"></div>
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

        <div class="animate-fade-in animate-delay-600 flex justify-center gap-4 opacity-0">
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
            <Globe size={24} class="transition-transform duration-300 group-hover:rotate-12" />
          </a>
          <a
            href="/Laurens-van-der-Tas-CV.pdf"
            target="_blank"
            class="animate-pulse-soft group rounded-full bg-white p-3 text-indigo-600 shadow-lg transition-all duration-300 hover:scale-110 hover:bg-indigo-50"
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
            Senior Data Platform & MLOps Engineer with a track record of building data systems from
            the ground up and guiding them into fully automated, production-grade platforms. My
            career began at the intersection of econometrics and software engineering as a freelance
            developer, progressed into data science and advanced analytics, and has since evolved
            into leading machine learning and MLOps initiatives at scale. I bring a unique blend of
            engineering craftsmanship and quantitative expertise, backed by an MSc with a solid
            econometric background. Whether designing architectures, operationalizing ML, or
            mentoring teams, I focus on turning complex data problems into solutions that deliver
            long-term value. Academic excellence (both theses graded 9/10) underscores a commitment
            to precision, while open-source contributions and continuous learning reflect my drive
            to stay ahead in a rapidly changing field.
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
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100 + 200} />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Cloud & DevOps</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.cloudDevOps as skill, i}
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100 + 300} />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Analytics & ML</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.analytics as skill, i}
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100 + 400} />
              {/each}
            </div>
          </div>

          <div class="card p-6 md:col-span-2 lg:col-span-2">
            <h3 class="text-primary mb-4 font-semibold">Tools & Platforms</h3>
            <div class="flex flex-wrap gap-2">
              {#each skills.tools as skill, i}
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100 + 500} />
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
              technologies={experience.technologies}
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
            <div class="mb-3 flex flex-col sm:flex-row sm:items-start sm:justify-between">
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
        &copy; {new Date().getFullYear()} &nbsp;{personalInfo.name}. All rights reserved.
      </p>
    </div>
  </footer>

  <ScrollToTop />
</main>
