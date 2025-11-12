#!/bin/bash

# BATTLESPACE GDD - Quick GitHub Pages Deployment Script
# Usage: ./deploy.sh

set -e

echo "🚀 BATTLESPACE GDD Deployment"
echo "=============================="

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git repository..."
    git init
    git branch -M main
fi

# Check for uncommitted changes
if [ -n "$(git status --porcelain)" ]; then
    echo "📝 Staging files..."
    git add .
    
    echo "💾 Committing changes..."
    read -p "Enter commit message (or press Enter for default): " commit_msg
    if [ -z "$commit_msg" ]; then
        commit_msg="Update GDD documentation"
    fi
    git commit -m "$commit_msg"
else
    echo "✓ No changes to commit"
fi

# Check for remote
if ! git remote | grep -q origin; then
    echo ""
    echo "🔗 Setting up GitHub remote..."
    read -p "Enter your GitHub repository URL: " repo_url
    git remote add origin "$repo_url"
fi

# Push to GitHub
echo ""
echo "⬆️  Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📋 Next steps:"
echo "1. Go to GitHub repository Settings → Pages"
echo "2. Set Source to 'Deploy from a branch' or 'GitHub Actions'"
echo "3. Select branch 'main' and folder '/ (root)'"
echo "4. Your site will be live at: https://YOUR_USERNAME.github.io/REPO_NAME/"
echo ""
