# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Track Changes

Always update CHANGELOG.md with additions/removals from the sites.

## Repository Overview

This repo contains five separate static sites, all published via GitHub Pages from `main` with no build step — edit files and push to deploy:

| Site | Directory | Short URL |
|---|---|---|
| Front-door hub | `/` (root) | `https://aka.ms/agentresources` |
| Microsoft 365 Copilot Resources | `m365-copilot/` | `https://aka.ms/m365copilot/resources` |
| Copilot Studio Resources | `copilot-studio/` | `https://aka.ms/copilotstudio/resources` |
| Agent 365 Resources | `agent365/` | `https://aka.ms/agent365/resources` |
| Build AI Agents | `develop-agents/` | (no short URL yet; Clarity tag ID also still TODO) |

Each child site is self-contained with its own `index.html`, `assets/css/styles.css`, `assets/js/main.js`, `images/`, and `favicon.ico`. The `main.js` across all child sites is identical — keep them in sync when making logic changes.

## Child Site Architecture

Each resource hub (`agent365/`, `copilot-studio/`, `m365-copilot/`) follows the same pattern:

- **Sections** are collapsible `div.section-card` elements toggled by `button.section-header` (accordion); state is tracked via the `open` CSS class and `aria-expanded`.
- **Navigation** is a sticky `nav.nav-strip` with fragment links (`#section-id`) that scroll to and open the matching card via `hashchange` listener in `main.js`.
- **Search** filters `li` elements inside `.link-list` and `.session-grid` across all cards in real time, auto-expanding sections that have matches.
- **Analytics** uses Microsoft Clarity; each site has its own tag ID in an inline `<script>` in `<head>`.
- Content uses two list styles: `.link-list` for resource links and `.session-grid` for conference session badges.

## Root Front-Door Site

- `index.html` — hero + three product cards + footer; all content in one file
- `assets/css/styles.css` — CSS custom properties in `:root`; hero and footer share a dark star-field background with an animated aurora overlay (`auroraShift` keyframes on `::before`)
- Per-card color identities: blue (#0078d4) for M365 Copilot, purple for Copilot Studio, indigo for Agent 365

## Design System

Shared across all four sites:

- Primary brand blues: `--brand-deep` (#003d73), `--brand-mid` (#0061a4), `--brand-accent` (#0078d4)
- Font stack: `'Aptos', 'Segoe UI', system-ui`
