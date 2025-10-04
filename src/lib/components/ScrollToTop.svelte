<script lang="ts">
	import { ChevronUp } from 'lucide-svelte';
	import { onMount } from 'svelte';

	let showButton = $state(false);

	onMount(() => {
		const handleScroll = () => {
			showButton = window.scrollY > 300;
		};

		window.addEventListener('scroll', handleScroll);

		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});

	function scrollToTop() {
		window.scrollTo({
			top: 0,
			behavior: 'smooth'
		});
	}
</script>

{#if showButton}
	<button
		onclick={scrollToTop}
		class="animate-fade-in no-print fixed right-8 bottom-8 z-50 rounded-full bg-accent p-3 text-white opacity-0 shadow-lg transition-all duration-300 hover:scale-110 hover:bg-accent-hover group"
		aria-label="Scroll to top"
		title="Scroll to top"
	>
		<ChevronUp size={24} class="group-hover:animate-bounce-subtle" />
	</button>
{/if}
