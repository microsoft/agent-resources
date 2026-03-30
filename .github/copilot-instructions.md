# Copilot Instructions

## Repository Overview

Five static sites published via GitHub Pages from `main` — no build step, no package manager. Edit and push to deploy.

| Site | Directory | URL |
|---|---|---|
| Front-door hub | `/` (root) | `https://aka.ms/airesources` |
| Microsoft 365 Copilot | `m365-copilot/` | `https://aka.ms/m365copilot/resources` |
| Copilot Studio | `copilot-studio/` | `https://aka.ms/copilotstudio/resources` |
| Agent 365 | `agent365/` | `https://aka.ms/agent365/resources` |
| Build AI Agents | `develop-agents/` | *(no short URL yet)* |
| Microsoft Foundry | `microsoft-foundry/` | *(no short URL yet)* |

## Architecture

### Child sites (agent365/, copilot-studio/, m365-copilot/, develop-agents/, microsoft-foundry/)

Each child site is self-contained with the same structure: `index.html`, `assets/css/styles.css`, `assets/js/main.js`, `images/`, and `favicon.ico`.

**The `main.js` across all child sites is identical — when changing JS logic, update all copies.**

The UI follows an accordion + search + deep-link pattern:

- **Sections** are collapsible `div.section-card` toggled by `button.section-header`. The `open` CSS class and `aria-expanded` attribute track state.
- **Navigation** is a sticky `nav.nav-strip` with `#fragment` links. The `hashchange` listener in `main.js` scrolls to and opens the target card.
- **Search** filters `li` elements in `.link-list` and `.session-grid` in real time, auto-expanding sections with matches.
- **Analytics** uses Microsoft Clarity with per-site tag IDs in an inline `<script>` in `<head>`.

Content uses two list styles: `.link-list` for resource links and `.session-grid` for conference session badges.

### Root site (/)

`index.html` is a hero + product cards + footer, all in one file. The CSS uses a dark star-field background with an animated aurora overlay (`auroraShift` keyframes on `::before`).

## Design System

- Brand colors: `--brand-deep` (#003d73), `--brand-mid` (#0061a4), `--brand-accent` (#0078d4)
- Per-card color identities: blue (#0078d4) for M365 Copilot, purple for Copilot Studio, indigo for Agent 365
- Font stack: `'Aptos', 'Segoe UI', system-ui`
- CSS custom properties defined in `:root` for colors, spacing, radii, shadows, transitions, and font sizes

## Key Conventions

- **No build system.** Plain HTML/CSS/JS only — no bundlers, transpilers, or package managers.
- **Keep `main.js` in sync.** All child sites share identical JS logic. After editing one, copy the file to the other child site directories.
- **Each site has its own Clarity tag.** Don't reuse tag IDs across sites.
- **Accordion state** is managed purely through the `open` class on `.section-card` — no hidden inputs or JS state objects.
