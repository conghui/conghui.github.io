# AGENTS.md - Development Guide for Agents

This is a **Jekyll-based academic personal website** with a Python crawler for Google Scholar statistics.

## Table of Contents
1. [Build Commands](#build-commands)
2. [Testing](#testing)
3. [Code Style Guidelines](#code-style-guidelines)
4. [Project Structure](#project-structure)

---

## Build Commands

### Jekyll (Main Site)

```bash
# Install dependencies
bundle install

# Build the site (outputs to _site/)
bundle exec jekyll build

# Serve locally with live reload (default: http://localhost:4000)
bundle exec jekyll liveserve

# Serve without live reload
bundle exec jekyll serve

# Clean build artifacts
bundle exec jekyll clean
```

### Python Crawler

```bash
# Install Python dependencies
cd google_scholar_crawler
pip install -r requirements.txt

# Run the crawler (requires GOOGLE_SCHOLAR_ID env var)
cd google_scholar_crawler
python main.py
```

### GitHub Actions

The project includes a workflow (`.github/workflows/google_scholar_crawler.yaml`) that:
- Runs daily at 8:00 UTC
- Runs on page build events
- Updates citation data in the `google-scholar-stats` branch

---

## Testing

### Jekyll
There are no formal tests for the Jekyll site. Manual testing via `bundle exec jekyll serve` is recommended.

### Python Crawler

```bash
# Run the crawler script
cd google_scholar_crawler
python -c "from main import *; print('Import OK')"

# Run with verbose output
python -c "
import os
os.environ['GOOGLE_SCHOLAR_ID'] = 'test_id'  # Use a valid ID for actual testing
exec(open('main.py').read())
"
```

---

## Code Style Guidelines

### General Principles
- Keep changes minimal and focused
- Test locally before committing
- Do not modify `_config.yml` unless explicitly required
- Avoid adding new dependencies without discussion

### Jekyll/Liquid Templates

**File Extensions**: `.html`, `.md`, `.yml`

**Formatting**:
- Use 2 spaces for indentation in YAML
- Use consistent Liquid tag spacing: `{{ content }}` (with spaces inside braces)
- Keep HTML/Liquid templates readable with proper line breaks

**Naming**:
- Variables: lowercase with underscores, e.g., `author_name`
- Files: lowercase with hyphens, e.g., `my-page.html`

**Best Practices**:
- Use `_includes/` for reusable components
- Use `_layouts/` for page templates
- Keep logic in includes minimal; prefer data-driven content

### Python (google_scholar_crawler)

**Imports** (in order):
1. Standard library
2. Third-party packages
3. Local imports

**Formatting**: Follow PEP 8 (enforced by linters)

**Naming**:
- Functions: `snake_case`, e.g., `fetch_author_data()`
- Constants: `UPPER_SNAKE_CASE`
- Classes: `PascalCase`

**Error Handling**:
- Use try/except for network operations
- Log errors appropriately
- Fail gracefully (don't crash the CI workflow)

**Example**:
```python
import os
import json
from datetime import datetime

from scholarly import scholarly

def fetch_author(author_id: str) -> dict:
    """Fetch author data from Google Scholar."""
    try:
        author = scholarly.search_author_id(author_id)
        scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
        return author
    except Exception as e:
        print(f"Error fetching author: {e}")
        return {}
```

### GitHub Actions Workflows

- Place workflows in `.github/workflows/`
- Use stable action versions (e.g., `@v2`, `@v3` not `@master`)
- Store secrets in GitHub Secrets, never in code
- Ensure workflows can run independently

---

## Project Structure

```
.
├── _config.yml          # Jekyll configuration
├── _pages/              # Page content (Markdown)
├── _includes/           # Reusable HTML components
├── _layouts/            # Page layouts
├── _sass/               # Sass stylesheets
├── assets/              # CSS, JS, fonts, images
├── google_scholar_crawler/  # Python crawler
│   ├── main.py
│   └── requirements.txt
├── .github/workflows/   # CI/CD workflows
└── docs/                # Documentation (excluded from build)
```

### Key Configuration

- **Repository**: `conghui/conghui.github.io`
- **Site URL**: Configured in `_config.yml`
- **Google Scholar**: Uses CDN for stats display

---

## Common Tasks

### Adding a New Page
1. Create `.md` file in `_pages/`
2. Add front matter:
```yaml
---
title: "Page Title"
layout: default
permalink: /custom-path/
---
```

### Modifying Styles
- Edit files in `_sass/` (Sass source)
- Or add custom CSS in `assets/css/`

### Updating the Crawler
1. Edit `google_scholar_crawler/main.py`
2. Test locally with valid `GOOGLE_SCHOLAR_ID`
3. Ensure output JSON matches expected schema

---

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_SCHOLAR_ID` | Google Scholar author ID | For crawler |
| `GOOGLE_SCHOLAR_STATS_USE_CDN` | Use CDN for stats | Site config |

---

## Useful Commands Reference

```bash
# Full local build and serve
bundle install && bundle exec jekyll liveserve

# Check for Jekyll plugin compatibility
bundle exec jekyll doctor

# Validate workflow files
# (Use GitHub CLI or online validators)
```
