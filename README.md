# 🌟 Professional CV Website

A beautiful, modern, and responsive CV website built with SvelteKit, Tailwind CSS, and deployed on GitHub Pages.

## ✨ Features

- **Modern Design**: Clean, professional layout with beautiful typography
- **Smooth Animations**: Engaging entrance animations and hover effects
- **Responsive**: Perfect on desktop, tablet, and mobile devices
- **Fast Loading**: Optimized for performance with static site generation
- **SEO Friendly**: Proper meta tags and semantic HTML
- **Print Friendly**: Optimized styles for printing
- **Easy to Customize**: Well-structured code and clear data separation

## 🚀 Live Demo

Visit the live site: [Your GitHub Pages URL]

## 🛠️ Built With

- [SvelteKit](https://kit.svelte.dev/) - The web framework
- [Tailwind CSS](https://tailwindcss.com/) - For styling
- [Lucide Svelte](https://lucide.dev/) - Beautiful icons
- [Inter Font](https://fonts.google.com/specimen/Inter) - Modern typography
- [GitHub Pages](https://pages.github.com/) - For hosting

## 📁 Project Structure

```text
src/
├── lib/
│   └── components/
│       ├── Navigation.svelte      # Top navigation bar
│       ├── Section.svelte         # Reusable section wrapper
│       ├── SkillTag.svelte        # Skill badges
│       └── ExperienceCard.svelte  # Work experience cards
├── routes/
│   ├── +layout.svelte            # Main layout with fonts and meta
│   └── +page.svelte              # CV content and data
├── app.css                       # Global styles and animations
└── app.html                      # HTML template
```

## 🔄 Updating CV Content

This project includes automation scripts to keep your CV content up-to-date:

### Update from LaTeX CV

If you have a LaTeX CV source file:

1. Place your LaTeX CV as `final-cv.tex` in the project root
2. Run the update script:

   ```bash
   npm run update-cv
   ```

This will:

- Parse your LaTeX CV into structured JSON
- Clean and process the data
- Update the website components with new content
- Build the site automatically

### Manual Updates

You can also manually edit the data in `src/routes/+page.svelte`:

## 🎨 Customization

### 1. Personal Information

Edit the `personalInfo` object in `src/routes/+page.svelte`:

```javascript
const personalInfo = {
 name: 'Your Name',
 title: 'Your Professional Title',
 email: 'your.email@example.com',
 phone: '+1 234 567 8900',
 location: 'Your City, Country',
 linkedin: 'https://linkedin.com/in/yourprofile',
 github: 'https://github.com/yourusername',
 website: 'https://yourwebsite.com'
};
```

### 2. Skills

Update the `skills` object with your technologies and proficiency levels:

```javascript
const skills = {
 programming: [
  { name: 'Your Skill', level: 'expert' } // levels: beginner, intermediate, advanced, expert
  // Add more skills...
 ]
 // Update other categories...
};
```

### 3. Work Experience

Modify the `experiences` array:

```javascript
const experiences = [
 {
  title: 'Your Job Title',
  company: 'Company Name',
  period: 'Start Date - End Date',
  description: 'Your role description and achievements...',
  technologies: ['Tech1', 'Tech2', 'Tech3']
 }
 // Add more experiences...
];
```

### 4. Colors and Styling

The site uses a blue/purple gradient theme. To change colors, update the CSS variables in `src/app.css` or modify the Tailwind classes.

### 5. CV PDF

Replace `static/Laurens-van-der-Tas-CV.pdf` with your own CV PDF file.

## 🪝 Code Quality & Git Hooks

This project uses [Husky](https://typicode.github.io/husky/) to enforce code quality through automated git hooks:

**Pre-commit Hook:**

- Runs ESLint and Prettier on staged files
- Validates TypeScript types
- Runs unit tests

**Commit Message Validation:**

- Enforces conventional commit format: `type(scope): description`
- Examples: `feat: add feature`, `fix(ui): resolve bug`, `docs: update readme`

**Pre-push Hook:**

- Ensures project builds successfully before pushing

```bash
# Verify Husky setup
npm run verify-setup

# Manual quality checks
npm run lint          # Check for linting issues
npm run format        # Format all files
npm run type-check    # Validate TypeScript types
```

See [HOOKS.md](./HOOKS.md) for detailed git hooks documentation.

## 🚀 Deployment to GitHub Pages

### Automatic Deployment (Recommended)

1. **Fork or clone this repository**
2. **Enable GitHub Pages**:
   - Go to repository Settings → Pages
   - Source: "GitHub Actions"
3. **Push to main branch** - deployment happens automatically!

### Manual Deployment

```bash
# Build the site
pnpm run build

# Deploy to GitHub Pages
pnpm run deploy
```

## 💻 Local Development

```bash
# Install dependencies
pnpm install

# Start development server
pnpm run dev

# Build for production
pnpm run build

# Preview production build
pnpm run preview
```

## 📱 Mobile Optimization

- Responsive design that works on all screen sizes
- Touch-friendly navigation
- Optimized typography for mobile reading
- Fast loading on mobile networks

## 🎯 Performance Features

- Static site generation for fast loading
- Optimized images and fonts
- Minimal JavaScript bundle
- Excellent Lighthouse scores

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Design inspired by modern portfolio websites
- Icons by [Lucide](https://lucide.dev/)
- Typography by [Google Fonts](https://fonts.google.com/)

---

Made with ❤️ and SvelteKit

Ready to showcase your professional journey? Customize this template and make it your own!
