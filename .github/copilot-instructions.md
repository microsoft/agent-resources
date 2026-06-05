# Copilot Instructions

## Repository Overview

Five static sites published via GitHub Pages from `main` — no build step, no package manager. Edit and push to deploy.

| Site                  | Directory            | URL                                      |
| --------------------- | -------------------- | ---------------------------------------- |
| Front-door hub        | `/` (root)           | `https://aka.ms/agentresources`          |
| Microsoft 365 Copilot | `m365-copilot/`      | `https://aka.ms/m365copilot/resources`   |
| Copilot Studio        | `copilot-studio/`    | `https://aka.ms/copilotstudio/resources` |
| Agent 365             | `agent365/`          | `https://aka.ms/agent365/resources`      |
| Build AI Agents       | `develop-agents/`    | `https://aka.ms/agent-development/resources`                     |
| Microsoft Foundry     | `microsoft-foundry/` | `https://aka.ms/foundry/resources`                   |

## Track Changes

Always update CHANGELOG.md with additions/removals from the sites. When updating CHANGELOG.md, make sure there is a newline between the header and the paragraph text. Each site has its own CHANGELOG.md file to track its changes, with all changes for all sites aggregated into the root CHANGELOG.md with dated entries grouped by site directory.

## Architecture

### Child sites (agent365/, copilot-studio/, m365-copilot/, develop-agents/, microsoft-foundry/)

Each child site is self-contained with the same structure: `index.html`, `assets/css/styles.css`, `images/`, and `favicon.ico`.

**All five child sites share a single `assets/js/main.js` at the repo root** (referenced as `../assets/js/main.js`). Edit it once and every site picks up the change.

The UI follows an accordion + search + deep-link pattern:

- **Sections** are collapsible `div.section-card` toggled by `button.section-header`. The `open` CSS class and `aria-expanded` attribute track state.
- **Navigation** is a sticky `nav.nav-strip` with `#fragment` links. The `hashchange` listener in `main.js` scrolls to and opens the target card.
- **Search** filters `li` elements in `.link-list` and `.session-grid` in real time, auto-expanding sections with matches.
- **Analytics** uses Microsoft Clarity with per-site tag IDs in an inline `<script>` in `<head>`.

Content uses two list styles: `.link-list` for resource links and `.session-grid` for conference session badges.

### Root site (/)

`index.html` is a hero + product cards + footer, all in one file. The CSS uses a dark star-field background with an animated aurora overlay (`auroraShift` keyframes on `::before`).

## Design System

**Always read `DESIGN.md` before making any visual or UI decisions.**
All font choices, colors, spacing, and aesthetic direction are defined there.
Do not deviate without explicit user approval. In QA mode, flag any code that doesn't match `DESIGN.md`.

- Brand colors: `--brand-deep` (#003d73), `--brand-mid` (#0061a4), `--brand-accent` (#0078d4)
- Per-product color identities: M365 blue, Studio purple, Agent 365 teal-green, Develop Agents steel blue, Foundry plum — each site sets its own `--brand-deep/mid/accent` tokens in `:root`
- Display/heading font: `'Plus Jakarta Sans'` (Google Fonts, weights 600/700/800) — loaded via CDN, falls back to Aptos
- Body font stack: `'Aptos', 'Segoe UI', system-ui`
- Monospace font: `'Geist Mono'` (Google Fonts) — for URLs, code, and data
- Child site surface color: `#fafaf8` (warm neutral, not pure white)
- CSS custom properties defined in `:root` for colors, spacing, radii, shadows, transitions, and font sizes

## Key Conventions

- **No build system.** Plain HTML/CSS/JS only — no bundlers, transpilers, or package managers.
- **Shared `main.js`.** All five child sites reference a single `../assets/js/main.js` at the repo root. Edit that one file; do not reintroduce per-site copies.
- **Each site has its own Clarity tag.** Don't reuse tag IDs across sites.
- **Accordion state** is managed purely through the `open` class on `.section-card` — no hidden inputs or JS state objects.
