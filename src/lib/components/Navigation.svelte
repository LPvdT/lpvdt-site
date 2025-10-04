<script lang="ts">
  import { Sun, Moon } from 'lucide-svelte';
  import { onMount } from 'svelte';

  let {
    isDark = $bindable(),
    toggleTheme
  }: { isDark: boolean; toggleTheme: () => void } = $props();

  let isMenuOpen = $state(false);
  let navElement: HTMLElement;

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

  function handleClickOutside(event: MouseEvent) {
    if (navElement && !navElement.contains(event.target as Node)) {
      isMenuOpen = false;
    }
  }

  function handleKeydown(event: KeyboardEvent) {
    if (event.key === 'Escape') {
      isMenuOpen = false;
    }
  }

  onMount(() => {
    document.addEventListener('click', handleClickOutside);
    document.addEventListener('keydown', handleKeydown);
    return () => {
      document.removeEventListener('click', handleClickOutside);
      document.removeEventListener('keydown', handleKeydown);
    };
  });
</script>

<nav
  bind:this={navElement}
  class="navbar-bg no-print border-primary transition-theme fixed top-0 right-0 left-0 z-50 border-b backdrop-blur-sm"
>
  <div class="mx-auto max-w-4xl px-6">
    <div class="flex h-16 items-center justify-between">
      <div class="gradient-text text-xl font-bold">LvdT</div>

      <div class="flex items-center space-x-4">
        <!-- Desktop Menu -->
        <div class="hidden space-x-8 md:flex">
          {#each menuItems as item}
            <button
              onclick={() => scrollToSection(item.href)}
              class="text-secondary hover:text-primary font-medium transition-all duration-300 hover:scale-105"
            >
              {item.label}
            </button>
          {/each}
        </div>

        <!-- Theme Toggle -->
        <button
          class="theme-toggle"
          onclick={toggleTheme}
          aria-label="Toggle dark mode"
          title={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
        >
          {#if isDark}
            <Sun size={18} class="theme-icon" />
          {:else}
            <Moon size={18} class="theme-icon" />
          {/if}
        </button>

        <!-- Mobile Menu Button -->
        <button
          onclick={() => (isMenuOpen = !isMenuOpen)}
          class="hamburger-menu text-secondary hover:bg-tertiary hover:text-primary relative rounded-md p-2 transition-all duration-300 md:hidden"
          aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
        >
          <div
            class="hamburger-lines relative flex h-6 w-6 flex-col items-center justify-center"
          >
            <span
              class="hamburger-line block h-0.5 w-5 bg-current transition-all duration-300 {isMenuOpen
                ? 'translate-y-0 rotate-45'
                : '-translate-y-1.5'}"
            ></span>
            <span
              class="hamburger-line block h-0.5 w-5 bg-current transition-all duration-300 {isMenuOpen
                ? 'opacity-0'
                : 'opacity-100'}"
            ></span>
            <span
              class="hamburger-line block h-0.5 w-5 bg-current transition-all duration-300 {isMenuOpen
                ? '-translate-y-2 -rotate-45'
                : 'translate-y-1.5'}"
            ></span>
          </div>
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    {#if isMenuOpen}
      <div
        class="mobile-menu border-primary bg-secondary transition-theme animate-slide-in-up border-t py-4 md:hidden"
      >
        <div class="space-y-2">
          {#each menuItems as item, index}
            <button
              onclick={() => scrollToSection(item.href)}
              class="text-secondary hover:bg-tertiary hover:text-primary animate-fade-in block w-full px-4 py-2 text-left font-medium opacity-0 transition-all duration-300 animate-delay-{(index +
                1) *
                100}"
            >
              {item.label}
            </button>
          {/each}
        </div>
      </div>
    {/if}
  </div>
</nav>

<!-- Mobile menu backdrop -->
{#if isMenuOpen}
  <div
    class="animate-fade-in fixed inset-0 z-40 bg-black/20 backdrop-blur-sm md:hidden"
    onclick={() => (isMenuOpen = false)}
    onkeydown={(e) => e.key === 'Enter' && (isMenuOpen = false)}
    role="button"
    tabindex="0"
    aria-label="Close menu"
  ></div>
{/if}

<!-- Spacer to prevent content from hiding behind fixed nav -->
<div class="no-print h-16"></div>
