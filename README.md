# BATTLESPACE - Game Design Document Site

Professional GitHub Pages documentation site for the BATTLESPACE tactical FPS game design document.

## 🚀 Quick Deploy to GitHub Pages

### Method 1: Automated (Recommended)

1. **Create GitHub Repository**
```bash
git init
git add .
git commit -m "Initial GDD site"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/battlespace-gdd.git
git push -u origin main
```

2. **Enable GitHub Pages**
- Go to repository Settings → Pages
- Source: Deploy from a branch
- Branch: `main` / `root`
- Save

Your site will be live at: `https://YOUR_USERNAME.github.io/battlespace-gdd/`

### Method 2: GitHub Actions (Advanced)

Use the included `.github/workflows/jekyll.yml` for automatic builds.

1. Push code to GitHub
2. Go to Settings → Pages → Source: GitHub Actions
3. Commit triggers automatic deployment

## 🧪 Local Testing

### Prerequisites
```bash
# Install Ruby (2.7+)
# Install Bundler
gem install bundler
```

### Run Locally
```bash
bundle install
bundle exec jekyll serve
```

Visit: `http://localhost:4000`

## 📁 Structure

```
battlespace-gdd-site/
├── _config.yml              # Jekyll configuration
├── index.md                 # Home page with navigation
├── docs/                    # All documentation
│   ├── gameplay/           # Gameplay systems
│   ├── combat/             # Combat mechanics
│   ├── roles/              # Character roles
│   ├── vehicles/           # Vehicles & aircraft
│   ├── equipment/          # Weapons & gear
│   ├── levels/             # Maps & locations
│   │   ├── ukraine/
│   │   ├── barents-sea/
│   │   └── south-china-sea/
│   ├── art/                # Art direction
│   ├── audio/              # Sound design
│   ├── ui/                 # UI/UX
│   ├── technical/          # Technical specs
│   ├── narrative/          # Story & lore
│   ├── characters/         # Character bios
│   ├── dev/                # Development docs
│   └── warfare/            # Warfare levels
└── organize_files.py       # File organization script
```

## 🎨 Customization

### Change Theme

Edit `_config.yml`:
```yaml
theme: jekyll-theme-cayman  # or slate, minimal, etc.
```

Available themes:
- `jekyll-theme-cayman` (default)
- `jekyll-theme-slate`
- `jekyll-theme-minimal`
- `jekyll-theme-architect`

### Modify Navigation

Edit `_config.yml` → `navigation` section

### Add Content

1. Create `.md` files in appropriate `docs/` subdirectory
2. Update `index.md` with new links
3. Commit and push

## 🔧 Troubleshooting

### Images Not Loading
Check that image paths in markdown use:
```markdown
![Alt text](../path/to/image.png)
```

### 404 Errors
Ensure all links in `index.md` match actual file paths in `docs/`

### Build Failures
Check GitHub Actions tab for error logs

## 📝 Maintenance

### Update Content
```bash
# Edit markdown files
git add .
git commit -m "Update documentation"
git push
```

### Reorganize Structure
Run the organization script:
```bash
python3 organize_files.py
```

## 🔐 Access Control

For private documentation:
1. Set repository to Private
2. Add collaborators in Settings → Collaborators
3. GitHub Pages will only be accessible to repository members

## 📊 Analytics (Optional)

Add Google Analytics to `_config.yml`:
```yaml
google_analytics: UA-XXXXXXXXX-X
```

## 🛠️ Tech Stack

- **Jekyll** - Static site generator
- **GitHub Pages** - Hosting
- **Kramdown** - Markdown processor
- **Rouge** - Syntax highlighting

## 📄 License

[Add your license here]

## 🤝 Contributing

Internal development team only. Contact project lead for access.

---

**Built for:** BATTLESPACE FPS Development Team  
**Engine:** Unreal Engine 5.3  
**Last Updated:** November 2025
