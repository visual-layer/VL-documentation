---
name: tech-write
description: "Guide technical documentation with clarity, actionable steps, and confidence. Use when creating, editing, or reviewing technical documentation including API docs, tutorials, guides, how-tos, README files, or any content that teaches users to accomplish technical tasks. Helps maintain consistent voice, avoid forbidden writing patterns, and ensure documentation empowers users. Also use when writing or editing Visual Layer product documentation, deployment guides, installation guides, or admin guides, and when applying Visual Layer terminology, capitalization, or structural conventions."
---

# Technical Writing

Write as a well-informed, pragmatic advisor who is technical but never condescending, always teaching and enabling rather than just telling. Visual Layer documentation follows specific product conventions layered on top of these general standards.

## Start Here: Load References Before Responding

This is a pre-flight step, not a suggestion. Load the relevant reference file(s) before answering any question, drafting any content, or giving any advice about documentation structure, placement, audience, or feature availability. Having grep results or prior context about the repo does not substitute for loading the references — those files contain rules that are not inferrable from source code alone.

Do not skip this step because you are "only advising" or "not writing yet." Placement decisions, structure questions, audience questions, and feature availability questions all depend on information in these files. If the task touches documentation in any way, load what applies.

**`references/feature-availability.md`** — load for:
- Any question about whether a feature is available, to whom, or under what conditions
- Any task involving documenting a Visual Layer feature
- Scanning vl-product or any VL repo to identify new or changed functionality
- Deciding whether content belongs in external docs, internal docs, or no docs at all

The product codebase is the `vl-product` repository, expected to be cloned alongside this docs repo (e.g., `../vl-product` relative to the VL-documentation root). All file paths in the Feature Availability Reference are relative to that root. Read those files directly to verify feature state — do not infer behavior from documentation or memory. The cloud production source of truth is `devops/env/prod/values.yaml`, not `settings.py`.

**`references/feature-overview-template.mdx`** — load for:
- Creating any new feature documentation page from scratch
- Any page that introduces a feature, explains how it works, provides an architecture breakdown, or walks through usage steps

**`references/processes-template.mdx`** — load for:
- Creating or editing workflow, automation, or trigger documentation
- Any page involving the Visual Layer Console, workflow steps, or trigger configuration

**`references/mintlify-setup.md`** — load for:
- Writing or reviewing developer setup content, prerequisites sections, or Mintlify CLI instructions

Load each file by reading it fully before starting the task. Do not load all four for every task — load what the task requires, and nothing more.

### Camtek Is Out of Scope Unless Explicitly Invoked

Camtek is a specific customer with its own documentation and code repos (`vl_camtek`, `vl-docs-camtek`) and a dedicated skill (`/camtek-docs`). Unless one of those repos is active or `/camtek-docs` has been explicitly invoked in this session, Camtek is not relevant to the current task.

When Camtek appears in the codebase — in client overlay configs, allowlists, or deployment paths — treat it as a signal to filter that content out, not to discuss it. Do not reference Camtek features, Camtek-specific configs, or Camtek deployment details in general Visual Layer documentation. The only valid mention of Camtek in this skill's scope is to note that something is customer-specific and therefore excluded from general docs.

### When Scanning vl-product or Any VL Repository

When you scan vl-product (or any other VL repo) to identify new code or new features, consult `references/feature-availability.md` before surfacing anything in documentation. For every feature you identify:

1. Check `vl/common/settings.py` against the Feature Availability Reference to determine the global default and whether an email allowlist restricts it.
2. Apply the Documentation Decision Tree from `feature-availability.md` to determine the correct documentation status.
3. Surface each feature with an explicit availability label:

| Label | Criteria |
|---|---|
| **GA — all users** | Globally enabled, no email allowlist |
| **GA on-prem, rolling out to cloud** | Enabled without restriction in `devops/env/k3s/values.yaml`; gated by customer allowlist in `devops/env/prod/values.yaml`. Document for on-prem audiences as generally available. Note "not yet available to cloud users" in cloud-facing docs. |
| **Limited rollout** | Globally disabled, diverse external email allowlist (not tied to one customer) |
| **Internal only** | Gated by `is_vl_user()` check or allowlist contains only `@visual-layer.com` addresses |
| **On-prem only** | Requires `RUN_MODE = ONPREM`; not available in cloud at all |
| **Pre-release** | Enabled in staging config but not production |
| **Not shipped** | Globally disabled, no allowlist, absent from all env configs |

Never describe a feature as available to all users without first confirming its status in the Feature Availability Reference. Features with email allowlists, internal-only gates, or staging-only configs must be labeled accordingly — or excluded from external documentation entirely.

## Core Principles

- Second person, active voice, confident delivery
- Vary sentence length: very long sentences for complex relationships, long sentences for procedures, short sentences for emphasis
- 12th grade reading level
- Write full sentences with proper connectors
- Trust the reader and state points directly
- Remove filler words and trust readers to infer obvious connections
- Direct, factual, instructive throughout
- No pleasantries: never "please", "kindly", "feel free to", "you may want to"
- No hedging: never "may", "might", "could potentially", "it is possible that"
- No marketing language, enthusiasm, or "revolutionizing" anything
- State capabilities as facts, not possibilities
- Professional but not formal. Write like a capable colleague explaining a system.

## The Imperative Rule

This is the most important structural rule in Visual Layer documentation. Imperative verbs signal "do this now" and are reserved exclusively for procedural steps.

**In procedures:** Use imperatives. "Run the following command." "Click **Save**." "Verify the output."

**Everywhere else:** Use instructive but non-imperative language.

- Chapter intros: "This chapter walks through...", "The next step is to...", "With X in place, the following phase..."
- Prerequisites: "Before proceeding, X must be installed...", "The following tools are required..."
- Context: "These settings control...", "The backend connects to..."

Never mix the two on the same line. A sentence that starts descriptively and ends with an imperative confuses the reader about when to act.

**Exception:** Cross-references are acceptable imperatives in non-procedural text: "See the Glossary" or "See Chapter 3."

## Forbidden Patterns

Never use these patterns:

**Opening crutches:**
- "Here's the thing," "Let's be honest," "Question for you"

**Triadic structures:**
- "No X, no Y, just Z"
- "Not X, not Y, but Z"

**Oppositional shortcuts without proof:**
- "X rather than Y" (unless you show the distinction in action)
- "X over Y" (as hollow shorthand)

**Buzzwords:**
- unlock, harness, landscape, broke the mold, in today's world

**Weak intensifiers:**
- actually (for emphasis), just (to minimize), you're not imagining it

**Punctuation overuse:**
- Em dashes as catch-all punctuation (use very sparingly)
- Colons replacing clear sentence structure
- Fragmented rhythm: "X enough to hold focus. Y enough to go where thinking leads."

## Phrases to Avoid

| Do not write | Write instead |
|---|---|
| "You should see..." | "The output shows..." or "Expected output:" |
| "You will use..." | "All remaining steps use..." |
| "You need to..." | Direct imperative (in procedure) or factual statement (elsewhere) |
| "Complete the following..." | "The following X must pass..." |
| "Please click..." | "Click..." |
| "Feel free to..." | (delete entirely) |
| "i.e." or "e.g." | "For example:" or restructure |

## Terminology and Capitalization

- **Product name**: "Visual Layer" is always two words, always capitalized, always bold in running text
- **Roles are proper nouns**: Admin, Editor, Viewer, Owner are always capitalized
- **"user" is always a common noun**: lowercase unless starting a sentence
- **UI elements are bold**: **Dataset Inventory**, **Filter Panel**, **Create User**, **Save & Continue**
- **Acronyms**: Spell out on first appearance in the document ("OpenID Connect (OIDC)"), then acronym only. Brand names (NVIDIA, K3s, Longhorn, Keycloak) do not need expansion.

## Documentation Modes

### Write Mode

Create new documentation from scratch.

**Process:**
1. Identify user goal and context
2. Determine prerequisites and assumptions
3. Build logical hierarchy
4. Write steps that move users forward
5. Test every command and code sample
6. Add context where decisions matter

**Structure:**
- Start with what the user will accomplish
- List prerequisites upfront
- Use clear, descriptive headings
- Keep paragraphs focused (3-5 sentences)
- End with next steps or related resources

### Edit Mode

Improve existing documentation for clarity and usability.

**Focus areas:**
1. Remove redundant explanations
2. Strengthen weak verbs
3. Eliminate jargon or define it immediately
4. Verify technical accuracy
5. Improve flow between sections
6. Add missing context

**Red flags:**
- Passive voice where active works better
- Vague pronouns (it, this, that) without clear antecedents
- Steps that assume knowledge not yet introduced
- Code samples without context
- Missing error scenarios

### Review Mode

Evaluate documentation against quality standards. Use the review checklist at the end of this document.

## Document Architecture

Visual Layer documentation follows a consistent hierarchy:

1. **About This Documentation** — scopes the guide, identifies the audience, references glossary and vendor docs
2. **Conceptual chapters** — explain architecture, components, how things work (non-imperative throughout)
3. **Procedural chapters** — step-by-step installation, configuration, or usage (imperatives in numbered steps only)
4. **Administration chapters** — workspace settings, user management, configuration (mixed concept and procedure)
5. **Appendices** — reference tables (env vars, CLI reference, services), troubleshooting, glossary, vendor documentation

Each guide targets a specific persona, and all content must be pitched to that persona's technical depth. A deployment guide for DevOps engineers and an installation guide for site administrators cover overlapping systems but at different depths.

## Structure Guidelines

### Heading Hierarchy

- H1: Page title (one per document)
- H2: Major sections
- H3: Subsections
- H4: Specific procedures or concepts
- Never skip levels

### Headings and Introductory Text

Every heading must be followed by at least one sentence of introductory text before any procedure, list, table, or code block. No exceptions. This grounds the reader before they encounter structured content.

### Prerequisites Section

Include when users need specific tools installed, access permissions, prior configuration, or baseline knowledge.

Format:
```markdown
## Prerequisites

Before you begin, verify you have:
- Tool X installed (version Y or later)
- Access to Z
- Completed [previous step]
```

### Procedural Writing

Procedures follow this pattern:

1. A heading with an anchor ID
2. Introductory text explaining what the procedure accomplishes
3. A procedure title block (format depends on output: LaTeX `\processstart` for PDF, `<Steps>` for MDX, numbered list for plain markdown)
4. Numbered steps using imperative verbs
5. Verification steps showing the command and expected output
6. Cross-reference to troubleshooting if applicable

Actions must never share a line with their explanatory intro. Separate explanation from command with a line break.

Verification steps use passive/descriptive language for results: "The output shows..." or "Expected output:" Never write "You should see..."

### Step Formatting

**For procedures:**
1. Use numbered lists for sequential steps
2. Start each step with an action verb
3. Include expected outcomes
4. Add code blocks with language tags

**For concepts:**
- Use paragraphs to explain
- Reserve bullets for true lists (not prose broken into fragments)
- Define terms inline on first use
- Use ordered lists only when sequence matters
- Lead-in sentences before all lists

## Style Standards

### Sentence and Paragraph Structure

- Short paragraphs, sentences rarely exceeding 20 words
- Full sentences with real connectors doing the work
- No artificial rhythm from fragmented sentences

### Feature-Benefit Pattern

Connect features to user outcomes.

**Weak:** "The API supports batch processing."
**Strong:** "Process multiple requests in a single API call to reduce latency and simplify error handling."

### Minimalist Approach

- Remove filler words (very, really, quite, simply, just)
- Cut redundant phrases
- Use "you" and "your" instead of "the user" or "one"

### Code Samples

- Always include language identifier: ```python, ```bash, ```json
- Show complete, runnable examples
- Add comments for non-obvious steps
- Document expected output in comments: `# Expected output: ...`
- Multi-line commands use backslash continuation
- Show exact, copy-pasteable commands in procedures (never pseudocode)
- Use `<placeholder>` for values the reader must replace, and state what to replace them with

Example:
```python
# Fetch user data from API
response = requests.get(f"{BASE_URL}/users/{user_id}")

# Raises an exception if request failed
response.raise_for_status()

# Returns parsed JSON
return response.json()
```

### Tables

- Use simple markdown tables for short, simple data
- Use structured/formatted tables for complex multi-line content (LaTeX `tabularx` for PDF, HTML tables for MDX)
- Header rows are always bold
- First column typically narrower (25-30%) with the second column filling remaining width

### Cross-References

- Reference other sections by display text and anchor: `[Troubleshooting](#troubleshooting)`
- When referencing another guide, use the full guide name in bold: "see the **Deployment Guide**"
- Every troubleshooting reference should be specific: "[Troubleshooting — Cluster and Deployment](#troubleshooting-cluster)" not just "see Troubleshooting"

### Error Guidance

Address likely failures without catastrophizing.

**Weak:** "Make sure you don't forget to set the API key or everything will break."
**Strong:** "Set your API key in the environment file. Without it, authentication requests will return a 401 error."

### Troubleshooting Sections

Troubleshooting uses a two-column table format:

| **Issue** | **Solution** |
|---|---|
| Error message or symptom (monospace if literal) | Instructive fix with exact commands |

Organize by deployment phase or component. Include foreseeable error scenarios rather than waiting for users to report them.

## Decision Framework

### When to Add Detail

Add explanation when:
- The step is non-obvious
- Multiple options exist
- The choice impacts security or performance
- Users commonly make mistakes here

### When to Omit Detail

Skip explanation when:
- The action is standard practice
- Users with stated prerequisites would know
- Detail belongs in a different document (link to it)

### Sentence Length Strategy

- **Very long sentences:** Use for explaining complex relationships or providing comprehensive context with multiple dependent clauses
- **Long sentences:** Use for procedures with multiple steps or when connecting related concepts
- **Short sentences:** Use for emphasis, critical warnings, or simple actions

Mix these throughout to avoid monotonous rhythm.

## Quality Indicators

**Strong documentation:**
- Users can complete the task without external help
- Code samples run without modification
- Prerequisites prevent false starts
- Error messages are explained
- Next steps are clear

**Weak documentation:**
- Requires existing expertise to understand
- Jumps between abstraction levels
- Leaves gaps in the workflow
- Uses jargon without definition
- Ends without direction

## Review Checklist

When reviewing Visual Layer documentation, evaluate:

- [ ] Imperative rule: imperatives appear only in procedural steps
- [ ] Every heading has introductory text before any list, table, procedure, code block or child heading. 
- [ ] Actions are on their own line, not sharing a line with explanatory text
- [ ] Roles capitalized (Admin, Editor, Viewer, Owner); "user" lowercase
- [ ] Product name: "Visual Layer" bold, two words, capitalized
- [ ] UI elements bold
- [ ] Acronyms spelled out on first use
- [ ] No forbidden phrases ("you should see", "please", "feel free to", "you need to")
- [ ] Verification steps use descriptive language, not "you should see"
- [ ] Code blocks have language tags
- [ ] Placeholders use `<angle-bracket>` notation with explanation
- [ ] Troubleshooting covers foreseeable errors, not just known ones
- [ ] Content is pitched to the correct persona for this guide
- [ ] No assumptions about reader knowledge that haven't been introduced
- [ ] Sentence length variety throughout
- [ ] No forbidden patterns (colons, em dashes, triadic structures, buzzwords)
- [ ] 4-column config/parameter tables in MDX use `<div className="config-table">` wrapper

## Working Approach

- Read existing content before suggesting changes and match established patterns
- Push back on ideas when it leads to better documentation
- Start with the smallest reasonable changes
- Never add content that serves the wrong audience for the guide being edited
- When in doubt about a convention, check 2-3 existing chapters for precedent

## Workflow

### Before Writing

1. Identify the task type and load the relevant reference file(s) from `references/` — this applies to writing, editing, reviewing, and advising; do not skip because you are "only answering a question"
2. Identify the user's goal
3. List prerequisites and assumptions
4. Map the logical path from start to finish
5. Gather all technical details (commands, paths, parameters)

### During Writing

1. Draft complete sections before refining
2. Test every technical instruction
3. Read aloud to catch awkward phrasing
4. Verify heading hierarchy is logical

### After Writing

1. Run the review checklist
2. Remove forbidden patterns
3. Test all code samples
4. Verify links work
5. Check sentence length variety

## Platform-Specific Notes

### Mintlify

When writing for Mintlify-based documentation:

- Use MDX components where appropriate
- Follow Mintlify's configuration standards
- Test rendering locally before committing
- Reference official docs: mintlify.com/docs
- For developer setup and prerequisites content, use `references/mintlify-setup.md` as the canonical template

**Common components:**
- `<Card>` for featured links
- `<CodeGroup>` for multi-language examples
- `<Accordion>` for optional details
- `<Tabs>` for alternative approaches

**Custom CSS: `config-table`**

Use the `config-table` class for 4-column reference tables where the last column (Description) needs the most space — configuration settings, API parameters, environment variables, and similar reference content. The class sets column widths to 20% / 10% / 10% / 40% and applies `word-break: break-all` to the first column so long identifiers (such as `DATASET_INGESTION_ONPREM_UI_ENABLED`) wrap cleanly rather than overflowing.

```mdx
<div className="config-table">

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `SOME_FLAG` | boolean | `true` | What it does. |

</div>
```

Do not use `config-table` for troubleshooting tables, comparison tables, or any 2-column layout. It is purpose-built for the 4-column config/parameter pattern.

## References

Load these files selectively based on the task at hand. The "Start Here" section at the top of this skill describes when each one applies.

| File | Contents |
|---|---|
| `references/feature-availability.md` | Six-layer feature gating pipeline, documentation decision tree, and full feature inventory with availability status |
| `references/feature-overview-template.mdx` | Approved MDX template for feature-level overview pages: intro, architecture breakdown, usage steps, and related articles |
| `references/processes-template.mdx` | Approved MDX template for workflow and automation process pages, including trigger configuration UI patterns |
| `references/mintlify-setup.md` | Canonical prerequisites and Mintlify CLI setup content for developer-facing documentation |