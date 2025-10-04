# 🚀 Quick Deployment Guide

## GitHub Pages Setup

### Step 1: Repository Setup

1. Push this code to your GitHub repository
2. Make sure your repository is public (required for free GitHub Pages)

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. Save the settings

### Step 3: Deploy

The GitHub Action will automatically deploy when you push to the `main` branch!

Your site will be available at: `https://yourusername.github.io/repository-name`

## Customization Checklist

- [ ] Update personal information in `src/routes/+page.svelte`
- [ ] Replace `static/Laurens-van-der-Tas-CV.pdf` with your CV
- [ ] Customize skills and experience sections
- [ ] Update colors/theme if desired
- [ ] Test on mobile devices
- [ ] Update README with your information

## Custom Domain (Optional)

1. Add a `CNAME` file to the `static/` folder with your domain
2. Configure your domain's DNS to point to GitHub Pages
3. Enable "Enforce HTTPS" in GitHub Pages settings

## Performance Tips

✅ The site is already optimized with:

- Static site generation
- Optimized images and fonts
- Minimal JavaScript
- Fast loading animations
- Mobile-first responsive design

## Troubleshooting

**Build fails?** Check the Actions tab in your GitHub repository for error details.

**Styles not loading?** Ensure the base path is correctly configured in `svelte.config.js`.

**PDF not accessible?** Make sure the PDF file is in the `static/` folder.

## Support

Need help? Check the README.md for detailed instructions or create an issue in the repository.

---

Happy deploying! 🎉
