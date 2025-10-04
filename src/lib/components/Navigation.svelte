<script lang="ts">
	import { Menu, X } from 'lucide-svelte';

	let isMenuOpen = $state(false);

	const menuItems = [
		{ label: 'About', href: '#about' },
		{ label: 'Skills', href: '#skills' },
		{ label: 'Experience', href: '#experience' },
		{ label: 'Projects', href: '#projects' },
		{ label: 'Education', href: '#education' }
	];

	function scrollToSection(href: string) {
		const element = document.querySelector(href);
		if (element) {
			element.scrollIntoView({ behavior: 'smooth' });
			isMenuOpen = false;
		}
	}
</script>

<nav
	class="bg-opacity-90 no-print fixed top-0 right-0 left-0 z-50 border-b border-gray-200 bg-white backdrop-blur-sm"
>
	<div class="mx-auto max-w-4xl px-6">
		<div class="flex h-16 items-center justify-between">
			<div class="gradient-text text-xl font-bold">LvdT</div>

			<!-- Desktop Menu -->
			<div class="hidden space-x-8 md:flex">
				{#each menuItems as item}
					<button
						onclick={() => scrollToSection(item.href)}
						class="font-medium text-gray-600 transition-colors hover:text-gray-900"
					>
						{item.label}
					</button>
				{/each}
			</div>

			<!-- Mobile Menu Button -->
			<button
				onclick={() => (isMenuOpen = !isMenuOpen)}
				class="rounded-md p-2 text-gray-600 hover:bg-gray-100 hover:text-gray-900 md:hidden"
			>
				{#if isMenuOpen}
					<X size={24} />
				{:else}
					<Menu size={24} />
				{/if}
			</button>
		</div>

		<!-- Mobile Menu -->
		{#if isMenuOpen}
			<div class="border-t border-gray-200 bg-white py-4 md:hidden">
				<div class="space-y-2">
					{#each menuItems as item}
						<button
							onclick={() => scrollToSection(item.href)}
							class="block w-full px-4 py-2 text-left font-medium text-gray-600 transition-colors hover:bg-gray-50 hover:text-gray-900"
						>
							{item.label}
						</button>
					{/each}
				</div>
			</div>
		{/if}
	</div>
</nav>

<!-- Spacer to prevent content from hiding behind fixed nav -->
<div class="no-print h-16"></div>
