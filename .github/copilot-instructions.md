# Copilot Instructions for nightplinkers.com

## Project Overview

This repository contains the website for **Night Plinkers** — an airgun safety documentation and compliance consulting business. The site serves manufacturers, importers, distributors, and retailers who need safety documentation, manual reviews, and regulatory compliance help for airgun products.

## Tech Stack

- **Pure static HTML/CSS** — a single `index.html` file with all styles inlined in a `<style>` block.
- No build tools, bundlers, or package managers.
- No JavaScript frameworks or dependencies.
- Designed to be drop-in compatible with GoDaddy Websites + Marketing HTML sections.

## Code Conventions

- All CSS class names use the `np-` prefix (e.g., `np-wrap`, `np-btn`, `np-card`).
- Styles live inside a `<style>` block in `<head>` — do not create external stylesheets.
- Use semantic HTML5 elements (`<main>`, `<section>`, `<aside>`, `<nav>`, `<form>`) with ARIA attributes for accessibility.
- Focusable interactive elements must have a visible focus style (`:focus { outline: 2px solid #32ff6a; outline-offset: 2px }`).
- Color palette: dark background `#0b0f14`, body text `#e7eef7`, muted text `#a9b7c6`, accent green `#32ff6a`, accent blue `#00c7ff`, card borders `#1f2a36`.
- Responsive breakpoint at `max-width: 900px` — switch grid layouts to single-column.
- External links must include `target="_blank" rel="noopener noreferrer"`.

## Content Domains

- **Services**: Safety Update/Insert/Quick-Start Card, Manual Review & Edit, Importer Compliance Review/Edit/Insert.
- **Platforms**: CO₂, Pre-Charged Pneumatic (PCP), Spring-Piston, Multi-Pump Pneumatic.
- **Markets**: US, UK, EU.
- Contact email: `nightplinkers@gmail.com`.

## Testing & Validation

There is no automated test suite. Validate changes by:
1. Opening `index.html` directly in a browser.
2. Checking layout at both desktop (≥900 px) and mobile (<900 px) viewport widths.
3. Verifying all internal anchor links (`#np-contact`, `#np-sample`) scroll correctly.
4. Confirming the contact form "Generate Email" button opens a pre-populated `mailto:` link.
5. Running the HTML through the [W3C Markup Validator](https://validator.w3.org/) for any structural issues.
