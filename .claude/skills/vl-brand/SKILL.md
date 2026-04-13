---
name: vl-brand
description: Visual Layer brand voice, style, tone, and color guidelines for documentation and marketing content creation
---

# Visual Layer Style Guide

Use this skill when writing or editing Visual Layer documentation, marketing content, or any customer-facing text.

## Brand Identity

**Platform Name**: Always "Visual Layer" (two words, both capitalized)

**Primary Color**: `#0097D9` (Visual Layer blue)

**Product Category**: Computer vision and dataset management platform for visual dataset analysis

## Voice

Visual Layer speaks in **second person, active voice, present tense**.

### Do

- Address users directly: "You can filter results"
- Use possessives: "your dataset," "your team," "your documentation"
- Open sentences with active present tense verbs
- State capabilities as facts

### Don't

- Use passive voice: "Results can be filtered"
- Use gerunds to start sentences
- Use "please" in instructions
- Use first person ("we," "our") unless specifically discussing the company

## Tone

Visual Layer's tone is **confident and efficient**.

### Characteristics

- **Professional but not formal**: Write like a capable colleague, not a manual
- **Direct**: State what is, not what might be
- **Factual**: Let functionality speak for itself
- **Helpful**: Content provides context; the platform solves problems

### Avoid

- Hedging language: "may," "might," "could potentially," "it is possible that"
- Marketing hyperbole: "revolutionary," "game-changing," "best-in-class"
- Excessive enthusiasm: "amazing," "incredible," "exciting"
- Uncertainty: "we think," "we believe," "probably"

## Style

Visual Layer content is **minimalist and scannable**.

### Sentence Structure

- Keep sentences under 20 words
- Use crisp, declarative statements
- Every word serves a function
- No decorative language

### Formatting Rules

- **Interface elements**: Always bold. Examples: **Dataset Inventory**, **Filter Panel**, **Action Bar**
- **Headings**: Always followed by at least one sentence before subsections
- **Lists**: Use unordered lists for 3+ items; ordered lists only when sequence matters
- **Lead-in sentences**: Every list must have an introductory sentence
- **Periods**: Include in all list items, even single phrases

### Prohibited

- "i.e." or "e.g." — Use "For example:" or "Example:" instead
- "Overview" as a heading — Content flows directly from metadata
- Divider lines mid-article
- Time-based statements (keep content evergreen)
- Concluding paragraphs at end of subsections

## Approach

Visual Layer integrates **features with benefits** in descriptions.

### Pattern

Combine what a feature does with why it matters in a single statement.

**Good**: "Semantic Search finds content using natural language, enabling intuitive exploration."

**Good**: "Duplicates detection identifies redundant frames, reducing storage costs."

**Bad**: "Semantic Search is a feature that allows you to search. It uses natural language processing."

### Organization

- Structure content by user action, not technical capability
- Focus on what users do, not what the system has
- Use technical terms only when they clarify, not to impress

## Content Patterns

### Next Steps and Related Resources

Always use CardGroup format with Card components. Never use plain bullet lists.

```jsx
<CardGroup cols={2}>
  <Card title="Explore Datasets" icon="search" href="/explore">
    Search and filter your visual data.
  </Card>
  <Card title="Export Results" icon="download" href="/export">
    Download curated datasets.
  </Card>
</CardGroup>
```

### Images

Always wrap in Frame component:

```jsx
<Frame>
  <img src="/images/example.png" alt="Descriptive alt text" />
</Frame>
```

### Procedures

Use simple numbered lists for process documentation:

1. Open the **Dataset Inventory**.
2. Click **Create Dataset**.

   The dataset creation dialog appears.

3. Enter a name and click **Save**.

Use `<Steps>` component only for tutorials.

---

## Marketing Color System

This section covers color rules for all Visual Layer marketing materials. Slides and website carry the strictest rules. Social graphics and print allow more flexibility within the same system.

### Color Roles

| Token | Hex | Marketing Role |
|-------|-----|----------------|
| Brand Blue | `#0197D8` | Primary CTA, links, highlights; gradient midpoint |
| Gradient Purple | `#A63B94` | Brand gradient start (0%) |
| Gradient Green | `#3CC788` | Brand gradient end (100%) — confirm exact value in Figma |
| Deep Navy | `#080B1A` | Dark-mode background base |
| Background Glow Teal | `#18C07D` | Atmospheric background glow on dark surfaces |
| Background Glow Violet | `#6B3FA0` | Atmospheric background glow, lower anchor |
| White | `#FFFFFF` | Light-mode background; all text on dark backgrounds |
| Near-Black Text | `#0D1117` | Body text on light backgrounds |

Visual Layer uses **two distinct gradient systems** that serve different purposes and should never be confused:

1. **The brand gradient** (`#A63B94` → `#0197D8` → `#3CC788`): a linear three-stop arc from purple through blue to green. Used exclusively on borders, dividers, and decorative accent shapes. This is a high-energy, chromatic element.
2. **The background glow**: soft radial glows in teal and violet that create atmospheric depth behind content. These are always diffuse — never crisp, never linear.

The multicolor logo "V" mark is the only other place multi-hue color appears. Do not apply the brand gradient to backgrounds, typography, or UI elements.

---

### Dark Treatment (Established)

The dark treatment is Visual Layer's primary and most mature expression. Use it for hero sections, full-bleed backgrounds, and any context where the brand needs to project technical depth or authority.

**Background base**: `#080B1A` (deep navy, near-black). Never pure black (`#000000`), which reads flat and cheap against the gradient glows.

**Background glow construction**: Radial glows placed off-center, never centered or symmetrical. The teal glow (`#18C07D`) anchors toward the upper-right or top-center. The violet glow (`#6B3FA0`) sits lower, typically bottom-right or bottom-center. Both glows blend softly into the base — atmospheric and illuminated, not painted or neon. Glow opacity stays between 40–70%: enough to read clearly, not so strong they compete with content.

**Text**: White (`#FFFFFF`) only. No off-white or gray for body text on dark backgrounds — contrast is too critical to compromise.

**Accent/CTA color**: Brand Blue (`#0097D9`) for buttons, links, and inline highlights. This is the only chromatic flat color that appears in UI-adjacent marketing elements. Do not use teal or violet as standalone flat accent colors — they exist only within gradients.

**Surface layering**: When cards, callout boxes, or overlay panels appear on dark backgrounds, use a semi-transparent dark surface at approximately `rgba(55, 60, 72, 0.6)` (derived from the UX `#373C48` Dataset BG token). This maintains depth without introducing a competing color.

---

### Light Treatment (Emerging)

The light treatment preserves the same brand identity with a white or near-white base. The gradient glows carry over, used sparingly as atmospheric accents rather than full-bleed backgrounds.

**Background base**: White (`#FFFFFF`) for the strictest surfaces (slides, website). Near-white surfaces such as `#F5F7FA` are acceptable for secondary panels, cards, or sidebar areas where a subtle separation from pure white helps readability.

**Background glow usage on light surfaces**: Apply as a soft radial wash in a corner or along one edge, not as a full bleed. Glow opacity should drop to 15–30% on white backgrounds. Use one glow color per composition on light surfaces — teal (`#18C07D`) or violet (`#6B3FA0`) — unless the layout is large enough to carry both without overwhelming the white space.

**Text**: Near-black (`#0D1117`) for headings and body copy. Mid-gray (`#5A6070`) for secondary labels, captions, and metadata. Never use the dark UX background tokens (`#151928`, `#373C48`) as text colors on light backgrounds — they read muddy against white.

**Accent/CTA color**: Brand Blue (`#0097D9`) remains the accent and CTA color on light backgrounds, identical to the dark treatment. This consistency is what makes the two treatments feel like one brand system.

**Surface layering**: Light cards and panels sit on `#F5F7FA` or `#EAECF0` — cool, neutral grays that echo the brand's technical character without introducing warmth.

---

### Gradient Construction Rules

**Brand gradient** (`#A63B94` → `#0197D8` → `#3CC788`)

This gradient is linear and always runs the full three-stop arc. Never truncate it to two stops — the purple-to-blue without green, or blue-to-green without purple, reads incomplete and inconsistent. Apply it to borders, dividers, and decorative accent shapes only. The stroke weight or shape size should be thin enough that the full color arc reads at a glance — typically 2–4px for borders and proportionally scaled for shapes.

**Background glows**

Background glows are always radial, never linear. A linear gradient reads as a texture. A radial glow reads as a light source, which is the effect the Visual Layer aesthetic depends on. Maximum two glow anchor points per composition — more than two creates visual noise. The glow colors are teal (`#18C07D`) and violet (`#6B3FA0`) only. Do not improvise new glow colors or use the brand gradient colors as glow sources.

**Background vs. accent — keep these separate**

The brand gradient and the background glows operate in different visual layers and should never overlap. A brand-gradient border sits on top of a glow background, not inside it.

---

### Per-Surface Rules

**Slides and Website (Strictest)**

- Use only the defined color tokens. No improvised accent colors.
- Every background is either the dark base (`#080B1A`) or white (`#FFFFFF`). Do not use mid-tone backgrounds such as medium gray or desaturated teal.
- Gradient glows follow the construction rules above exactly.
- Brand Blue (`#0097D9`) is the only CTA color. No secondary button colors.
- Typography is white on dark and near-black (`#0D1117`) on light. No exceptions.
- Do not mix dark and light treatments within a single slide or page section unless a deliberate full-bleed section break makes the transition structurally clear.

**LinkedIn Social Graphics (Flexible)**

- The same color tokens apply, but single-glow compositions are acceptable where a full teal-violet range would feel heavy at small sizes.
- Brand Blue (`#0097D9`) can be used as a background tint for text-only cards, at reduced opacity over the dark base.
- White text on dark and near-black text on light still apply strictly — contrast cannot be compromised on social feeds.
- The multicolor "V" logo mark is the most reliable brand signal at small sizes; lead with it.

**Print and Event Materials (Flexible)**

- Confirm color profiles with your print vendor (CMYK conversion from the hex values above). Brand Blue converts to approximately C:100 M:25 Y:0 K:5.
- Gradient glows should be pre-rendered as high-resolution raster assets rather than reproduced as vector gradients, which often shift on press.
- On large-format materials (booth backdrops, banners), the full dark treatment with both teal and violet glows is the strongest brand expression. Light treatment is viable for collateral such as datasheets and one-pagers, where readability under fluorescent lighting matters more than brand intensity.

---

### What to Avoid

- **Using the brand gradient as a background.** It belongs on borders, dividers, and accent shapes only. As a background it competes with content and loses its identity as a brand accent.
- **Truncating the brand gradient to two stops.** Always run the full `#A63B94` → `#0197D8` → `#3CC788` arc.
- **Linear background gradients.** Background depth comes from radial glows only.
- **Mid-tone backgrounds.** Medium gray, desaturated blue, or dark teal as a flat background creates visual ambiguity between the dark and light treatments.
- **Warm colors outside the logo mark and brand gradient.** Orange, yellow, or standalone red anywhere else makes the brand feel inconsistent.
- **Overlit glows.** A background glow at 90%+ opacity competes with content.
- **Brand Blue as a background color.** It is an accent and CTA color only.

---

## Quick Reference

| Element | Rule |
|---------|------|
| Platform name | Visual Layer (two words) |
| Voice | Second person, active |
| Tone | Confident, efficient |
| Sentences | Under 20 words |
| Interface elements | Always **bold** |
| Lists (3+ items) | Unordered |
| Hedging words | Never |
| "Please" | Never |
| "i.e." / "e.g." | Never (use "For example:") |

## Examples

### Before (Wrong)

> The filtering feature may help you potentially find images that could match your criteria. Please click on the Filter button to get started. This is an amazing tool that we believe will revolutionize your workflow.

### After (Correct)

> Filter images by metadata, labels, or visual similarity. Click **Filter** in the **Action Bar** to open the **Filter Panel**. Select your criteria and click **Apply**.
