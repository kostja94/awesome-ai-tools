# Contributing to Awesome AI Tools

> Product facts are maintained in AI Product Registry. This repository maintains the curated inclusion set, categories, and order in `catalog/selection.yaml`; `README.md`, `README-CN.md`, and `INDEX.md` are generated outputs. New submissions must be matched to a verified Registry entity before publication.

Thank you for your interest in contributing to Awesome AI Tools! This document provides guidelines and instructions for contributing.

Section reading context is maintained only in `catalog/section-guides.yaml`, keyed by stable selection section ID, and rendered automatically. Use short contextual sentences with descriptive anchors to matching Alignify articles, not generic calls to visit or copied article summaries. English output links English articles; Chinese output links `/zh/` articles, with no cross-language fallback. Omit a locale when no matching article exists. Verify the article body and route in the local Alignify deployment before adding a link; this is editorial reading context, not a Registry fact source. When splitting or renaming section IDs, explicitly review these mappings; `catalog.py check` rejects orphaned mappings. Do not edit generated READMEs to maintain these links.

## How to Contribute

### Option 1: Submit via GitHub Issue (Recommended)

1. **Check if the product already exists**
   - Search the README.md and INDEX.md to ensure the product hasn't been added
   - Search AI Product Registry and identify the stable `registry_id`

2. **Create a new Issue**
   - Go to the [Issues](https://github.com/kostja94/awesome-ai-tools/issues) page
   - Click "New Issue"
   - Use the title format: `Add: [Product Name]`
   - Include the following information:
     - Product name
     - Website URL
     - Section (from the current README table of contents)
     - Provider/Company name
     - Brief description (1-2 sentences, including notable model versions if relevant)

3. **Wait for review**
   - The maintainer will review and add the product to the repository

### Option 2: Contact via Email

If you prefer to contact directly, please email: **zyjstc@gmail.com**

Include the same information as listed in Option 1.

### Formatting Guidelines

When submitting a product, please follow this format:

- **Product Name**: [Name without version numbers; model/product line name only]
- **Website**: [URL]
- **Section**: [Section from the README table of contents]
- **Provider**: [Company/Provider Name]
- **Description**: [Brief 1-2 sentence description; current model versions belong here, not in the name]

### Sections

The catalog is organized into 22 groups with 49 sections — see the table of
contents in [README.md](README.md) for the current, authoritative list (Models,
Agent Development Infrastructure, Coding & App Development, Image & Design,
Video & Filmmaking, Voice/Speech/Audio, Search & Web Data, Data & AI
Infrastructure, Productivity & Knowledge, and more, down to vertical and
discovery sections).

Naming rules:

- Model entries are listed by family or product line (e.g. `Qwen Coder`,
  `GPT Image`, `Nano Banana`); version numbers live in the description.
- Platform and application entries belong in their application section, not in
  the Models sections; hosted third-party model endpoints are not listed as
  separate model families.
- Within a section, better-known products are listed first.

### Code of Conduct

- Be respectful and constructive
- Provide accurate information
- Follow the project's formatting guidelines
- Ensure all links are valid and accessible

## Questions?

If you have questions about contributing, please open a [GitHub Issue](https://github.com/kostja94/awesome-ai-tools/issues) or contact the maintainer via email: **zyjstc@gmail.com**

Thank you for contributing! 🎉

