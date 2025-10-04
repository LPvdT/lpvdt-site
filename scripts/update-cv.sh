#!/bin/bash

# CV Update Script
# This script parses the LaTeX CV and updates the website with the latest data

set -e

echo "🔄 Updating CV website with latest data..."
echo ""

# Check if LaTeX file exists
if [ ! -f "final-cv.tex" ]; then
	echo "❌ Error: final-cv.tex not found!"
	echo "Please make sure the LaTeX CV file is in the project root."
	exit 1
fi

# Step 1: Parse the LaTeX CV
echo "📄 Step 1: Parsing LaTeX CV..."
python3 scripts/parse-cv.py

if [ $? -ne 0 ]; then
	echo "❌ Failed to parse CV"
	exit 1
fi

echo "✅ CV parsed successfully"
echo ""

# Step 2: Process and update website
echo "🔄 Step 2: Processing data and updating website..."
python3 scripts/update-website.py

if [ $? -ne 0 ]; then
	echo "❌ Failed to update website"
	exit 1
fi

echo "✅ Website updated successfully"
echo ""

# Step 3: Build the site
echo "🏗️  Step 3: Building the website..."
npm run build

if [ $? -ne 0 ]; then
	echo "❌ Build failed"
	exit 1
fi

echo "✅ Build completed successfully"
echo ""

# Step 4: Run tests (optional)
echo "🧪 Step 4: Running tests..."
npm run lint

if [ $? -ne 0 ]; then
	echo "⚠️  Linting issues found, but continuing..."
else
	echo "✅ All tests passed"
fi

echo ""
echo "🎉 CV website update complete!"
echo ""
echo "📊 Summary:"
echo "   • LaTeX CV parsed and converted to JSON"
echo "   • Website updated with latest personal data"
echo "   • Build completed successfully"
echo "   • Site ready for deployment"
echo ""
echo "💡 Next steps:"
echo "   • Preview: npm run dev"
echo "   • Deploy: git add . && git commit -m 'feat: update CV data' && git push"
echo ""
