<script lang="ts">
  import { Section, ExperienceCard, ScrollToTop, SkillTag, content } from "$lib";
  import { Download, Mail, MapPin, ExternalLink, Globe } from "lucide-svelte";
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
          {content.personalInfo.name}
        </h1>

        <p
          class="animate-slide-in-up animate-delay-400 mb-8 font-medium tracking-wide text-blue-100/90 opacity-0"
          style="font-size: clamp(1.125rem, 2.5vw, 1.5rem);"
        >
          {content.personalInfo.title}
        </p>

        <div
          class="animate-fade-in animate-delay-500 mb-8 flex flex-wrap justify-center gap-6 opacity-0"
        >
          <a
            href="mailto:{content.personalInfo.email}"
            class="flex items-center gap-2 text-blue-100/90 transition-all duration-300 hover:scale-105 hover:text-white"
          >
            <Mail size={20} />
            <span class="hidden font-medium sm:inline"
              >{content.personalInfo.email}</span
            >
          </a>
          <div class="flex items-center gap-2 text-blue-100/90">
            <MapPin size={20} />
            <span class="font-medium">{content.personalInfo.location}</span>
          </div>
        </div>

        <div
          class="animate-fade-in animate-delay-600 flex justify-center gap-4 opacity-0"
        >
          <!-- TODO: Update ExternalLink icon to something better -->
          <a
            href={content.personalInfo.linkedin}
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
            href={content.personalInfo.github}
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
            href={content.personalInfo.website}
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
              {#each content.skills.programming as skill, i}
                <SkillTag skill={skill.name} level={skill.level} delay={i * 100} />
              {/each}
            </div>
          </div>

          <div class="card p-6">
            <h3 class="text-primary mb-4 font-semibold">Data Engineering & MLOps</h3>
            <div class="flex flex-wrap gap-2">
              {#each content.skills.dataEngineering as skill, i}
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
              {#each content.skills.cloudDevOps as skill, i}
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
              {#each content.skills.advancedAnalytics as skill, i}
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
              {#each content.skills.tools as skill, i}
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
          {#each content.experiences as experience, i}
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
          {#each content.projects as project, i}
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
        {#each content.education as edu, i}
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
        &copy; {new Date().getFullYear()} &nbsp;{content.personalInfo.name}. All rights
        reserved.
      </p>
    </div>
  </footer>

  <ScrollToTop />
</main>
