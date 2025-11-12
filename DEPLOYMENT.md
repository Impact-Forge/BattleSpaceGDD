# 🚀 Quick Deployment Guide

## Option 1: One-Command Deploy (Fastest)

```bash
./deploy.sh
```

Follow the prompts to push to GitHub.

---

## Option 2: Manual Deployment

### Step 1: Initialize Git
```bash
git init
git add .
git commit -m "Initial GDD site"
git branch -M main
```

### Step 2: Connect to GitHub
```bash
# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/battlespace-gdd.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to: `https://github.com/YOUR_USERNAME/battlespace-gdd/settings/pages`
2. **Source:** Deploy from a branch
3. **Branch:** `main`
4. **Folder:** `/ (root)`
5. Click **Save**

### Step 4: Access Your Site
Wait 2-3 minutes, then visit:
```
https://YOUR_USERNAME.github.io/battlespace-gdd/
```

---

## Option 3: GitHub Actions (Auto-Deploy)

### Enable Actions
1. Push code to GitHub (Steps 1-2 above)
2. Go to Settings → Pages
3. **Source:** GitHub Actions
4. Every push triggers automatic deployment

---

## 🧪 Test Locally First

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Open: http://localhost:4000
```

---

## 🔧 Common Issues

### "Page build failed"
- Check `.github/workflows/jekyll.yml` syntax
- Verify all markdown files have valid front matter
- Review build logs in Actions tab

### Images not loading
```markdown
# Use relative paths:
![Image](../assets/image.png)

# Not absolute:
![Image](/assets/image.png)
```

### 404 on navigation links
- Verify file paths match `index.md` links
- Check file extensions (.md not .markdown)

---

## 📊 Site Statistics

- **Total Pages:** 80+
- **Categories:** 14
- **Build Time:** ~10-15 seconds
- **Deploy Time:** 2-3 minutes

---

## 🔄 Update Workflow

```bash
# Make changes to markdown files
# Then:
git add .
git commit -m "Update [section]"
git push

# Site auto-updates in 2-3 minutes
```

---

## 🎨 Customize Theme

Edit `_config.yml`:
```yaml
theme: jekyll-theme-cayman  # Change this line
```

Available themes:
- `jekyll-theme-slate` (dark)
- `jekyll-theme-minimal` (clean)
- `jekyll-theme-architect` (bold)
- `jekyll-theme-tactile` (modern)

---

## 📱 Mobile Responsive

All themes are mobile-responsive by default. Test at:
- Desktop: Chrome DevTools (F12 → Toggle Device)
- Real device: Use GitHub Pages URL

---

## 🔐 Private Repository

To keep GDD private:
1. Set repo to **Private** in Settings
2. GitHub Pages still works for collaborators
3. Only team members with repo access can view

---

## ✅ Deployment Checklist

- [ ] Repository created on GitHub
- [ ] Code pushed to `main` branch
- [ ] GitHub Pages enabled in Settings
- [ ] Site accessible at GitHub Pages URL
- [ ] All links working (test navigation)
- [ ] Images loading correctly
- [ ] Mobile view looks good

---

**Need Help?** Check the [full README](README.md) or Jekyll docs at [jekyllrb.com](https://jekyllrb.com)
