<script lang="ts">
	let {
		title,
		company,
		period,
		description,
		technologies = [],
		delay = 0
	}: {
		title: string;
		company: string;
		period: string;
		description: string;
		technologies?: string[];
		delay?: number;
	} = $props();
</script>

<div
	class="animate-slide-in-left card opacity-0 p-6"
	style="animation-delay: {delay}ms"
>
	<div class="mb-3 flex flex-col sm:flex-row sm:items-start sm:justify-between">
		<div>
			<h3 class="text-lg font-semibold text-primary mb-1">{title}</h3>
			<p class="font-medium text-accent">{company}</p>
		</div>
		<span class="mt-1 text-sm text-muted sm:mt-0">{period}</span>
	</div>

	<p class="mb-4 leading-relaxed text-secondary">{description}</p>

	{#if technologies.length > 0}
		<div class="flex flex-wrap gap-2">
			{#each technologies as tech, i}
				<span class="rounded-md bg-tertiary border border-primary px-2.5 py-1 text-xs font-medium text-secondary transition-colors hover:bg-secondary">
					{tech}
				</span>
			{/each}
		</div>
	{/if}
</div>
