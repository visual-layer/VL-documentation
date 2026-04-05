# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the **Visual Layer Documentation Website** - a comprehensive documentation platform built with Mintlify for Visual Layer's computer vision and dataset management platform. The repository contains technical documentation, API references, deployment guides, and user manuals for Visual Layer's visual dataset analysis platform.

## The most important rules
- Always ask if you're not sure and NEVER assume 
- Always align with the conventions, guidelines, standards, style tone & voice we've established in this guide
- Always consult with mintlify docs if you you're not sure on structure, syntax, etc.

## Common Development Commands

### Local Development
```bash
# Install Mintlify CLI globally
npm install -g mintlify

# Start development server
mintlify dev

# Start on custom port
mintlify dev --port 3333
```

### Testing and Development
Since this is a documentation site, there are no test commands or build processes beyond local development server startup.

## Architecture & Structure

### Documentation Platform
**Framework**: Built on Mintlify using `docs.json` as the main configuration file for navigation, theming, and site structure.

**Content Format**: All documentation uses MDX (Markdown + JSX) allowing for rich interactive components including:
- Card groups for navigation
- Steps components for procedures
- Tip and Note callouts for important information
- Code blocks with syntax highlighting
- Embedded videos and interactive examples

### Content Organization

**Documentation Structure**: Content is organized hierarchically with clear navigation paths and consistent file naming conventions.

### Content Standards & Patterns

**Front Matter Structure** (based on established documentation standards):
```yaml
---
title: "Page Title"                 # Full clear, descriptive title
description: "Brief description"    # SEO and page description
sidebar: "Page Title Shortened if Necessary" # Page title shortened to 20 characters maximum (not shortened if not necessary)
---
```

**Page Structure Patterns**:

Following are the different kinds of content maintained in this repo:

1. **Overview Pages** (introduces a set of related pages; intro to "what's coming" in the rest of the relevant section/set of pages):
   - Brief introductory paragraph explaining the concept
   - Card components for organizing related content by theme
   - Clear navigation pathways to detailed sections
   - Card group layouts for navigation
   - Each card with descriptive title and brief description
   - Clear visual organization for better user experience

2. **Concept Pages** (Definitions and Entities style):
   - Note callouts for important introductory information
   - Definition tables with custom styling classes
   - Two-column layout for terminology explanations
   - Comprehensive concept explanations with examples

3. **Process Documentation Pages** :
Process Documentation Pages represent the bulk of the documentation, and guide users through a specific feature and the actions that can be taken. For long processes and/or features with many actions, this might be broken down into a group of process documentation pages. These, like other pages should open with an Overview Page (as described above). 
   - Prerequisites section listing required setup
   - Step-by-step numbered instructions with clear actions and outcomes. 
   - Use the simple ordered lists for these procedures. Make sure outcomes are on new lines but part of the step that led to the outcome. 
   - Code examples in fenced code blocks

4. **Tutorial Pages**:
Tutorials guide users through a specific use case example in order to show them interactively how to use the platform/feature. Tutorials, like other pages should open with an Overview Page (as described above). Each page should represent and entire end-to-end use case or a standalone process/procedure.
   - Prerequisites section listing required setup
   - Step-by-step numbered instructions with clear actions and outcomes.
   - Use the `<Step>` object for these procedures. Make sure outcomes are on new lines but part of the step that led to the outcome
   - Code examples in fenced code blocks

**Standard Icon Mapping for Cards and Components**:

Use the following icon names consistently across all documentation:

- **Tutorial Objectives cards**: `icon="goal"`
- **Tutorial Scenarios accordions**: `icon="target"`
- **Create and/or update next step cards**: `icon="database"`
- **General Explore next step cards**: `icon="search"`
- **Semantic Search cards**: `icon="scan-text"`
- **Visual Search cards**: `icon="scan-search"`
- **Filtering cards**: `icon="sliders-horizontal"`
- **Export cards**: `icon="download"`
- **Share cards**: `icon="share-2"`
- **All other collaboration and saved views**: `icon="blend"`
- **Enrichment cards**: `icon="sparkles"`
- **Terms next step cards**: `icon="book-a"`
- **Deployment and Technical article and self-hosting next step cards**: `icon="blocks"`
- **Inventory update next step cards**: `icon="layout-dashboard"`
- **Next step cards to other tutorials**: `icon="graduation-cap"`
- **Models and model catalog cards**: `icon="boxes"`
- **Metadata management cards**: `icon="file-braces-corner"`
- **API reference cards**: `icon="file-code-2"`
- **Clusters cards**: `icon="grid-3x3"`
- **Data quality and curation cards**: `icon="library-big"`
- **Objects cards**: `icon="group"`
- **Image view cards**: `icon="images"`
- **Task manager cards**: `icon="list-checks"`
- **Troubleshooting cards**: `icon="bug"`
- **Users/user management cards**: `icon="users"`
- **Administration general cards**: `icon="shield"`


### Mintlify Configuration

Key configuration in `docs.json` and `fastdup-docs.json`:
- **Theme**: Custom Visual Layer branding with primary color `#0097D9`
- **Navigation**: Tab-based structure with grouped pages
- **Features**: Custom styling, interactive components
- **Legacy Integration**: Separate fastdup documentation configuration

### Assets Organization
- `/images/` - Screenshots, videos, and diagrams organized by feature
- `/favicon.png` and `/favicon.svg` - Brand assets for site favicon
- `styles.css` - Global styling customizations and Visual Layer branding

### Custom Styling
The repository includes extensive custom styling in `styles.css` with:
- **Brand Colors**: Primary Visual Layer blue (`#0097D9`) and gradient themes
- **Typography**: Custom Roboto font family with specific weights and letter spacing  
- **Components**: Hero sections, search bars, API grids, and custom table styles
- **Responsive Design**: Mobile-first approach with defined breakpoints

## Development Guidelines

**When Creating New Documentation**:
1. Follow the established front matter structure
2. Use appropriate page structure patterns based on content type
3. Implement MDX components for enhanced formatting
4. Maintain consistency with existing documentation standards
5. Test all code examples and procedures before publishing

**Content Style Guidelines**:

**Tone - Confident and Efficient**
- State capabilities as facts. Your content provides the context. The platform helps users solve problems.
- Professional but not formal. Write like a capable colleague, not a manual.
- No hedging or uncertainty. Avoid "may," "might," "could potentially," or "it is possible that."
- Let functionality speak for itself. No marketing hyperbole, excessive enthusiasm, or "revolutionizing" language.

**Voice - Second Person and Active**
- Use "your documentation," "your dataset," "your team" for direct engagement.
- Address the user directly. "You can filter results" not "Results can be filtered."
- Active voice unless absolutely unavoidable. Open sentences with active present tense, not gerunds.
- Never use "please." Say "Click Submit" not "Please click Submit."

**Style - Minimalist and Scannable**
- Short paragraphs. Rarely exceed 20 words per sentence.
- Clear headers organize content. Every section starts with introductory text.
- **CRITICAL**: All headings must have at least one sentence before any subsections. Never place an h3 directly after an h2 without intervening text.
- Almost no decorative language. Every word serves a function.
- Crisp declarative sentences. State what is, not what might be.

**Approach - Feature-Benefit Integration**
- Embed value propositions in descriptions. "Semantic Search finds content using natural language, enabling intuitive exploration" combines what and why.
- Organize by user action rather than technical capability. Focus on what users do, not what the system has.
- No jargon for jargon's sake. Use technical terms when they clarify, not impress.
- Never use "i.e." or "e.g." Use "For example:" or "Example:" with proper punctuation.

**Formatting Standards**
- Use MDX components (Card, Steps, Tip, Note) for enhanced user experience.
- Capitalize consistently. Prepositions in titles always lowercase.
- Check spacing before finishing. Formatting with ** ** mid-sentence requires attention.
- **CRITICAL**: Both "Next Steps" and "Related Resources" sections must use CardGroup format with Card components. Never use plain bullet lists for these sections.
- Always include periods, even in ordered lists.
- Every article opens with an introduction, even if minimal.
- Never use divider lines mid-article without consultation.
- **CRITICAL**: All interface elements and names of interface areas must always be BOLD. Examples: **Dataset Inventory**, **Filter Panel**, **Action Bar**, **Search**, **Export**.

## Visual Layer Documentation Standards

### Writing Guidelines
- **Voice**: Second person ("you"), active voice, present tense. Address users directly.
- **Tone**: Confident and efficient. State capabilities as facts, not possibilities.
- **Platform Naming**: "Visual Layer" (consistent capitalization)
- **Content Strategy**: Prioritize accuracy and usability. No lengthy explanations or marketing language.
- **Sentence Length**: Crisp and declarative. Rarely exceed 20 words.
- **Structure**: Include prerequisites, clear step-by-step instructions, and related resources
- **Format**: Use relative paths for internal links, language tags on code blocks, alt text on images
- **Approach**: Integrate features with benefits. "Duplicates detection identifies redundant frames, reducing storage costs" combines what and why.

### Git Workflow Requirements
- NEVER use `--no-verify` when committing
- Ask about uncommitted changes before starting work
- Create new branch when no clear branch exists
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

### Documentation Quality Standards
- Test all code examples before publishing. Accuracy matters.
- Match style and formatting of existing pages. Maintain consistency.
- Search existing content before adding new material. Avoid duplication.
- Check existing patterns. Align with established conventions.
- Start with the smallest reasonable changes. Respect what works.
- Make content evergreen. Avoid time-based statements.
- Write with confidence. State capabilities as facts, not possibilities.
- Keep sentences crisp. Rarely exceed 20 words.

### Specific Documentation Rules
- **No "Overview" headings**: Content should flow directly from the metadata to an intro without a new heading
- **CRITICAL - All headings require introductory text**: Every heading must have at least one sentence before any subsections. Never place an h3 directly after an h2 without text between them. Never place an h4 directly after an h3 without text between them.
- **Section intros**: All headings must be followed by a minimal intro before starting subsections and/or lists
- **Basic numbering for procedures**: Use simple numbered steps (1, 2, 3) rather than Steps components
- **Lead-in sentences**: Every list must have an opening sentence introducing the content
- **Related Articles**: Always include as the last section unless completely irrelevant

## Platform-Specific Notes
- Visual Layer supports both cloud and on-premises deployments
- Chrome browser is recommended for optimal user experience
- API authentication uses JWT tokens with short expiration times
- Documentation includes video content and interactive examples
- Legacy fastdup documentation maintained in separate configuration
- for sections with subsections, there should never be any concluding or summary paragraphs at the end of the last subsection that are related to summaries of the entire main section. instead, all summaries, conclusions, etc. should be part of the intro to the main section.
- lists with more than 2 items should always use unordered lists even if they also make sense as part of prose paragraphs.
- `<Frame>`
  <img src="/images/highlight-filters-and-insights.png" />
`</Frame>`  this is the way to wrap images always

# Mintlify documentation

## Working relationship
- You can push back on ideas-this can lead to better documentation. Cite sources and explain your reasoning when you do so
- ALWAYS ask for clarification rather than making assumptions
- NEVER lie, guess, or make up information

## Project context
- Format: MDX files with YAML frontmatter
- Config: docs.json for navigation, theme, settings
- Components: Mintlify components

## Content strategy
- Prioritize accuracy and usability. No lengthy explanations or excessive enthusiasm.
- Treat content as evergreen. Avoid time-based statements unless writing release notes.
- Search existing content before adding new material. Avoid duplication unless strategic.
- Check existing patterns for consistency. Match established style.
- Start with the smallest reasonable changes. Respect what works.
- State capabilities as facts. Let functionality speak for itself.
- Organize by user action, not technical capability. Focus on what users do.

## docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

## API documentation 
Always consult with the following support articles from Mintlify if necessary to ensure structure, and integrity of content. Following are the primary but NOT the ONLY pages that you should consult with: 
https://www.mintlify.com/docs/guides/migrating-from-mdx.md
https://www.mintlify.com/docs/api-playground/overview
https://www.mintlify.com/docs/api-playground/openapi-setup
https://www.mintlify.com/docs/api-playground/managing-page-visibility
https://www.mintlify.com/docs/api-playground/multiple-responses
https://www.mintlify.com/docs/api-playground/mdx-setup 



## Writing standards
- **Voice**: Second person ("you"), active voice. Address users directly.
- **Tone**: Confident and efficient. State facts, not possibilities.
- **Sentences**: Short and declarative. Rarely exceed 20 words.
- **Language**: Minimalist. No decorative language, jargon, or marketing hyperbole.
- **Approach**: Embed value in descriptions. Combine what features are with why they matter.
- **Prerequisites**: Include at start of procedural content.
- **Testing**: Test all code examples before publishing.
- **Consistency**: Match style and formatting of existing pages.
- **Use Cases**: Include both basic and advanced use cases.
- **Lists**: Use ordered lists only when order matters.
- **Code Blocks**: Include language tags on all code blocks.
- **Images**: Include alt text on all images.
- **Links**: Use relative paths for internal links.

## Git workflow
- NEVER use --no-verify when committing
- Ask how to handle uncommitted changes before starting
- Create a new branch when no clear branch exists for changes
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

## Do not
- NEVER skip frontmatter on any MDX file
- NEVER use absolute URLs for internal links
- NEVER include untested code examples
- Make assumptions - always ask for clarification!!!!