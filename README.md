# Visual Layer Documentation

This repository contains the source for the Visual Layer documentation site, built with [Mintlify](https://mintlify.com). It covers product usage, deployment, API reference, and admin guides for cloud and on-premises customers.

The published site lives at [docs.visual-layer.com](https://docs.visual-layer.com).

## Repository Layout

| Path | Contents |
|---|---|
| `docs/` | All published documentation pages, organized by section (`quick-start/`, `explore-and-search/`, `Dataset-Enrichment/`, etc.) |
| `images/` | Screenshots, diagrams, and screen recordings referenced by MDX pages |
| `docs.json` | Mintlify navigation, theme, and site configuration |
| `styles.css` | Custom CSS for Visual Layer branding, tables, and components |
| `CLAUDE.md` | Instructions for Claude Code when editing this repo (style, voice, conventions) |
| `CONTRIBUTING.md` | Branch workflow, commit conventions, and review process |
| `internal/` | Internal-only documentation (excluded from the published site) |
| `.claude/skills/` | Project-scoped Claude Code skills bundled with the repo |

## Quick Start

The fastest way to preview docs locally is to install the Mintlify CLI and run the dev server.

### Prerequisites

- **Node.js** version 19 or higher ([download](https://nodejs.org/))
- **Git** ([download](https://git-scm.com/))
- **A code editor** such as [VS Code](https://code.visualstudio.com/)

### Install and Run

1. Clone the repository.

   ```bash
   git clone https://github.com/visual-layer/VL-documentation.git
   cd VL-documentation
   ```

2. Install the Mintlify CLI globally.

   ```bash
   npm install -g mintlify
   ```

3. Start the development server from the repo root.

   ```bash
   mintlify dev
   ```

4. Open `http://localhost:3000` in your browser.

To run on a different port:

```bash
mintlify dev --port 3333
```

## Editing Documentation

All pages are MDX (Markdown with JSX components). Style, voice, structure, and Mintlify component conventions are documented in [`CLAUDE.md`](./CLAUDE.md). Contributors should read it before making content changes.

For branch and commit conventions, see [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## Working with Claude Code

This repo is set up for collaborative editing with [Claude Code](https://claude.com/claude-code), Anthropic's coding agent. Project-scoped skills are bundled under `.claude/skills/` and load automatically when you run Claude Code from the repo root.

For the full Claude workflow, including which skills are available and how to use them, see [`internal/using-claude.md`](./internal/using-claude.md). That file is internal-only and excluded from the published docs site.

## Related Resources

- [Mintlify documentation](https://mintlify.com/docs)
- [Visual Layer product site](https://visual-layer.com)
- [Published docs site](https://docs.visual-layer.com)
