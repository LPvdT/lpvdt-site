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

  const levelClasses = {
    beginner: 'skill-beginner',
    intermediate: 'skill-intermediate',
    advanced: 'skill-advanced',
    expert: 'skill-expert'
  };
</script>

<span
  class="animate-fade-in inline-block cursor-default rounded-full border px-3 py-1.5 text-sm font-medium opacity-0 transition-all duration-300 hover:scale-105 hover:shadow-lg {levelClasses[
    level
  ]}"
  style="animation-delay: {delay}ms"
>
  {skill}
</span>
