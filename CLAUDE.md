# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the Visual Layer documentation repository built with Mintlify. Visual Layer is a computer vision platform for managing and analyzing visual datasets at scale. The documentation covers:

- Platform guides for creating, managing, and exploring datasets
- API reference for programmatic access
- On-premises deployment instructions
- Integration guides for external services

## Architecture & Structure

### Documentation Framework
- **Framework**: Mintlify documentation platform
- **Content Format**: MDX files with YAML frontmatter
- **Configuration**: `docs.json` for navigation, theme, and site settings
- **Components**: Mintlify-specific components (Card, Steps, Tip, etc.)

### Content Organization
```
docs/                          # Main documentation content
├── getting-started/           # Introduction and quick start guides
├── Creating-Datasets/         # Dataset creation and annotation import
├── Managing-Datasets/         # Dataset operations (save, share, export)
├── Exploring-datasets/        # Search, filtering, and quality analysis
├── Dataset-Enrichment/        # AI model-based data enhancement
├── on-prem/                   # On-premises installation guides
└── Integrations/              # External service integrations

api-reference/                 # API documentation
fastdup_docs_old/             # Legacy fastdup documentation
changelog/                     # Release notes
```

### Key Configuration Files
- `docs.json` - Main Mintlify configuration with navigation structure
- `fastdup-docs.json` - Configuration for legacy fastdup docs tab
- `README.md` - Developer setup instructions for Mintlify CLI

## Common Development Tasks

### Local Development
```bash
# Install Mintlify CLI globally
npm install -g mintlify

# Start development server
mintlify dev

# Start on custom port
mintlify dev --port 3333
```

### Content Guidelines (from existing docs/claude.md)
- Use second-person voice ("you")
- Include prerequisites at start of procedural content
- Test all code examples before publishing
- Match style and formatting of existing pages
- Use relative paths for internal links
- Language tags on all code blocks
- Alt text on all images

### Frontmatter Requirements
All MDX files must include:
```yaml
---
title: "Clear, descriptive page title"
description: "Concise summary for SEO/navigation"
---
```

### Git Workflow Rules
- NEVER use `--no-verify` when committing
- Ask about uncommitted changes before starting work
- Create new branch when no clear branch exists
- Commit frequently throughout development
- NEVER skip or disable pre-commit hooks

## Content Strategy
- Document just enough for user success - not too much, not too little
- Prioritize accuracy and usability
- Search for existing information before adding new content to avoid duplication
- Check existing patterns for consistency
- Start by making the smallest reasonable changes
- Make content evergreen when possible

## Custom Styling
The repository includes extensive custom styling in `styles.css` that defines:

### Brand Elements
- **Colors**: Primary brand color `#0097D9` used throughout
- **Typography**: Custom Roboto font family with specific weights and letter spacing
- **Gradient**: Brand gradient `linear-gradient(90deg, rgba(167,56,149,1) 0%, rgba(0,152,217,1) 50%, rgba(41,183,135,1) 100%)`

### Custom Components
- **Hero sections**: Background images and responsive layouts
- **Search bar**: Custom styling with backdrop blur effects
- **API grid**: Responsive grid layout for API reference cards
- **Tables**: Multiple table styles (integration-table, flow-table, etc.) with specific formatting
- **Dark mode**: Comprehensive dark mode support with CSS variables

### Layout Features
- **Responsive design**: Mobile-first approach with breakpoints at 768px and 996px
- **Footer customizations**: Custom email display and social icons
- **Navigation**: Custom dropdown styling and primary button design

When creating new content, refer to existing CSS classes and maintain visual consistency with the established design system.

## Technical Writing Standards

### Core Principles
- **Clarity First**: Explain the why before the how. Prioritize understanding over thoroughness
- **Audience Awareness**: Tailor tone and technical detail to user role (Data Scientist, Developer, Platform Admin)
- **Consistency**: Use the same format and terms across articles
- **Plain Language**: Direct, scannable communication that breaks complex information into digestible chunks
- **Visual-First**: Use diagrams, screenshots, and callouts to enhance understanding

### Writing Style
- **Voice**: Active voice, present tense, second person ("you")
- **Platform Naming**: "Visual Layer" (never "visual layer" or "Visual Layer Platform")
- **Tone**: Direct, professional, explaining technical concepts to knowledgeable colleagues
- **Structure**: Front-load key information, use hierarchical headings
- **Language**: US English spelling and conventions
- **Prohibited**: Em dashes, emojis, unnecessary jargon, "please" in instructions

### Document Structure
Required flow for all documentation:
1. **Title**: Descriptive and specific
2. **Introduction**: What this guide covers and why it matters
3. **Prerequisites**: Required access, tools, or knowledge
4. **Steps/Main Content**: Clear, logical progression
5. **Summary/Outcomes**: What was accomplished, next steps
6. **Related Resources**: Internal links, APIs, tutorials

### Formatting Conventions

#### UI Elements and Actions
- **UI Elements**: Bold, exact match from interface (`**Save**`, `**Settings > Preferences**`)
- **Code/Commands**: Monospace blocks or inline backticks (`` `python3 process.py` ``)
- **Instructions**: Imperative verbs ("Click Save" not "Click the Save button")
- **Navigation**: Use > between menu items (`Settings > Preferences > General`)

#### Lists and Structure
- **Numbered Lists**: Sequential steps, prioritized items, procedures that must be followed in order
- **Bulleted Lists**: Collections where sequence doesn't matter, options, requirements
- **Parallel Structure**: Maintain grammatical consistency within lists
- **Capitalization**: First word of each list item, complete sentences end with periods

#### Headings and Titles
- **Tutorial/Instructional**: Use gerunds ("Creating your First Workflow")
- **Task-based**: Use imperatives ("Configure your workspace")
- **Conceptual**: Use nouns ("Workflow Components", "API Reference")
- **Hierarchy**: Maintain consistent grammatical structures across levels

### Content Guidelines

#### Prerequisites Section
Always include:
- Required accounts or roles
- Technical knowledge required
- System or environment dependencies
- Links to external setup resources

#### Code and Examples
- Use fenced code blocks with specified language
- Include expected output after relevant examples
- Test all code examples before publishing
- Use monospace for user input and file names

#### Error Messages
Follow three-part formula:
1. **Problem Statement**: What happened (clear, user-friendly language)
2. **Cause** (optional): Why it happened (only if helpful)
3. **Solution**: What to do next (specific action steps)

Example: "We couldn't save your file. Check if you have permission to save in this location."

#### Visual Elements
- **Screenshots**: PNG format, first screenshot should show entire screen
- **Callouts**: Use consistent visual indicators
  - Warning: Critical actions or consequences
  - Note: Additional helpful info
  - Tip: Shortcuts or suggestions
- **Alt Text**: Descriptive text for all images
- **Diagrams**: Include when describing complex flows

#### Numbers and Measurements
- Spell out numbers zero through nine
- Use numerals for 10 and above
- Include units of measurement where applicable
- Use commas in numbers over 999 (1,000)
- US date format (MM/DD/YYYY)
- 12-hour time format with AM/PM

#### Troubleshooting Content
Essential components:
1. **Problem Statement**: Clear description of what goes wrong
2. **Symptoms**: Observable signs of the issue
3. **Cause**: Why the problem occurs
4. **Solution**: Step-by-step resolution
5. **Prevention**: Tips to avoid future occurrences

### Document Structure Rules

#### Overview and Introduction
- **No "Overview" headings**: Content after the intro card should flow directly without a separate "Overview" heading
- **No "Key Features" sections**: Feature information should be integrated into the introduction or presented as tables/subsections
- **Consolidate introductory content**: All intro material should be together in short, flowing paragraphs without separate top-level headings

#### Procedures and Configuration
- **Use basic numbering for procedures**: Configuration sections should use simple numbered steps (1, 2, 3) rather than `<Steps>` components
- **Clear procedure titles**: Name procedure sections based on the action (e.g., "Configuring Visual Similarity Thresholds" not "Configuration Options")

#### Section Organization
- **Intro text for sections with subsections**: Every section that contains subsections must include introductory text after the main heading before the first subsection
- **Lead-in sentences for all lists**: Every ordered and unordered list must have an opening sentence that introduces what the list contains
- **Related Articles section**: When relevant, include a "Related Articles" section as the very last section with links to related documentation, minimally including other articles in the same documentation section

#### Examples
```markdown
## Best Practices

Optimize your implementation by following these recommended practices.

### Threshold Configuration

Apply these guidelines when setting up thresholds:

- First guideline
- Second guideline
```

### Quality Checklist
Before publishing any documentation:
- [ ] Follows document structure template
- [ ] Uses active voice and present tense
- [ ] Includes all required frontmatter (title, description)
- [ ] Tests all code examples and procedures
- [ ] Maintains parallel structure in lists
- [ ] Uses consistent terminology throughout
- [ ] Includes descriptive alt text for images
- [ ] Links use descriptive text (never "click here")
- [ ] Follows US English conventions
- [ ] No standalone "Overview" or "Key Features" headings
- [ ] All procedures use basic numbering (1, 2, 3)
- [ ] Every section with subsections has intro text
- [ ] Every list has a lead-in sentence
- [ ] Includes Related Articles section when relevant

## Platform-Specific Notes
- Visual Layer supports both cloud and on-premises deployments
- Chrome browser is recommended for optimal user experience
- API authentication uses JWT tokens with short expiration times
- Documentation includes video content and interactive examples
- Integrates with analytics (Amplitude, Google Analytics) and social platforms