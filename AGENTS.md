# AGENTS.md

This file provides guidance to coding agents when working with
code in this repository.

## Project Overview

**Selbstlernkurs Python** - A self-learning Python course for library and
information science students at Humboldt-Universität zu Berlin. The course uses
MyST Markdown and Jupyter Book to create an interactive learning environment.

**Target Audience**: Master's students in Library and Information Science
(distance learning program)

**Course Structure**: Project-based learning with library/information science
use cases (CSV processing, MARC-XML metadata, Excel statistics)

## Repository Architecture

### Chapter Organization

Numbered directories represent sequential course modules:

- `000-Einleitung/` - Introduction and course usage
- `010-Installation_Technik/` - Python installation and setup
- `020-Projekt_Taschenrechner_I/` - Calculator project I (basic concepts)
- `030-Exkurs_Unix/` - Unix command line excursion
- `040-Projekt_CSV_I/` - CSV file processing
- `045-Projekt_Taschenrechner_II/` - Calculator project II (input, loops)
- `050-Exkurs_Git/` - Git version control excursion
- `060-Projekt_CSV_II/` - Advanced CSV processing
- `070-Projekt_MARC-XML/` - Library metadata processing
- `080-Projekt_Excel/` - Excel file processing
- `900-Cheatsheet.md` - Quick reference
- `999-Epilog/` - Glossary, index, literature, imprint

### Key Directories

- `solutions/` - Solution scripts for exercises (e.g.,
  `solutions/020/taschenrechner.py`)
- `_build/` - Generated build output (do not edit manually)
- `.venv/` - Python virtual environment (Python 3.13+)
- `assets/` - Images, logos, and static files

### Content Format

Each chapter contains:

- `.ipynb` files - Interactive Jupyter notebooks with executable code
- `.md` files - MyST Markdown documentation
- Learning objectives (🎓 Lernziele) at the start
- Exercises that qualify as "Kleine Aufgabe" course assignments

Content is in German using gender-neutral language with asterisks (e.g.,
"Lernende\*r")

## Common Development Commands

### Environment Setup

```bash
# Activate virtual environment (automatic with direnv via .envrc)
source .venv/bin/activate

# Install/update dependencies
pip install -r requirements.txt
```

**Dependencies** (Python 3.13+):

- `jupyter-book==2.0.0b3` ⚠️ Beta version - may have unstable APIs
- `jupyterlab`, `ipywidgets`, `jupyterquiz`, `numpy`

### Building and Testing

```bash
# Build the complete MyST book (outputs to _build/)
jupyter book build --execute --all

# Start JupyterLab for editing notebooks
jupyter lab
# or: .venv/bin/jupyter lab

# Run solution scripts
./solutions/020/taschenrechner.py
# or: python3 solutions/020/taschenrechner.py
```

## Key Technical Details

### MyST Book Configuration (`myst.yml`)

- **Project ID**: `009c9d71-a4fc-4438-8118-31289551ac9b`
- **Template**: `book-theme` with custom logo/favicon in `assets/`
- **Table of Contents**: Defined in `toc.yml` with hierarchical chapter
  structure
- **Jupyter Integration**:
    - Jupyter Lite enabled (browser-based Python execution)
    - Binder integration (cloud-based interactive notebooks via mybinder.org)
- **License**: CC-BY-4.0 (content) / MIT (code)
- **Bibliography**: `bibliography.bib` for citations

### Adding New Content

When adding chapters or sections:

1. Create files in the appropriate numbered directory (e.g.,
   `040-Projekt_CSV_I/`)
2. Update `toc.yml` to include the new file in the navigation hierarchy
3. Follow MyST frontmatter conventions for metadata:
    ```yaml
    ---
    short_title: Title
    numbering:
        heading_1: true
        heading_2: true
        title: true
    ---
    ```
4. Use margin notes for hints: `:::::{margin} ... :::::`
5. Include learning objectives (🎓 Lernziele) at the start of chapters

### Jupyter Notebooks

- Use MyST markdown cells (not plain markdown) for rich formatting
- Include interactive Python examples with expected outputs
- Use `jupyterquiz` for in-notebook quizzes and exercises
- Notebooks support Mermaid diagrams for visualizations
- Comment syntax: `# Comment text` (everything after `#` is ignored)

### Python Solution Scripts

Pattern for solution files (see `solutions/020/taschenrechner.py`):

- Include shebang: `#! /usr/bin/env python3`
- Make executable: `chmod +x script.py`
- Follow PEP 8 style guidelines
- Use `if __name__ == "__main__":` for executable logic

### Language and Style

**German content with specific conventions**:

- Gender-neutral asterisks: "Lernende\*r", "Bibliothekswissenschaftler\*innen"
- German terms with English in parentheses: "Versionskontrolle (Version
  Control)"
- File/folder names may include umlauts: `Dateien_öffnen.ipynb`
- Decimal numbers: German text style in prose, Python dot notation in code

### Pedagogical Structure

**Project-based, incremental learning**:

- **Iterative complexity**: Projects revisited with added features (e.g.,
  `Taschenrechner` I & II)
- **Domain-specific context**: All examples use library/information science
  data
- **Self-paced design**: Students can skip ahead or follow linear progression
- **Mixed formats**: Notebooks (hands-on), Markdown (theory), Excursions
  (context)

## Development Notes

- **Never edit `_build/`** - regenerated on each build
- **Ignore `.ipynb_checkpoints/`** - Jupyter autosave artifacts
- **Beta warning**: `jupyter-book==2.0.0b3` may have breaking changes in
  updates
- **Binder deployment**: Changes to main branch automatically available in
  cloud environment
