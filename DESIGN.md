# Design System — Agent Resources

## Product Context
- **What this is:** Five curated resource hub sites for the Microsoft Copilot/AI ecosystem — high-signal links organized by product, audience, and topic, maintained by the Microsoft Copilot Acceleration Team (CAT).
- **Who it's for:** Enterprise developers, architects, and IT pros building and deploying AI agents with Microsoft tools. The M365 Copilot site also serves end users adopting Copilot in their workflow.
- **Space/industry:** Microsoft ecosystem / enterprise AI / developer tooling
- **Project type:** Static resource hub / documentation aggregator (plain HTML/CSS/JS, no build system)
- **Memorable thing:** "This is the definitive place for information I need and trust."

---

## Aesthetic Direction
- **Direction:** Editorial/Utilitarian — information as the hero. The content IS the product: curated links, organized sections, fast retrieval. No decoration that doesn't earn its presence.
- **Decoration level:** Intentional — the root hub's dark dot-grid + aurora overlay is the signature decoration (keep it). Child sites use per-product color accents as the sole expressive element.
- **Mood:** "A senior engineer's well-organized reference library." Confident. Dense but not cluttered. Authoritative without being corporate. Practitioner-made, not marketing.
- **Positioning:** Deliberately NOT learn.microsoft.com — that's official documentation. This is practitioner-curated. The design should signal that distinction.
- **Reference sites:** developer.microsoft.com (studied), docs.github.com (studied), developers.cloudflare.com (studied), learn.microsoft.com (studied)

---

## Typography

- **Display / Hero headings:** [Plus Jakarta Sans](https://fonts.google.com/specimen/Plus+Jakarta+Sans) — geometric, modern, similar DNA to Segoe UI but with personality at large sizes. Not overused in Microsoft's ecosystem. Weights 600, 700, 800.
- **Body:** Aptos, Segoe UI, system-ui, -apple-system, sans-serif — exactly right for the Microsoft-device-heavy audience; renders perfectly on Windows without a CDN call.
- **UI labels / section headers / buttons:** Plus Jakarta Sans 500–700
- **Monospace / URLs / code:** [Geist Mono](https://fonts.google.com/specimen/Geist+Mono) 400–500
- **Loading strategy:** One `<link rel="preconnect" href="https://fonts.googleapis.com">` + one `<link>` for Plus Jakarta Sans and Geist Mono per site. Aptos/Segoe UI requires no CDN.

### Type Scale

| Token | Size | Role |
|-------|------|------|
| `--text-xs` | 0.7rem (11.2px) | Labels, caps, metadata |
| `--text-sm` | 0.8rem (12.8px) | Small body, table rows, code |
| `--text-base` | 0.935rem (14.9px) | Body copy, link descriptions |
| `--text-md` | 1rem (16px) | Lead body, nav items |
| `--text-lg` | 1.1rem (17.6px) | Card titles |
| `--text-xl` | 1.25rem (20px) | Subsection headers |
| `--text-2xl` | 1.5rem (24px) | Section card titles |
| `--text-3xl` | 1.875rem (30px) | Page H1 |
| `--text-4xl` | 2.25rem (36px) | Hero display |

### Font Stack in CSS

```css
--font-display: 'Plus Jakarta Sans', 'Aptos', 'Segoe UI', system-ui, sans-serif;
--font-body: 'Aptos', 'Segoe UI', system-ui, -apple-system, sans-serif;
--font-mono: 'Geist Mono', 'Cascadia Code', 'Consolas', monospace;
```

### Typographic Hierarchy Rules
- Hero titles: Plus Jakarta Sans 800, letter-spacing -0.02em, line-height 1.08
- Section card headers: Plus Jakarta Sans 700, letter-spacing -0.01em
- Body: Aptos 400, line-height 1.65
- UI labels: Plus Jakarta Sans 700, letter-spacing 0.06em, uppercase, 11.2px
- All-caps labels ONLY for nav/UI chrome — never for body content

---

## Color

### Root Hub
The root hub stays dark. The dot-grid + aurora overlay is the site's visual signature.

```css
--surface-dark: #0d1b35;
--aurora-teal:  rgba(0,180,200,.12);
--aurora-blue:  rgba(0,100,160,.10);
```

### Child Site Surfaces (warm neutral — not pure white)
```css
--surface:       #fafaf8;   /* warm off-white — signals human-crafted */
--surface-alt:   #f0f0ee;   /* section backgrounds, search bar */
--surface-hover: #e8e8e6;   /* hover states */
```

### Per-Product Color Identity

Each child site overrides `--brand-deep`, `--brand-mid`, `--brand-accent` with its product tokens. The section header dot, nav active indicator, and link accent all use `--brand-accent`.

| Site | Deep | Mid | Accent | Light |
|------|------|-----|--------|-------|
| **M365 Copilot** | `#003d73` | `#0061a4` | `#0078d4` | `#50e6ff` |
| **Copilot Studio** | `#3b1f8e` | `#6344c5` | `#b4a7e5` | `#e9e4ff` |
| **Agent 365** | `#005e50` | `#007a6d` | `#4fd1c5` | `#b2f5ea` |
| **Develop Agents** | `#004578` | `#005a9e` | `#a0c8f0` | `#dbeeff` |
| **Microsoft Foundry** | `#4a1942` | `#7a3173` | `#e879c0` | `#fce4f6` |

> **Rule:** Each site sets `--brand-deep`, `--brand-mid`, `--brand-accent` in its `:root`. All shared components inherit from these tokens. Never hardcode product colors in shared components.

### Text
```css
--text:        #0d1117;   /* primary — near-black, not pure black */
--text-muted:  #4a5568;   /* secondary, descriptions */
--text-subtle: #718096;   /* metadata, placeholder, timestamps */
--text-on-dark:#e8f4fd;   /* on dark hero surfaces */
```

### Borders
```css
--border:        #dededc;   /* default — warm (matches warm neutral surface) */
--border-strong: #c0c0bc;   /* emphasized borders, input fields */
```

### Semantic Colors
```css
--success: #107c10;   /* GA / confirmed / active */
--warning: #ffaa44;   /* preview / beta / caution */
--error:   #c42b1c;   /* deprecated / unavailable / danger */
--info:    #0078d4;   /* informational — same as M365 accent */
```

### Dark Mode
Dark mode reduces saturation 10–15%. Surfaces flip to near-black; text flips to near-white. Per-product accent colors stay the same (they're already saturated enough to read on dark).

```css
[data-theme="dark"] {
  --surface:       #111110;
  --surface-alt:   #1c1c1a;
  --surface-hover: #262624;
  --text:          #f0f0ee;
  --text-muted:    #a0a098;
  --text-subtle:   #6a6a64;
  --border:        #2a2a28;
  --border-strong: #3a3a38;
}
```

---

## Spacing

- **Base unit:** 8px
- **Density:** Comfortable — content-dense but scannable; accordion list items get enough vertical breathing room to distinguish entries

```css
--space-1:  4px;   /* micro gaps, icon padding */
--space-2:  8px;   /* tight component gaps */
--space-3:  12px;  /* badge gaps, small padding */
--space-4:  16px;  /* default component padding */
--space-5:  20px;  /* card padding, section body padding */
--space-6:  24px;  /* section gaps */
--space-7:  32px;  /* between sections */
--space-8:  40px;  /* hero padding sides */
--space-9:  48px;  /* page section padding */
--space-10: 64px;  /* top-level page padding */
```

---

## Layout

- **Approach:** Grid-disciplined — strict content max-width, predictable accordion column, responsive collapse
- **Max content width:** 1120px
- **Max hero inner width:** 800px (text column)
- **Breakpoints:** Mobile first; primary breakpoint at 768px (stack accordion, collapse nav)
- **Border radius scale:**
  ```css
  --radius-sm: 6px;    /* buttons, inputs, badges */
  --radius:    10px;   /* section cards, alert boxes */
  --radius-lg: 16px;   /* mockup shells, major containers */
  ```
- **Shadow scale:**
  ```css
  --shadow-sm: 0 1px 2px rgba(0,0,0,.05);
  --shadow-md: 0 3px 12px rgba(0,0,0,.07);
  --shadow-lg: 0 8px 28px rgba(0,0,0,.10);
  ```

### Child Site Layout Structure
1. **Hero** — flat dark background (product `--brand-deep` or near-black), left-aligned text, bottom border in `--brand-accent` (3px). No gradient.
2. **Nav strip** — sticky, white background, horizontal fragment links, active state = product `--brand-accent` bottom border.
3. **Search bar** — `--surface-alt` background, full-width input, result count.
4. **Content** — accordion `div.section-card` with section dot in product `--brand-accent`.
5. **Footer** — minimal, dark.

---

## Motion

- **Approach:** Minimal-functional — only transitions that aid comprehension of state changes.
- **Easing:**
  - Enter: `cubic-bezier(0,0,.2,1)` (ease-out)
  - Exit: `cubic-bezier(.4,0,1,1)` (ease-in)
  - Move: `cubic-bezier(.4,0,.2,1)` (ease-in-out)
- **Duration:**
  - Micro (color/border): 100ms
  - Short (hover state, icon): 180ms (`--transition: .18s cubic-bezier(.4,0,.2,1)`)
  - Medium (accordion expand): 250ms
  - Long (page-level): 350ms
- **Reduced motion:** `@media (prefers-reduced-motion: reduce)` — disable all transforms and transitions. Already in place; do not remove.
- **Anti-patterns to avoid:** Scroll-triggered animations, entrance animations on list items, decorative looping animations (only the root aurora is exempt, it's the brand moment).

---

## Hero Pattern — Child Sites

Replace gradient heroes with flat dark headers. A gradient reads as a framework default; a flat dark header with a product-color accent reads as a deliberate decision.

```html
<div class="hero">
  <!-- hero gets background: var(--brand-deep) + bottom-border: 3px solid var(--brand-accent) -->
  <div class="breadcrumb">...</div>
  <h1 class="hero-title">...</h1>
  <p class="hero-sub">...</p>
  <span class="hero-tag">...</span>
</div>
```

```css
.hero {
  background: var(--brand-deep);
  border-bottom: 3px solid var(--brand-accent);
  padding: 32px 40px 28px;
  color: #ffffff;
}
/* No .hero::before gradient overlay for child sites */
```

The root hub is exempt — it keeps the dot-grid + aurora because that's the front door visual signature.

---

## Component Patterns

### Section card dot
Each accordion section header has a small colored dot (`8px circle`) in `--brand-accent`. This is the per-product identity signal within the content — subtle but consistent.

### Link list entries
`.link-list li` structure: title (product link color) + description (muted body text) + tags (badges). Entries get `11px` minimum vertical padding top/bottom. Hover: `--surface-alt` background.

### Nav strip active state
Active nav item: `color: --brand-accent`, `border-bottom: 2px solid --brand-accent`, `font-weight: 600`.

### Badges
Use semantic badge variants for resource type tagging. Never use color alone — always pair with a text label.

---

## Decisions Log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-06-05 | Plus Jakarta Sans added as display/heading font | Breaks all-Aptos uniformity; creates typographic hierarchy; not overused in Microsoft ecosystem |
| 2026-06-05 | Warm neutral `#fafaf8` surface replaces pure white | Signals human-crafted; subtle differentiation from generic Microsoft properties |
| 2026-06-05 | Flat dark heroes replace gradient heroes | Gradient reads as AI UI kit default; flat dark with product-color border accent reads as deliberate |
| 2026-06-05 | Per-product color system systematized (5 products × 4 tokens) | Establishes consistent identity per site without shared stylesheet changes |
| 2026-06-05 | Root hub dark aesthetic preserved | It's a differentiator from learn.microsoft.com — keep it |
| 2026-06-05 | Initial design system created | /design-consultation based on codebase research + competitive analysis of 5 sites + user memorable-thing answer |
