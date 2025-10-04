<script lang="ts">
	let {
		title,
		children,
		class: className = '',
		animationDelay = 0
	}: {
		title: string;
		children: any;
		class?: string;
		animationDelay?: number;
	} = $props();
</script>

<section
	class="animate-slide-in-up mb-12 opacity-0 {className}"
	style="animation-delay: {animationDelay}ms"
>
	<h2 class="gradient-text mb-6 text-2xl font-bold">
		{title}
	</h2>
	<div class="space-y-4">
		{@render children()}
	</div>
</section>
