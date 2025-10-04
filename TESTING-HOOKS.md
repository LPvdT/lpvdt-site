# Testing Husky Setup

This is a test file to verify that our Husky hooks are working correctly.

## Test Steps

1. **Format test**: Intentionally add malformed code
2. **Lint test**: Check that ESLint catches issues
3. **Type test**: Verify TypeScript checking
4. **Commit message test**: Try invalid commit format

Run these tests:

```bash
# 1. Add poorly formatted code and see if pre-commit fixes it
echo "const   badFormat    =    'test'   ;" > test-format.js
git add test-format.js
git commit -m "test: format check"

# 2. Try invalid commit message (should fail)
git commit -m "bad commit message format"

# 3. Try valid commit message (should pass)
git commit -m "test: verify husky hooks working"
```

The hooks should:

- ✅ Auto-format code during pre-commit
- ✅ Reject invalid commit messages
- ✅ Accept valid conventional commit messages
- ✅ Run type checking and tests
