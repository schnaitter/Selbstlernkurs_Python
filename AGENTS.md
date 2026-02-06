# AGENTS.md

## Project Overview

**Selbstlernkurs Python** - A self-learning Python course for library and
information science students at Humboldt-Universität zu Berlin using MyST
Markdown and Jupyter Book.

## Repository Structure

### Chapters (sequential modules)

- `000-Einleitung/` - Introduction
- `010-Installation_Technik/` - Setup
- `020-Projekt_Taschenrechner_I/` - Calculator I (basics)
- `030-Exkurs_Unix/` - Unix excursion
- `040-Projekt_CSV_I/` - CSV processing
- `050-Exkurs_Git/` - Git excursion
- `060-Projekt_Taschenrechner_II/` - Calculator II (input, loops)
- `070-Projekt_CSV_II/` - Advanced CSV
- `080-Projekt_MARC-XML/` - Library metadata
- `090-Projekt_Excel/` - Excel processing
- `900-Cheatsheet.md` - Quick reference
- `999-Epilog/` - Glossary, imprint

### Other directories

- `solutions/` - Exercise solutions (e.g., `solutions/020/taschenrechner.py`)
- `assets/` - Images, logos
- `_build/` - Generated output (never edit)

## Development

```bash
# Environment (Python 3.14, managed via uv)
source .venv/bin/activate
uv pip sync requirements.txt

# Build
jupyter book build --execute --all

# Edit notebooks
jupyter lab
```

**Dependencies**: `jupyter-book==2.1.2`, `jupyterlab`, `ipywidgets`,
`jupyterquiz`

## Content Guidelines

### Files

- `.ipynb` - Jupyter notebooks with executable code
- `.md` - MyST Markdown documentation
- Config: `myst.yml` (project), `toc.yml` (navigation)

### Adding content

1. Create files in numbered directory
2. Update `toc.yml`
3. Use frontmatter:
   ```yaml
   ---
   short_title: Title
   numbering:
     heading_1: true
     heading_2: true
   ---
   ```
4. Start chapters with learning objectives (🎓 Lernziele)

### Language

- German content with gender-neutral asterisks: "Lernende\*r"
- German terms with English: "Versionskontrolle (Version Control)"

### Solution scripts

```python
#! /usr/bin/env python3
# Make executable: chmod +x script.py
# Follow PEP 8
```
