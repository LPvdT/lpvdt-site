<script lang="ts">
const {
  title,
  company,
  period,
  description,
  technologies = [],
  delay = 0
}: {
  title: string
  company: string
  period: string
  description: string
  technologies?: string[]
  delay?: number
} = $props()
</script>

<div
  class="animate-slide-in-left card p-6 opacity-0"
  style="animation-delay: {delay}ms"
>
  <div class="mb-3 flex flex-col sm:flex-row sm:items-start sm:justify-between">
    <div>
      <h3 class="text-primary mb-1 text-lg font-semibold">{title}</h3>
      <p class="text-accent font-medium">{company}</p>
    </div>
    <span class="text-muted mt-1 text-sm sm:mt-0">{period}</span>
  </div>

  <p class="text-secondary mb-4 leading-relaxed">{description}</p>

  {#if technologies.length > 0}
    <div class="flex flex-wrap gap-2">
      {#each technologies as tech, i}
        <span
          class="bg-tertiary border-primary text-secondary hover:bg-secondary rounded-md border px-2.5 py-1 text-xs font-medium transition-colors"
        >
          {tech}
        </span>
      {/each}
    </div>
  {/if}
</div>
