# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the **Visual Layer Documentation Website** - a comprehensive documentation platform built with Mintlify for Visual Layer's computer vision and dataset management platform. The repository contains technical documentation, API references, deployment guides, and user manuals for Visual Layer's visual dataset analysis platform.

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

**Main Documentation Sections**:
- `/docs/getting-started/` - Introduction, quick start guides, and platform orientation
- `/docs/Creating-Datasets/` - Dataset creation, annotation import, and custom metadata
- `/docs/Managing-Datasets/` - Dataset operations (save, share, export, metadata management)
- `/docs/Exploring-datasets/` - Search, filtering, quality analysis, and data exploration
- `/docs/Dataset-Enrichment/` - AI model-based data enhancement and analysis
- `/docs/on-prem/` - On-premises installation and configuration guides
- `/docs/Integrations/` - External service integrations (S3, GCS, etc.)
- `/api-reference/` - REST API documentation with authentication and endpoints
- `/changelog/` - Release notes and version history

**Documentation Structure**: Content is organized hierarchically with clear navigation paths and consistent file naming conventions.

### Content Standards & Patterns

**Front Matter Structure** (based on established documentation standards):
```yaml
---
title: "Page Title"                 # Full descriptive title
description: "Brief description"    # SEO and page description
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
   - Use the <Step> object for these procedures. Make sure outcomes are on new lines but part of the step that led to the outcome 
   - Code examples in fenced code blocks


### Mintlify Configuration

Key configuration in `docs.json` and `fastdup-docs.json`:
- **Theme**: Custom Visual Layer branding with primary color `#0097D9`
- **Navigation**: Tab-based structure with grouped pages
- **Features**: Custom styling, interactive components
- **Legacy Integration**: Separate fastdup documentation configuration

### Assets Organization
- `/images/` - Screenshots, videos, and diagrams organized by feature
- `/favicon.png` and `/favicon.svg` - Brand assets for site favicon
- `/api-reference/openapi.json` - OpenAPI specification for REST API
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
- Use MDX components (Card, Steps, Tip, Note) for enhanced user experience
- Follow established front matter structure for metadata consistency
- Provide comprehensive concept explanations with examples
- Create mermaid designs when appropriate to assist in conceptual content
- Use videos and interactive content where helpful for complex procedures 
- always make sure capitalization is absolutely consistent across content types. so for example, prepositions in titles should ALWAYS be lower case.
- always double-check your work before finishing an implementation to ensure spacing is correct wherever you made changes. sometimes spacing can be tricky when using ** ** mid-sentnece.
- always use active voice unless **absolutely** unavoidable. that includes preferring opening sentences with active simple present tense instead of gerunds.
- never use "please" and never use i.e. nor e.g. Only "For example" or "Example:". And always use correct punctuation including periods - even when in ordered lists.Finally, every article must ALWAYS open with an introduction - even if minimal.
- never use divider lines in the middle of articles unless you consult with me before starting.
- exception to title case for titles and headings: ensure that sidebarTitle always use sentence case and is always limited to 20 chars at most. This means that sometimes longer title needs to be shortened only for the sidebarTitle

## Visual Layer Documentation Standards

### Writing Guidelines
- **Voice**: Second person ("you"), active voice, present tense
- **Platform Naming**: "Visual Layer" (consistent capitalization)
- **Content Strategy**: Always prioritize accuracy and usability
- **Structure**: Include prerequisites, clear step-by-step instructions, and related resources
- **Format**: Use relative paths for internal links, language tags on code blocks, alt text on images

### Git Workflow Requirements
- NEVER use `--no-verify` when committing
- Ask about uncommitted changes before starting work
- Create new branch when no clear branch exists
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

### Documentation Quality Standards
- Test all code examples before publishing
- Match style and formatting of existing pages
- Search for existing information before adding new content to avoid duplication
- Check existing patterns for consistency
- Start by making the smallest reasonable changes
- Make content evergreen when possible

### Specific Documentation Rules
- **No "Overview" headings**: Content should flow directly from the metadata to an intro without a new heading 
- **Section intros**: All headings must be followed by a minimal intro before starting subsections and/or lists
- **Basic numbering for procedures**: Use simple numbered steps (1, 2, 3) rather than Steps components
- **Intro text for sections**: Every section with subsections must include introductory text
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
- <Frame>
  <img src="/images/highlight-filters-and-insights.png" />
</Frame>  this is the way to wrap images always

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
- Prioritize accuracy and usability of information
- All content should be treated as evergreen, avoiding time-based statements and/or discussion of past, current, recent or future versions, releases, etc. unless writing release notes and/or unless requested to add a non-standard Note
- Search for existing information before adding new content. Avoid duplication unless it is done for a strategic reason
- Check existing patterns for consistency
- Start by making the smallest reasonable changes

## docs.json

- Refer to the [docs.json schema](https://mintlify.com/docs.json) when building the docs.json file and site navigation

## Frontmatter requirements for pages
- title: Clear, descriptive page title
- description: Concise summary for SEO/navigation

## Writing standards
- Second-person voice ("you")
- Prerequisites at start of procedural content
- Test all code examples before publishing
- Match style and formatting of existing pages
- Include both basic and advanced use cases
- Use ordered lists and/or steps only when the order has impact/significance
- Language tags on all code blocks
- Alt text on all images
- Relative paths for internal links

## Git workflow
- NEVER use --no-verify when committing
- Ask how to handle uncommitted changes before starting
- Create a new branch when no clear branch exists for changes
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

## Do not
- Skip frontmatter on any MDX file
- Use absolute URLs for internal links
- Include untested code examples
- Make assumptions - always ask for clarification