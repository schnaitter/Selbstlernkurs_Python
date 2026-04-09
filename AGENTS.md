# AGENTS.md

## Project

Selbstlernkurs Python (MyST Markdown / Jupyter Book for HU Berlin LIS students "im Fernstudium").

## Structure

- `000-Einleitung/` to `999-Epilog/`: Sequential modules.
- `solutions/`: Exercise solutions.
- `assets/`: Images/logos.
- `_build/`: Output (DO NOT EDIT).

## Dev

- **Env**: Python 3.14 (via `uv`). `uv sync`.
- **Build**: `uv run jupyter book build --execute --all`
- **Edit**: `uv run jupyter lab`
- **Deps**: `jupyter-book>=2.0.0`, `jupyterlab`, `ipywidgets`, `jupyterquiz`

## Guidelines

- **Files**: `.ipynb` (code), `.md` (docs). Config: `myst.yml`, `toc.yml`.
- **Adding content**: 1. Create numbered dir $\rightarrow$ 2. Update `toc.yml` $\rightarrow$ 3. Use YAML frontmatter (short_title, numbering) $\rightarrow$ 4. Start with "🎓 Lernziele".
- **Language**: German + gender-neutral asterisks ("Lernende\*r"). English terms in parens: "Versionskontrolle (Version Control)".
- **Scripts**: `#! /usr/bin/env python3`, `chmod +x`, PEP 8.
