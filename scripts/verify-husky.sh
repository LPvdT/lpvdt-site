#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}🔍 Verifying Husky Setup...${NC}"
echo ""

# Check if .husky directory exists
if [ -d ".husky" ]; then
	echo -e "${GREEN}✅ .husky directory exists${NC}"
else
	echo -e "${RED}❌ .husky directory not found${NC}"
	exit 1
fi

# Check if hooks exist and are executable
hooks=("pre-commit" "commit-msg" "pre-push")

for hook in "${hooks[@]}"; do
	if [ -f ".husky/$hook" ]; then
		if [ -x ".husky/$hook" ]; then
			echo -e "${GREEN}✅ $hook hook exists and is executable${NC}"
		else
			echo -e "${YELLOW}⚠️  $hook hook exists but is not executable${NC}"
			chmod +x ".husky/$hook"
			echo -e "${GREEN}✅ Made $hook executable${NC}"
		fi
	else
		echo -e "${RED}❌ $hook hook not found${NC}"
	fi
done

# Check if husky and lint-staged are installed
echo ""
echo -e "${YELLOW}📦 Checking dependencies...${NC}"

if npm list husky >/dev/null 2>&1; then
	echo -e "${GREEN}✅ husky is installed${NC}"
else
	echo -e "${RED}❌ husky is not installed${NC}"
fi

if npm list lint-staged >/dev/null 2>&1; then
	echo -e "${GREEN}✅ lint-staged is installed${NC}"
else
	echo -e "${RED}❌ lint-staged is not installed${NC}"
fi

# Check package.json scripts
echo ""
echo -e "${YELLOW}📜 Checking package.json scripts...${NC}"

if grep -q "\"pre-commit\":" package.json; then
	echo -e "${GREEN}✅ pre-commit script found${NC}"
else
	echo -e "${RED}❌ pre-commit script not found${NC}"
fi

if grep -q "\"lint-staged\":" package.json; then
	echo -e "${GREEN}✅ lint-staged configuration found${NC}"
else
	echo -e "${RED}❌ lint-staged configuration not found${NC}"
fi

echo ""
echo -e "${GREEN}🎉 Husky setup verification complete!${NC}"
echo ""
echo -e "${YELLOW}📚 Next steps:${NC}"
echo "1. Stage some files: git add ."
echo "2. Try a commit: git commit -m 'feat: test husky setup'"
echo "3. Check that hooks run automatically"
echo ""
echo -e "${YELLOW}💡 Tip:${NC} Use conventional commit format: type(scope): description"
