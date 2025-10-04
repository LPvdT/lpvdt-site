<script lang="ts">
	import '../app.css';
	import favicon from '$lib/assets/favicon.svg';
	import { browser } from '$app/environment';
	import { onMount } from 'svelte';
	import { Sun, Moon } from 'lucide-svelte';

	let { children } = $props();

	let isDark = $state(false);

	function updateTheme() {
		const theme = isDark ? 'dark' : 'light';
		document.documentElement.setAttribute('data-theme', theme);
		if (browser) {
			localStorage.setItem('theme', theme);
		}
	}

	function toggleTheme() {
		isDark = !isDark;
		updateTheme();
	}

	onMount(() => {
		// Check for saved theme preference or default to system preference
		const savedTheme = localStorage.getItem('theme');
		const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

		isDark = savedTheme ? savedTheme === 'dark' : prefersDark;
		updateTheme();
	});
</script><svelte:head>
	<meta charset="utf-8" />
	<meta name="viewport" content="width=device-width, initial-scale=1" />
	<meta name="description" content="Laurens van der Tas - Professional CV and Portfolio" />
	<meta property="og:title" content="Laurens van der Tas - CV" />
	<meta property="og:description" content="Professional CV and Portfolio" />
	<meta property="og:type" content="website" />

	<link rel="icon" href={favicon} />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap"
		rel="stylesheet"
	/>

	<title>Laurens van der Tas - CV</title>
</svelte:head>

<div class="bg-primary text-primary transition-theme min-h-screen">
	<!-- Dark Mode Toggle -->
	<button
		class="theme-toggle fixed right-6 top-6 z-50 no-print"
		onclick={toggleTheme}
		aria-label="Toggle dark mode"
		title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
	>
		{#if isDark}
			<Sun size={20} class="theme-icon" />
		{:else}
			<Moon size={20} class="theme-icon" />
		{/if}
	</button>

	{@render children?.()}
</div>
