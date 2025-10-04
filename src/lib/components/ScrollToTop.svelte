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
		class="animate-fade-in no-print fixed right-8 bottom-8 z-50 rounded-full bg-blue-600 p-3 text-white opacity-0 shadow-lg transition-all duration-300 hover:scale-110 hover:bg-blue-700"
		aria-label="Scroll to top"
	>
		<ChevronUp size={24} />
	</button>
{/if}
