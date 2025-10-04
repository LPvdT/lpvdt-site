<script lang="ts">
	let {
		skill,
		level = 'intermediate',
		delay = 0
	}: {
		skill: string;
		level?: 'beginner' | 'intermediate' | 'advanced' | 'expert' | string;
		delay?: number;
	} = $props();

	const levelColors = {
		beginner: 'bg-gray-100 text-gray-700 border-gray-200',
		intermediate: 'bg-blue-100 text-blue-700 border-blue-200',
		advanced: 'bg-green-100 text-green-700 border-green-200',
		expert: 'bg-purple-100 text-purple-700 border-purple-200'
	};
</script>

<span
	class="animate-fade-in inline-block rounded-full border px-3 py-1 text-sm font-medium opacity-0 transition-all duration-300 hover:scale-105 hover:shadow-md {levelColors[
		level
	]}"
	style="animation-delay: {delay}ms"
>
	{skill}
</span>
