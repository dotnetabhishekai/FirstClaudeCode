# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is a collection of standalone, single-file HTML web tools/demos — no build system, package manager, or test framework. Each tool is fully self-contained (HTML + CSS + JS in one file) and runs by opening the file directly in a browser.

Current tools:
- `bookmark-manager.html` — card-based bookmark manager with categories, tags, search, and read/unread status (persisted via `localStorage`).
- `invoice-generator.html` — live-preview invoice generator with line items, tax calc, and print/Save-as-PDF support via print CSS.
- `snake.html` — Snake game with smooth interpolated movement, particle effects, speed levels, pause, and touch/keyboard controls; high score in `localStorage`.
- `csv-visualizer.html` — drag-and-drop CSV dashboard with custom CSV parser, per-column type detection/stats, and Chart.js-based bar/line/pie charts.
- `sample-data.csv` — sample dataset for exercising `csv-visualizer.html`.

`prompts_library.txt.txt` and `doc.md` contain the original prompts used to generate each tool and a summary of their features — useful as a spec/reference when extending a tool.

## Working with these files

- There is no build, lint, or test command — verify changes by opening the HTML file directly in a browser.
- Keep each tool fully self-contained in its single HTML file (inline `<style>` and `<script>`). Only `csv-visualizer.html` pulls an external dependency (Chart.js via CDN); avoid adding new external dependencies to the other tools unless necessary.
- Tools follow a dark/neon themed UI using CSS custom properties (`:root { --bg, --panel, --accent, --text, ... }`) defined at the top of the `<style>` block — match this pattern when styling.
- Persisted state uses `localStorage` with tool-specific keys (e.g. `neonSnakeHighScore_DotnetAbhishekAI`). Keep keys namespaced per tool to avoid collisions.
- Each tool's header/footer includes "DotnetAbhishekAI" / "dotnetabhishekai" branding — preserve this in any new tools or edits.
