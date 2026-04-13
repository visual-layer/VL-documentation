# Contributing

Thanks for working on Visual Layer documentation. This guide covers the branch workflow, commit conventions, and review process. For style, voice, and Mintlify conventions, see [`CLAUDE.md`](./CLAUDE.md). For the Claude Code workflow, see [`internal/using-claude.md`](./internal/using-claude.md).

This file and everything under `internal/` are internal-only and excluded from the published documentation site.

## Before You Start

Make sure you have:

- A working local checkout of this repo (see [README](./README.md) for setup)
- The Mintlify CLI installed and `mintlify dev` running successfully
- Read [`CLAUDE.md`](./CLAUDE.md) for voice, tone, and structural conventions

If you plan to verify feature availability against the product, also clone `vl-product` as a sibling directory of this repo:

```bash
cd ..
git clone https://github.com/visual-layer/vl-product.git
```

The `tech-write` skill expects `vl-product` at `../vl-product` relative to the docs repo root.

## Branch Workflow

The default branch is `main`. All changes go through pull requests.

1. Create a branch from `main` with a descriptive name.

   ```bash
   git checkout main
   git pull
   git checkout -b <topic-branch-name>
   ```

   Use kebab-case names that describe the change, such as `landing-page-legal-cards` or `fix-cluster-explore-screenshots`.

2. Make your edits, committing frequently.

3. Push the branch and open a pull request against `main`.

   ```bash
   git push -u origin <topic-branch-name>
   ```

4. Request review and wait for approval before merging.

## Commit Messages

Write clear, present-tense commit subjects under 70 characters. The body should explain the *why* when it's not obvious from the diff.

Examples from this repo:

- `Add Terms of Service and Privacy Policy cards to landing page`
- `Expand self-hosting Configuration page with config.json and .env docs`
- `Adjust config-table column widths to 20/10/10/40`

Avoid `--no-verify` when committing. Pre-commit hooks exist for a reason — if a hook blocks you, fix the underlying issue rather than skipping it.

## What Gets Committed Where

| Type of change | Goes in |
|---|---|
| Page content (text, MDX components, structure) | `docs/<section>/<page>.mdx` |
| Screenshots, diagrams, screen recordings | `images/<descriptive-name>.{png,gif,mp4}` |
| Navigation, sidebar, page ordering | `docs.json` |
| Custom CSS classes or branding tweaks | `styles.css` |
| Style or convention rules for Claude | `CLAUDE.md` |
| Project-scoped Claude skills | `.claude/skills/<skill-name>/` |
| Internal process docs (not published) | `internal/` |

Always commit image assets in the same PR as the MDX pages that reference them. Orphan references and orphan images both cause confusion later.

## Pull Request Checklist

Before requesting review, verify:

- [ ] `mintlify dev` runs cleanly with no console errors
- [ ] All new pages have frontmatter (`title`, `description`, `sidebarTitle` if needed)
- [ ] All new images are committed alongside the MDX that references them
- [ ] Internal links use relative paths (no absolute URLs to docs.visual-layer.com)
- [ ] All code blocks have language tags
- [ ] All images have alt text
- [ ] Headings have introductory text before any subheadings, lists, tables, or code blocks
- [ ] Voice and style match [`CLAUDE.md`](./CLAUDE.md)

## Review Process

Pull requests are reviewed by Visual Layer's documentation owner. Expect comments on:

- Voice and tone consistency
- Structural conventions (headings, prerequisites, related resources)
- Technical accuracy (especially feature availability claims)
- Image quality and asset organization

Address comments by pushing additional commits to the same branch — do not force-push unless explicitly asked.

## Reporting Issues

For documentation bugs, missing content, or stale screenshots, file an issue in the [GitHub issue tracker](https://github.com/visual-layer/VL-documentation/issues) or add an entry to the **Documentation Gaps & Improvements** Notion database (ask the docs owner for access).
