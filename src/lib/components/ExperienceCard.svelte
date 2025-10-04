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
	class="animate-slide-in-left rounded-lg border border-gray-100 bg-white p-6 opacity-0 shadow-sm transition-all duration-300 hover:border-gray-200 hover:shadow-lg"
	style="animation-delay: {delay}ms"
>
	<div class="mb-3 flex flex-col sm:flex-row sm:items-start sm:justify-between">
		<div>
			<h3 class="text-lg font-semibold text-gray-900">{title}</h3>
			<p class="font-medium text-blue-600">{company}</p>
		</div>
		<span class="mt-1 text-sm text-gray-500 sm:mt-0">{period}</span>
	</div>

	<p class="mb-4 leading-relaxed text-gray-700">{description}</p>

	{#if technologies.length > 0}
		<div class="flex flex-wrap gap-2">
			{#each technologies as tech, i}
				<span class="rounded-md bg-gray-100 px-2 py-1 text-xs font-medium text-gray-700">
					{tech}
				</span>
			{/each}
		</div>
	{/if}
</div>
