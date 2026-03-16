# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a static front-door website that links to three Microsoft AI resource hubs:

- **Microsoft 365 Copilot** → `https://aka.ms/m365copilot/resources`
- **Copilot Studio** → `https://aka.ms/copilotstudio/resources`
- **Agent 365** → `https://aka.ms/agent365/resources`

The site is published via GitHub Pages from the `main` branch. There is no build step — editing files and pushing to `main` is all that's needed to deploy.

## File Structure

- `index.html` — the entire page (hero, three cards, footer)
- `assets/css/styles.css` — all styles; uses CSS custom properties defined in `:root`
- `images/` — product icons (`copilot-icon.png`, `copilot-studio-icon.png`, `agent365-icon.png`)
- `favicon.ico` — multi-size (16/32/48px) robot face icon generated with Pillow

## Design System

The visual design mirrors the three child resource sites. Key tokens in `:root`:

- Primary brand blues: `--brand-deep` (#003d73), `--brand-mid` (#0061a4), `--brand-accent` (#0078d4)
- Font stack: `'Aptos', 'Segoe UI', system-ui`
- Each card has a per-product color identity (blue for M365 Copilot, purple for Copilot Studio, indigo for Agent 365)

The hero uses a dark star-field pattern (`#0d1b35` base + 1px dot grid) with an animated CSS aurora overlay (`::before` with `auroraShift` keyframes). The footer uses the same background treatment.

## Regenerating the Favicon

```bash
python3 -c "
from PIL import Image, ImageDraw
# ... draw robot face at 16/32/48px sizes
frames[0].save('favicon.ico', format='ICO', sizes=[(s,s) for s in [16,32,48]], append_images=frames[1:])
"
```

Pillow is required (`pip install Pillow`).
