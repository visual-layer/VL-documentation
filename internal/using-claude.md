# Using Claude Code with This Repo

This guide explains how to use [Claude Code](https://claude.com/claude-code) — Anthropic's coding agent — to write, edit, and review Visual Layer documentation. The repo is set up so that the right voice, conventions, and reference material load automatically when you work from the repo root.

## What Claude Code Knows About This Repo

When you run Claude Code from the VL-documentation root, three things happen automatically:

1. **`CLAUDE.md` loads as durable instructions.** Voice, tone, structural rules, terminology, and Mintlify component conventions are always in context. You do not need to remind Claude how to write Visual Layer documentation.

2. **Project-scoped skills load from `.claude/skills/`.** The skills bundled with this repo are described below. They activate when their description matches what you ask Claude to do.

3. **Standard Claude Code tools are available.** File reading and editing, git operations, search (Grep, Glob), and bash all work out of the box.

## Bundled Skills

The following skills are checked into `.claude/skills/` and load automatically. You do not need to install them separately.

### `tech-write`

The technical writing skill that drives all documentation work. It covers voice, the imperative rule (imperatives only in procedures), forbidden phrases, terminology, structural conventions, and the documentation modes (write, edit, review).

It also includes four reference files:

| Reference | When it loads |
|---|---|
| `feature-availability.md` | When deciding whether a feature should be documented, who it's available to, or how to label it for cloud vs. on-prem audiences |
| `feature-overview-template.mdx` | When creating a new feature documentation page from scratch |
| `processes-template.mdx` | When creating or editing workflow, automation, or trigger documentation |
| `mintlify-setup.md` | When writing developer setup or Mintlify CLI prerequisites content |

The skill expects the `vl-product` repository to be cloned alongside this docs repo at `../vl-product`. Without it, feature-availability checks against the product source code cannot run. See the [Contributing guide](../CONTRIBUTING.md#before-you-start) for the clone command.

### `vl-brand`

The Visual Layer brand voice and style guide. Covers second-person active voice, the confident-and-efficient tone, the minimalist sentence structure, and the marketing color system (brand gradient, background glows, dark and light treatments). Use it for any customer-facing text, including marketing copy that lives outside the docs repo.

## Standard Claude Code Skills Worth Knowing

Beyond the bundled skills, several built-in Claude Code skills are useful for docs work:

| Skill | Purpose |
|---|---|
| `commit` | Drafts a commit message in the repo's existing style and creates the commit |
| `link-checker` | Scans MDX pages for broken internal and external links |
| `mintlify` | Mintlify-specific component reference and configuration help |

These come with Claude Code itself — no installation needed.

## How to Invoke Claude on a Task

Open a terminal in the repo root and run `claude` to start an interactive session, or use the IDE extension. Then describe what you want in plain English.

### Example Tasks

The skills auto-activate based on what you ask. You don't need to name them.

| What you say | What happens |
|---|---|
| "Rewrite the Find Similar section of `docs/explore-and-search/visual-search.mdx` to lead with the hover + crop button" | `tech-write` activates; Claude reads the file, applies voice and structural rules, makes the edit |
| "Audit `docs/quick-start/dataset-exploration-ux.mdx` for forbidden phrases and weak voice" | `tech-write` activates in review mode; Claude returns a list of issues with line numbers |
| "Document the new Object Size Filter — check vl-product to confirm it's GA in cloud" | `tech-write` activates and loads `feature-availability.md`; Claude reads `../vl-product/devops/env/prod/values.yaml` to verify availability before drafting |
| "Update the marketing site hero copy to match the brand voice" | `vl-brand` activates; Claude rewrites the copy against the style guide |
| "Commit these changes" | The `commit` skill drafts a message in the repo's style and runs `git commit` |

### Example Multi-Step Workflow

Adding a new feature page from scratch typically looks like:

1. **Describe the feature.** "I need a new page for the Object Size Filter under explore-and-search. It's GA in cloud as of release 2.58."
2. **Let Claude verify availability.** Claude reads `../vl-product/devops/env/prod/values.yaml` and confirms the flag is enabled with no allowlist.
3. **Draft against the template.** Claude loads `feature-overview-template.mdx` from the `tech-write` skill and produces a draft page.
4. **Review and iterate.** Read the draft, ask Claude to adjust sections, refine examples, or add screenshots.
5. **Commit and open a PR.** Use the `commit` skill, then open the PR with `gh pr create` or the IDE.

## Verifying Feature Availability

This is the highest-value pattern in the repo. Claude has access to the source of truth (vl-product) and the rules for interpreting it (`feature-availability.md`). Use it whenever you are tempted to write "this feature is available to all users" — Claude can confirm or correct that claim against the actual config.

The relevant files in vl-product:

- `devops/env/prod/values.yaml` — cloud production source of truth
- `devops/env/k3s/values.yaml` — on-prem K3s configuration
- `vl/common/settings.py` — global defaults and email allowlists

The `tech-write` skill knows how to interpret these files. Just ask: "Is the Models Catalog GA in cloud?" or "What's the availability status of Train Model?"

## Logging Documentation Gaps to Notion

Visual Layer tracks documentation gaps in a Notion database called **Documentation Gaps & Improvements**. To log items from a Claude session, the docs owner uses the `notion-task-capture` skill, which is **not** bundled with this repo because it requires Notion workspace access tied to specific account permissions.

If you need to log gaps and you have access to the Notion workspace, ask the docs owner to share the skill with your personal Claude Code installation. Otherwise, file a GitHub issue and the docs owner will move it into Notion.

## Updating the Bundled Skills

The skills under `.claude/skills/` are the canonical version for this project. To update them:

1. Edit the files in `.claude/skills/<skill-name>/` directly.
2. Test the change by running Claude Code from the repo root and invoking the skill on a real task.
3. Commit the changes alongside any related docs updates.

If you also maintain personal copies of these skills under `~/.claude/skills/`, the repo copies take precedence when you work from this repo root. You do not need to keep the two in sync — pick one source of truth per project.

## Adding a New Skill to the Repo

To bundle a new skill with this repo:

1. Create a directory under `.claude/skills/<skill-name>/`.
2. Add a `SKILL.md` file with frontmatter (`name`, `description`) and the skill body.
3. Add any reference files under `<skill-name>/references/`.
4. Document the skill in this guide so contributors know it exists.
5. Commit and push.

Skills should be project-scoped — meaning they exist because of something specific to Visual Layer documentation. General-purpose skills belong in your personal `~/.claude/skills/` directory, not the repo.

## Troubleshooting

| Issue | Fix |
|---|---|
| Claude doesn't seem to know the voice rules | Confirm you started Claude Code from the repo root so `CLAUDE.md` loaded |
| `tech-write` skill can't find vl-product | Clone `vl-product` as a sibling of this repo (`../vl-product`) |
| A skill isn't activating when expected | Describe the task more directly — skill activation is description-driven, so vague prompts can miss |
| Pre-commit hooks failing | Fix the underlying issue rather than skipping with `--no-verify`; ask Claude to investigate the failure |

## Related Resources

- [Claude Code documentation](https://docs.claude.com/en/docs/claude-code)
- [`CLAUDE.md`](../CLAUDE.md) — voice, tone, and Mintlify conventions
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — branch and PR workflow
- [Mintlify docs](https://mintlify.com/docs)
