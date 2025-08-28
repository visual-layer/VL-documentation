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

1. **Overview Pages** (Getting Started style):
   - Brief introductory paragraph explaining the concept
   - Card components for organizing related content by theme
   - Clear navigation pathways to detailed sections
   - "Learn More" section with related links

2. **Concept Pages** (Definitions and Entities style):
   - Note callouts for important introductory information
   - Definition tables with custom styling classes
   - Two-column layout for terminology explanations
   - Comprehensive concept explanations with examples

3. **Tutorial Pages** (Quick Start style):
   - Prerequisites section listing required setup
   - Step-by-step numbered instructions with clear actions
   - Code examples in fenced code blocks
   - Progressive complexity building through sections

4. **Tutorial Hub Pages**:
   - Card group layouts for navigation
   - Each card with descriptive title and brief description
   - Clear visual organization for better user experience

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
- **Dark Mode**: Comprehensive dark mode support with CSS variables

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
- Include clear step-by-step instructions for tutorials
- Provide comprehensive concept explanations with examples
- Use custom CSS classes for consistent styling
- Embed videos and interactive content where helpful for complex procedures

## Visual Layer Documentation Standards

### Writing Guidelines
- **Voice**: Second person ("you"), active voice, present tense
- **Platform Naming**: "Visual Layer" (consistent capitalization)
- **Content Strategy**: Document just enough for user success - prioritize accuracy and usability
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
- **No "Overview" headings**: Content should flow directly without separate overview sections
- **Basic numbering for procedures**: Use simple numbered steps (1, 2, 3) rather than Steps components
- **Intro text for sections**: Every section with subsections must include introductory text
- **Lead-in sentences**: Every list must have an opening sentence introducing the content
- **Related Articles**: Include as the last section when relevant

## Platform-Specific Notes
- Visual Layer supports both cloud and on-premises deployments
- Chrome browser is recommended for optimal user experience
- API authentication uses JWT tokens with short expiration times
- Documentation includes video content and interactive examples
- Legacy fastdup documentation maintained in separate configuration
- for sections with subsections, there should never be any concluding or summary paragraphs at the end of the last subsection that are related to summaries of the entire main section. instead, all summaries, conclusions, etc. should be part of the intro to the main section.
- lists with more than 2 items should always use unordered lists even if they also make sense as part of prose paragraphs.
- How It Works and other similar high level explanations that include steps or process descriptiosn (empahsize high level/theory) must use the <Step> object for the steps and their descriptins. For How to Apply the Filter as an example, this section must use a regular ordered list, as it does now, but the final paragraph in this case explains benefits and should be the intro para to the process instead of a conclusions.
- always make sure capitalization is absolutely consistent across content types. so for example, prepositions in titles should ALWAYS be lower case.
- always double-check your work before finishing an implementation to ensure spacing is correct wherever you made changes. soemtimes spacing can be tricky when using ** ** mid-sentnece.
- always use active voice unless absolutely unavoidable. that includes preferring opening sentences with active simple present tense instead of gerunds.
- never use "please" and never use i.e. nor e.g. Only "For example" or "Example:". And always use correct punctuation including periods - even when in ordered lists.Finally, every article must ALWAYS open with an introduction - even if minimal.
- never use divider lines in the middle of articles unless you consult with me before starting.
- exception to title case for titles and headings: ensure that sidebarTitle always use sentence case and is always limited to 20 chars at most. This means that sometimes longer title needs to be shortened only for the sidebarTitle
- steps and processes must always use the formatting we noted in memory already - either ordered lists or <Step> depending on the kind of information and NEVER any other kind of formatting. For complex flows with sublevels (1. a. i. , 2. b. ii. etc.), this is still true, but you can use ** ** to emphasize stages for example.
