# 🪝 Git Hooks with Husky

This project uses [Husky](https://typicode.github.io/husky/) to enforce code quality and consistency through git hooks.

## 🛠️ Configured Hooks

### Pre-commit Hook

Runs before each commit to ensure code quality:

- **Lint-staged**: Automatically formats and lints only staged files
- **Type checking**: Validates TypeScript types in Svelte components
- **Tests**: Runs unit tests to ensure functionality

**What it checks:**

- ESLint rules for JavaScript/TypeScript/Svelte files
- Prettier formatting for all supported files
- TypeScript type checking
- Unit test suite

### Commit Message Hook

Validates commit message format to maintain consistent git history:

**Required format:** `type(scope): description`

**Allowed types:**

- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation updates
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes
- `build`: Build system changes

**Examples:**

```
feat: add navigation component
fix(ui): resolve button styling issue
docs: update deployment guide
style: format code with prettier
refactor(components): simplify section layout
test: add unit tests for skills component
```

### Pre-push Hook

Runs before pushing to remote repository:

- **Build verification**: Ensures the project builds successfully
- **Final quality check**: Prevents broken code from being pushed

## 🎯 Lint-staged Configuration

The following file types are automatically processed:

**JavaScript/TypeScript/Svelte files:**

- ESLint with auto-fix
- Prettier formatting
- TypeScript type checking (for .svelte files)

**Other files (JSON, Markdown, CSS, HTML):**

- Prettier formatting

## 🚀 Manual Commands

You can run these commands manually:

```bash
# Format all files
npm run format

# Check formatting
npm run format:check

# Lint code
npm run lint

# Lint with auto-fix
npm run lint:fix

# Type check
npm run type-check

# Run tests
npm run test

# Run lint-staged manually
npm run pre-commit
```

## 🔧 Customization

### Modifying Hooks

Edit files in `.husky/` directory:

- `.husky/pre-commit` - Pre-commit checks
- `.husky/commit-msg` - Commit message validation
- `.husky/pre-push` - Pre-push verification

### Updating Lint-staged

Modify the `lint-staged` configuration in `package.json`:

```json
{
	"lint-staged": {
		"*.{js,ts,svelte}": ["eslint --fix", "prettier --write"],
		"*.{json,md,css,html}": ["prettier --write"]
	}
}
```

### Skipping Hooks (Emergency)

In rare cases, you can skip hooks:

```bash
# Skip pre-commit hook
git commit --no-verify -m "emergency fix"

# Skip pre-push hook
git push --no-verify
```

**⚠️ Warning:** Only use `--no-verify` in emergencies as it bypasses all quality checks.

## 🎯 Benefits

- **Consistent code style** across the entire project
- **Early bug detection** before code reaches the repository
- **Standardized commit messages** for better git history
- **Automated quality checks** reduce manual review time
- **Prevention of broken builds** being pushed to main branch

## 🐛 Troubleshooting

**Hook not running?**

- Ensure Husky is installed: `npm run prepare`
- Check file permissions: `chmod +x .husky/*`

**Lint-staged failing?**

- Run commands manually to debug: `npm run lint:fix`
- Check file staging: `git status`

**Commit message rejected?**

- Follow the required format: `type(scope): description`
- Keep description under 50 characters
- Use lowercase for type and scope

---

**Happy coding with quality assurance! 🎉**
