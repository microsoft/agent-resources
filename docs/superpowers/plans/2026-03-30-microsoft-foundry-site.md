# Microsoft Foundry Resource Site — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create `microsoft-foundry/` as a fully-populated child resource site with 11 accordion sections, cobalt blue color identity, and curated links — matching the structure of the other four child sites.

**Architecture:** Static HTML/CSS/JS, no build step. A single `index.html` holds all content. `styles.css` is derived from `agent365/assets/css/styles.css` with cobalt-blue tokens replacing the indigo/blue ones. `main.js` is an identical copy of the shared accordion + hash-nav + search script (per CLAUDE.md — keep all copies in sync). Push to `main` to deploy via GitHub Pages.

**Tech Stack:** HTML5, CSS custom properties, vanilla JS (no frameworks, no build tools)

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `microsoft-foundry/index.html` | Create (overwrite 1-line placeholder) | All site content: head, hero, nav, 11 sections, footer |
| `microsoft-foundry/assets/css/styles.css` | Create | Cobalt blue identity; layout identical to other sites |
| `microsoft-foundry/assets/js/main.js` | Create (copy) | Accordion, hash-nav, search — identical to other sites |
| `microsoft-foundry/favicon.ico` | Create (copy) | Placeholder favicon until Foundry-specific one is available |
| `microsoft-foundry/images/` | Create (empty dir) | Placeholder for future og-image, header image |

---

### Task 1: Scaffold directory structure and shared assets

**Files:**
- Create: `microsoft-foundry/assets/css/` (directory)
- Create: `microsoft-foundry/assets/js/` (directory)
- Create: `microsoft-foundry/images/` (directory)
- Create: `microsoft-foundry/assets/js/main.js` (copy of agent365 version)
- Create: `microsoft-foundry/favicon.ico` (copy from agent365)

- [ ] **Step 1: Create directory structure and copy shared files**

```bash
mkdir -p microsoft-foundry/assets/css
mkdir -p microsoft-foundry/assets/js
mkdir -p microsoft-foundry/images
cp agent365/assets/js/main.js microsoft-foundry/assets/js/main.js
cp agent365/favicon.ico microsoft-foundry/favicon.ico
```

- [ ] **Step 2: Verify files exist**

```bash
ls -R microsoft-foundry/
```

Expected output includes:
```
microsoft-foundry/assets/css/
microsoft-foundry/assets/js/main.js
microsoft-foundry/favicon.ico
microsoft-foundry/images/
```

- [ ] **Step 3: Commit scaffold**

```bash
git add microsoft-foundry/assets/js/main.js microsoft-foundry/favicon.ico
git commit -m "feat(foundry): scaffold directory structure and shared assets"
```

---

### Task 2: Create styles.css with cobalt blue identity

**Files:**
- Create: `microsoft-foundry/assets/css/styles.css`

- [ ] **Step 1: Write the complete styles.css**

Create `microsoft-foundry/assets/css/styles.css` with this exact content:

```css
/* ── Reset & Base ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
	--brand-deep:   #071e75;
	--brand-mid:    #1038c8;
	--brand-accent: #1a4fe0;
	--brand-light:  #4c80f5;
	--teal-accent:  #3d6be0;
	--surface:      #ffffff;
	--surface-alt:  #eef2ff;
	--surface-hover:#dce5ff;
	--text:         #0d1117;
	--text-muted:   #4a5568;
	--text-on-dark: #dce9ff;
	--border:       #c0ccf5;
	--radius:       12px;
	--radius-lg:    20px;
	--shadow-sm:    0 1px 3px rgba(7,30,117,.06);
	--shadow-md:    0 4px 16px rgba(7,30,117,.08);
	--shadow-lg:    0 8px 32px rgba(7,30,117,.12);
	--transition:   .2s cubic-bezier(.4,0,.2,1);
	--space-1: .25rem;
	--space-2: .5rem;
	--space-3: .75rem;
	--space-4: 1rem;
	--space-5: 1.25rem;
	--space-6: 1.5rem;
	--space-7: 2rem;
	--space-8: 2.5rem;
	--space-9: 3rem;
	--space-10: 4rem;
	--text-xs: .7rem;
	--text-sm: .8rem;
	--text-base: .935rem;
	--text-md: 1rem;
	--text-lg: 1.1rem;
	--text-xl: 1.2rem;
	--text-2xl: 1.4rem;
}

html { scroll-behavior: smooth; }

body {
	font-family: 'Aptos', 'Segoe UI', system-ui, -apple-system, sans-serif;
	color: var(--text);
	line-height: 1.6;
	background: var(--surface);
	-webkit-font-smoothing: antialiased;
}

a {
	color: var(--brand-accent);
	text-decoration: none;
	transition: color var(--transition);
}
a:hover { color: var(--brand-mid); }

/* Focus-visible for keyboard navigation */
a:focus-visible, button:focus-visible, input:focus-visible {
	outline: 2px solid var(--brand-accent);
	outline-offset: 2px;
	border-radius: 4px;
}

.hero {
	background: linear-gradient(135deg,
		#071e75 0%, #1038c8 30%, #1a4fe0 65%, #3d6be0 100%);
	color: #ffffff;
	padding: 2.75rem 2rem 2.5rem;
	text-align: center;
	position: relative;
	overflow: hidden;
}
.hero::before {
	content: '';
	position: absolute;
	inset: 0;
	background:
		radial-gradient(ellipse 600px 400px at 20% 80%, rgba(26,79,224,.3) 0%, transparent 70%),
		radial-gradient(ellipse 500px 350px at 80% 20%, rgba(61,107,224,.2) 0%, transparent 70%);
	pointer-events: none;
}
.hero h1 {
	font-size: clamp(1.6rem, 4vw, 2.4rem);
	font-weight: 700;
	letter-spacing: -.02em;
	margin-bottom: var(--space-2);
	position: relative;
	color: #ffffff;
}
.hero p {
	font-size: var(--text-md);
	opacity: .9;
	max-width: 620px;
	margin: 0 auto;
	position: relative;
	color: #ffffff;
}
.hero a { color: #ffffff; font-weight: 700; text-decoration: underline; }
.hero a:hover { color: #c7d4ff; }

/* ── Back to Hub ── */
.hero-back {
	min-height: 44px;
	position: absolute;
	top: 1rem;
	left: 1.25rem;
	display: inline-flex;
	align-items: center;
	gap: .4rem;
	padding: .35rem .8rem;
	background: rgba(255,255,255,.15);
	border: 1px solid rgba(255,255,255,.3);
	border-radius: 2rem;
	color: #ffffff;
	font-size: .78rem;
	font-weight: 600;
	text-decoration: none;
	backdrop-filter: blur(4px);
	transition: background var(--transition), transform var(--transition);
	z-index: 1;
}
.hero-back:hover {
	background: rgba(255,255,255,.28);
	color: #ffffff;
	transform: translateX(-2px);
}
.hero-back svg {
	width: 14px;
	height: 14px;
	stroke: currentColor;
	fill: none;
	stroke-width: 2;
	stroke-linecap: round;
	stroke-linejoin: round;
	flex-shrink: 0;
}

/* ── Search ── */
.search-bar {
	max-width: 480px;
	margin: 1.25rem auto 0;
	position: relative;
}
.search-bar input {
	width: 100%;
	padding: .85rem 1.2rem .85rem 2.8rem;
	border: 1.5px solid rgba(255,255,255,.25);
	border-radius: 50px;
	background: rgba(255,255,255,.18);
	color: #ffffff;
	font-size: var(--text-md);
	backdrop-filter: blur(8px);
	transition: border-color var(--transition), background var(--transition);
}
.search-bar input::placeholder { color: rgba(255,255,255,.55); }
.search-bar input:focus {
	border-color: rgba(255,255,255,.4);
	background: rgba(255,255,255,.28);
	outline: none;
}
.search-bar svg {
	position: absolute;
	left: 1rem;
	top: 50%;
	transform: translateY(-50%);
	width: 18px;
	height: 18px;
	stroke: rgba(255,255,255,.6);
	fill: none;
	pointer-events: none;
}

/* ── Nav Pills ── */
.nav-strip {
	background: var(--surface);
	border-bottom: 1px solid var(--border);
	padding: .75rem 2rem;
	position: sticky;
	top: 0;
	z-index: 100;
	overflow-x: auto;
	display: flex;
	gap: var(--space-2);
	justify-content: center;
	-webkit-overflow-scrolling: touch;
}
.nav-strip::-webkit-scrollbar { display: none; }
.nav-strip a {
	min-height: 44px;
	display: inline-flex;
	align-items: center;
	white-space: nowrap;
	padding: .45rem 1rem;
	border-radius: 50px;
	font-size: .85rem;
	font-weight: 500;
	color: var(--text-muted);
	transition: all var(--transition);
	border: 1px solid transparent;
}
.nav-strip a:hover {
	color: var(--brand-accent);
	background: var(--surface-alt);
	border-color: var(--border);
}

/* ── Main Layout ── */
.content-wrap {
	max-width: 1080px;
	margin: 0 auto;
	padding: var(--space-9) var(--space-7) var(--space-10);
}

/* ── Section Cards ── */
.section-card {
	margin-bottom: var(--space-7);
	border: 1px solid var(--border);
	border-radius: var(--radius-lg);
	background: var(--surface);
	box-shadow: var(--shadow-sm);
	overflow: hidden;
	transition: box-shadow var(--transition);
}
.section-card:hover { box-shadow: var(--shadow-md); }

.section-header {
	display: flex;
	align-items: center;
	gap: var(--space-4);
	padding: 1.25rem 1.5rem;
	cursor: pointer;
	user-select: none;
	background: var(--surface);
	transition: background var(--transition);
	border: none;
	width: 100%;
	text-align: left;
	font: inherit;
	color: inherit;
}
.section-header:hover { background: var(--surface-alt); }

.section-icon {
	width: 42px;
	height: 42px;
	border-radius: var(--radius);
	display: flex;
	align-items: center;
	justify-content: center;
	font-size: 1.3rem;
	flex-shrink: 0;
}
.icon-start    { background: #dce5ff; color: #1038c8; }
.icon-news     { background: #e0f2fe; color: #0369a1; }
.icon-adoption { background: #ecfdf5; color: #047857; }
.icon-train    { background: #fff7ed; color: #c2410c; }
.icon-build    { background: #ede9fe; color: #5b21b6; }
.icon-models   { background: #dce5ff; color: #1038c8; }
.icon-evaluate { background: #fce7f3; color: #9d174d; }
.icon-arch     { background: #f0fdf4; color: #166534; }
.icon-stories  { background: #fefce8; color: #854d0e; }
.icon-samples  { background: #fff7ed; color: #c2410c; }
.icon-comm     { background: #fefce8; color: #854d0e; }

.section-title {
	font-size: var(--text-lg);
	font-weight: 600;
	flex: 1;
}

.chevron {
	width: 20px;
	height: 20px;
	stroke: var(--text-muted);
	fill: none;
	transition: transform .25s ease;
	flex-shrink: 0;
}
.section-card.open .chevron { transform: rotate(180deg); }

.section-body {
	display: none;
	padding: 0 1.5rem 1.5rem;
}
.section-card.open .section-body { display: block; }

/* ── Sub-sections ── */
.sub-heading {
	font-size: var(--text-sm);
	font-weight: 700;
	text-transform: uppercase;
	letter-spacing: .06em;
	color: var(--text-muted);
	margin: 1.25rem 0 .5rem;
	padding-bottom: .35rem;
	border-bottom: 1px solid var(--border);
}
.sub-heading:first-child { margin-top: 0; }

/* ── Link Lists ── */
.link-list {
	list-style: none;
	display: flex;
	flex-direction: column;
	gap: .35rem;
}
.link-list li {
	padding: .5rem .75rem;
	border-radius: var(--radius);
	transition: background var(--transition);
	font-size: var(--text-base);
	line-height: 1.5;
}
.link-list li:hover { background: var(--surface-hover); }
.link-list a { font-weight: 500; }

.link-sep {
	color: var(--text-muted);
	margin: 0 .25rem;
	font-size: .85em;
}

/* ── Session Grid ── */
.session-grid {
	display: grid;
	grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
	gap: var(--space-3);
	list-style: none;
}
.session-grid li {
	border: 1px solid var(--border);
	border-radius: var(--radius);
	overflow: hidden;
	transition: all var(--transition);
}
.session-grid li:hover {
	border-color: var(--brand-light);
	box-shadow: var(--shadow-md);
}
.session-grid a {
	display: flex;
	align-items: center;
	gap: var(--space-3);
	padding: .75rem 1rem;
	color: var(--text);
	font-weight: 500;
	font-size: .9rem;
	text-decoration: none;
	height: 100%;
}
.session-grid a:hover { color: var(--brand-accent); }

.session-badge {
	font-size: var(--text-xs);
	font-weight: 700;
	background: var(--surface-alt);
	color: var(--brand-accent);
	padding: .2rem .5rem;
	border-radius: 6px;
	flex-shrink: 0;
	letter-spacing: .02em;
}

/* ── Footer ── */
footer {
	background: var(--brand-deep);
	color: var(--text-on-dark);
	text-align: center;
	padding: 3rem 2rem 2rem;
}
footer p { opacity: .7; font-size: .95rem; margin-bottom: 1rem; }
footer .copyright {
	margin-top: 2.5rem;
	font-size: var(--text-sm);
	opacity: .45;
}

/* ── Responsive ── */
@media (max-width: 640px) {
	.hero { padding: 2rem 1.25rem 1.75rem; }
	.content-wrap { padding: var(--space-7) var(--space-4) var(--space-9); }
	.nav-strip { justify-content: flex-start; padding: .75rem 1rem; }
	.section-header { padding: 1rem 1.25rem; }
	.section-body { padding: 0 1.25rem 1.25rem; }
	.session-grid { grid-template-columns: 1fr; }
}

@media (min-width: 641px) and (max-width: 1024px) {
	.nav-strip { justify-content: flex-start; }
	.session-grid { grid-template-columns: repeat(2, 1fr); }
}
```

- [ ] **Step 2: Commit**

```bash
git add microsoft-foundry/assets/css/styles.css
git commit -m "feat(foundry): add cobalt blue styles.css"
```

---

### Task 3: Create index.html shell — head, hero, nav, footer

**Files:**
- Create: `microsoft-foundry/index.html` (overwrite the 1-line placeholder)

- [ ] **Step 1: Write the shell** (no section cards yet — `<main>` is empty)

Create `microsoft-foundry/index.html`:

```html
<!doctype html>
<html lang="en">
  <head>
    <title>Microsoft Foundry Resources</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="icon" href="favicon.ico" sizes="any" />
    <link rel="stylesheet" href="assets/css/styles.css" />

    <!-- Open Graph -->
    <meta property="og:type" content="article" />
    <meta property="og:title" content="Microsoft Foundry Resources" />
    <meta
      property="og:description"
      content="Curated learning materials to help you build, evaluate, and deploy AI models and agents with Microsoft Foundry — curated by the Microsoft Copilot Acceleration Team (CAT)."
    />
    <meta
      name="image"
      property="og:image"
      content="https://microsoft.github.io/agent-resources/microsoft-foundry/images/og-image.png"
    />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta name="author" content="Robert Standefer" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="Microsoft Foundry Resources" />
    <meta
      name="twitter:description"
      content="Curated learning materials to help you build, evaluate, and deploy AI models and agents with Microsoft Foundry — curated by the Microsoft Copilot Acceleration Team (CAT)."
    />
    <meta
      name="twitter:image"
      content="https://microsoft.github.io/agent-resources/microsoft-foundry/images/og-image.png"
    />

    <!-- TODO: Add Microsoft Clarity tag ID for this site -->
  </head>
  <body>
    <!-- ── Hero ── -->
    <section class="hero">
      <a href="../" class="hero-back">
        <svg viewBox="0 0 24 24"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
        Agent Resources
      </a>
      <h1>Microsoft Foundry Resources</h1>
      <p>
        Resources to help you build, evaluate, and deploy AI models and agents with Microsoft Foundry,<br>
        curated by the <a href="https://aka.ms/wearecat">Microsoft Copilot Acceleration Team (CAT)</a>.
      </p>
      <div class="search-bar">
        <svg
          viewBox="0 0 24 24"
          stroke-width="2"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <circle cx="11" cy="11" r="8" />
          <line x1="21" y1="21" x2="16.65" y2="16.65" />
        </svg>
        <input
          type="text"
          id="searchInput"
          aria-label="Search resources"
          placeholder="Search resources..."
          autocomplete="off"
        />
      </div>
    </section>

    <!-- ── Sticky Nav ── -->
    <nav class="nav-strip" id="navStrip">
      <a href="#get-started">Get Started</a>
      <a href="#news">News</a>
      <a href="#adoption">Adoption</a>
      <a href="#training">Training</a>
      <a href="#building">Build</a>
      <a href="#models">Models</a>
      <a href="#evaluate">Evaluate</a>
      <a href="#architecture">Architecture</a>
      <a href="#stories">Stories</a>
      <a href="#samples">Samples</a>
      <a href="#community">Community</a>
    </nav>

    <!-- ── Content ── -->
    <main class="content-wrap">
      <!-- sections go here in Tasks 4–8 -->
    </main>

    <!-- ── Footer ── -->
    <footer>
      <p>Created &amp; managed by <a href="https://www.linkedin.com/in/rstandefer/">Robert Standefer</a> and the <a href="https://aka.ms/wearecat">Microsoft Copilot Acceleration Team (CAT)</a></p>
      <p class="copyright">© 2026 Microsoft. All rights reserved.</p>
    </footer>

    <script src="assets/js/main.js"></script>
  </body>
</html>
```

- [ ] **Step 2: Open in browser and verify**

Open `microsoft-foundry/index.html` in a browser (e.g., double-click the file or use a local server). Confirm:
- Hero renders with cobalt blue gradient (dark navy at left, medium blue at right)
- "Agent Resources" back-link appears top-left
- Nav strip shows all 11 pill links and sticks on scroll
- Footer is dark navy with white text
- No console errors

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add index.html shell with hero, nav, footer"
```

---

### Task 4: Sections 1–2 — Get Started and News

**Files:**
- Modify: `microsoft-foundry/index.html` — replace `<!-- sections go here -->` comment with sections 1 and 2

- [ ] **Step 1: Add sections 1 and 2 inside `<main class="content-wrap">`**

Replace the `<!-- sections go here in Tasks 4–8 -->` comment with:

```html
      <!-- ── GET STARTED ── -->
      <div class="section-card" id="get-started">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-start" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16l4-4-4-4"/><line x1="8" y1="12" x2="16" y2="12"/></svg></span>
          <span class="section-title">Get started with Microsoft Foundry</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">What is Microsoft Foundry?</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/what-is-ai-foundry" target="_blank" rel="noopener">What is Microsoft Foundry?</a> &mdash; overview and core concepts</li>
            <li>Documentation hub &mdash; <a href="https://learn.microsoft.com/azure/ai-foundry/" target="_blank" rel="noopener">learn.microsoft.com/azure/ai-foundry</a></li>
            <li>Microsoft Foundry portal &mdash; <a href="https://ai.azure.com" target="_blank" rel="noopener">ai.azure.com</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/quickstarts/get-started-playground" target="_blank" rel="noopener">Quickstart: Get started in the Foundry playground</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects" target="_blank" rel="noopener">Create your first project in Microsoft Foundry</a></li>
          </ul>
          <h3 class="sub-heading">Key concepts</h3>
          <ul class="link-list">
            <li><strong>Hubs</strong> &mdash; top-level governance containers shared across teams and projects</li>
            <li><strong>Projects</strong> &mdash; workspaces where teams build, evaluate, and deploy AI apps</li>
            <li><strong>Connections</strong> &mdash; secure links to models, data sources, and services</li>
            <li><strong>Deployments</strong> &mdash; hosted model endpoints for production inference</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/concepts/ai-foundry-architecture" target="_blank" rel="noopener">Microsoft Foundry architecture</a> &mdash; how hubs, projects, and resources relate</li>
          </ul>
        </div>
      </div>

      <!-- ── NEWS ── -->
      <div class="section-card" id="news">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-news" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
          <span class="section-title">News and announcements</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <ul class="link-list">
            <li>Azure AI Blog &mdash; <a href="https://techcommunity.microsoft.com/category/azure-ai-services/blog/azure-ai-services-blog" target="_blank" rel="noopener">latest posts and announcements</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/whats-new" target="_blank" rel="noopener">What's new in Microsoft Foundry</a> &mdash; release notes and changelog</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/whats-new" target="_blank" rel="noopener">What's new in Azure OpenAI Service</a> &mdash; model and feature releases</li>
            <li><a href="https://blogs.microsoft.com/ai/" target="_blank" rel="noopener">Microsoft AI Blog</a> &mdash; platform strategy and announcements</li>
          </ul>
          <h3 class="sub-heading">Microsoft Build 2025</h3>
          <ul class="session-grid">
            <li><a href="https://build.microsoft.com/sessions/4372eb0e-ea4d-4ea2-a4fd-208e2e14e1f1" target="_blank" rel="noopener"><span class="session-badge">BRK</span> Intelligent Apps with Azure AI Foundry</a></li>
            <li><a href="https://build.microsoft.com/sessions/3f82a9ef-c12e-4be6-9547-04b42d9e498b" target="_blank" rel="noopener"><span class="session-badge">BRK</span> Azure AI Agent Service: Build production AI agents</a></li>
          </ul>
          <h3 class="sub-heading">Microsoft Ignite 2024</h3>
          <ul class="session-grid">
            <li><a href="https://ignite.microsoft.com/sessions/KEY01" target="_blank" rel="noopener"><span class="session-badge">KEY01</span> Opening Keynote</a></li>
            <li><a href="https://ignite.microsoft.com/sessions/BRK102" target="_blank" rel="noopener"><span class="session-badge">BRK102</span> Azure AI Foundry: Build the next generation of AI apps</a></li>
          </ul>
        </div>
      </div>

      <!-- remaining sections added in tasks 5–8 -->
```

- [ ] **Step 2: Open in browser, click "Get Started" and "News" headers**

Confirm:
- Both cards expand/collapse on click
- `#get-started` and `#news` nav links scroll to and open the correct card
- All links have correct `target="_blank" rel="noopener"` (inspect in DevTools if unsure)

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add Get Started and News sections"
```

---

### Task 5: Sections 3–4 — Successful Adoption and Training & Certification

**Files:**
- Modify: `microsoft-foundry/index.html` — replace `<!-- remaining sections added in tasks 5–8 -->` with sections 3 and 4 (keep the comment at the end for remaining tasks)

- [ ] **Step 1: Add sections 3 and 4 before the remaining-sections comment**

```html
      <!-- ── SUCCESSFUL ADOPTION ── -->
      <div class="section-card" id="adoption">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-adoption" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></span>
          <span class="section-title">Successful adoption</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Cloud Adoption Framework</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/" target="_blank" rel="noopener">AI adoption scenario in the Cloud Adoption Framework</a> &mdash; strategy, plan, ready, adopt, govern, manage</li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/azure-ai-foundry-landing-zone" target="_blank" rel="noopener">Microsoft Foundry landing zone accelerator</a> &mdash; reference implementation for enterprise deployments</li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/plan" target="_blank" rel="noopener">Plan for AI adoption</a> &mdash; organizational readiness and AI strategy</li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/ready" target="_blank" rel="noopener">Prepare your Azure environment for AI workloads</a></li>
          </ul>
          <h3 class="sub-heading">Adoption guidance</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/responsible-use-of-ai-overview" target="_blank" rel="noopener">Responsible use of AI in Microsoft Foundry</a> &mdash; principles and practices for responsible AI adoption</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/responsible-use-of-ai-overview" target="_blank" rel="noopener">Responsible AI overview for Azure AI Services</a></li>
            <li><a href="https://www.microsoft.com/ai/responsible-ai" target="_blank" rel="noopener">Microsoft Responsible AI</a> &mdash; company-wide principles and tools</li>
          </ul>
        </div>
      </div>

      <!-- ── TRAINING & CERTIFICATION ── -->
      <div class="section-card" id="training">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-train" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg></span>
          <span class="section-title">Training and certification</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Microsoft Learn paths</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/" target="_blank" rel="noopener">Build AI apps with Microsoft Foundry</a> &mdash; end-to-end learning path</li>
            <li><a href="https://learn.microsoft.com/training/paths/work-with-azure-openai/" target="_blank" rel="noopener">Develop AI solutions with Azure OpenAI Service</a></li>
            <li><a href="https://learn.microsoft.com/training/paths/apply-prompt-engineering-azure-openai/" target="_blank" rel="noopener">Apply prompt engineering with Azure OpenAI Service</a></li>
            <li><a href="https://learn.microsoft.com/training/paths/develop-ai-agents-azure-open-ai-semantic-kernel-sdk/" target="_blank" rel="noopener">Develop AI agents with Azure OpenAI and Semantic Kernel</a></li>
            <li><a href="https://learn.microsoft.com/training/browse/?products=azure-machine-learning&resource_type=learning%20path" target="_blank" rel="noopener">Browse all Azure AI &amp; ML learning paths</a></li>
          </ul>
          <h3 class="sub-heading">Applied Skills &amp; labs</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/credentials/applied-skills/develop-generative-ai-solutions-with-azure-openai-service/" target="_blank" rel="noopener">Develop generative AI solutions with Azure OpenAI Service</a> &mdash; Applied Skills credential</li>
            <li><a href="https://learn.microsoft.com/credentials/applied-skills/build-a-natural-language-processing-solution-with-azure-ai-language/" target="_blank" rel="noopener">Build a natural language processing solution with Azure AI Language</a> &mdash; Applied Skills credential</li>
            <li><a href="https://learn.microsoft.com/training/browse/?resource_type=module&products=azure-machine-learning&levels=intermediate" target="_blank" rel="noopener">Intermediate Azure AI hands-on labs</a></li>
          </ul>
          <h3 class="sub-heading">Certifications</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/credentials/certifications/azure-ai-engineer/" target="_blank" rel="noopener">AI-102: Azure AI Engineer Associate</a> &mdash; designing and implementing Azure AI solutions</li>
            <li><a href="https://learn.microsoft.com/credentials/certifications/azure-data-scientist/" target="_blank" rel="noopener">DP-100: Azure Data Scientist Associate</a> &mdash; machine learning solutions on Azure</li>
            <li><a href="https://learn.microsoft.com/credentials/certifications/azure-ai-fundamentals/" target="_blank" rel="noopener">AI-900: Azure AI Fundamentals</a> &mdash; foundational AI and ML concepts on Azure</li>
          </ul>
        </div>
      </div>
```

- [ ] **Step 2: Verify in browser**

Click "Adoption" and "Training" nav pills — both should scroll to and open the matching cards.

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add Successful Adoption and Training sections"
```

---

### Task 6: Sections 5–6 — Build with Foundry and Models & Services

**Files:**
- Modify: `microsoft-foundry/index.html`

- [ ] **Step 1: Add sections 5 and 6**

```html
      <!-- ── BUILD WITH FOUNDRY ── -->
      <div class="section-card" id="building">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-build" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg></span>
          <span class="section-title">Build with Microsoft Foundry</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Azure AI Agent Service</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank" rel="noopener">What is Azure AI Agent Service?</a> &mdash; build production AI agents with tools and memory</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/agents/quickstart" target="_blank" rel="noopener">Quickstart: Create your first AI agent</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/overview" target="_blank" rel="noopener">Agent tools overview</a> &mdash; code interpreter, file search, function calling, Bing grounding</li>
          </ul>
          <h3 class="sub-heading">Prompt Flow</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/prompt-flow" target="_blank" rel="noopener">Prompt Flow in Microsoft Foundry</a> &mdash; build and iterate on LLM-based flows</li>
            <li><a href="https://microsoft.github.io/promptflow/" target="_blank" rel="noopener">Prompt Flow documentation</a> &mdash; open-source SDK and tooling</li>
            <li><a href="https://github.com/microsoft/promptflow" target="_blank" rel="noopener">microsoft/promptflow</a> &mdash; GitHub repository</li>
          </ul>
          <h3 class="sub-heading">Foundry SDK &amp; development tools</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/develop/sdk-overview" target="_blank" rel="noopener">Microsoft Foundry SDK overview</a> &mdash; Python, JavaScript, and .NET</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/develop/trace-production-sdk" target="_blank" rel="noopener">Tracing and observability for AI apps</a> &mdash; distributed tracing in Foundry</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/tutorials/copilot-sdk-build-rag" target="_blank" rel="noopener">Tutorial: Build a RAG app with the Foundry SDK</a></li>
            <li><a href="https://marketplace.visualstudio.com/items?itemName=ms-toolsai.aistudio" target="_blank" rel="noopener">Microsoft Foundry VS Code extension</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/develop/langchain" target="_blank" rel="noopener">Use LangChain with Microsoft Foundry</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/develop/semantic-kernel" target="_blank" rel="noopener">Use Semantic Kernel with Microsoft Foundry</a></li>
          </ul>
        </div>
      </div>

      <!-- ── MODELS & SERVICES ── -->
      <div class="section-card" id="models">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-models" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg></span>
          <span class="section-title">Models and services</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Model catalog</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/model-catalog-overview" target="_blank" rel="noopener">Model catalog overview</a> &mdash; browse and compare hundreds of models from Microsoft, OpenAI, Meta, Mistral, and more</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/model-benchmarks" target="_blank" rel="noopener">Model benchmarks</a> &mdash; compare quality and performance metrics across models</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/deploy-models-serverless" target="_blank" rel="noopener">Serverless API deployments (MaaS)</a> &mdash; pay-per-token, no managed infrastructure</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/deploy-models-managed-compute" target="_blank" rel="noopener">Managed compute deployments (MaaP)</a> &mdash; dedicated compute with full control</li>
          </ul>
          <h3 class="sub-heading">Azure OpenAI Service</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/overview" target="_blank" rel="noopener">Azure OpenAI Service overview</a> &mdash; GPT-4o, o-series, DALL-E, Whisper, embeddings</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/models" target="_blank" rel="noopener">Azure OpenAI model reference</a> &mdash; all available models and versions</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/whats-new" target="_blank" rel="noopener">What's new in Azure OpenAI</a> &mdash; latest model releases and features</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/quotas-limits" target="_blank" rel="noopener">Quotas, limits, and regional availability</a></li>
          </ul>
          <h3 class="sub-heading">Azure AI Services</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-services/" target="_blank" rel="noopener">Azure AI Services documentation hub</a> &mdash; vision, speech, language, document intelligence, search</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/computer-vision/overview" target="_blank" rel="noopener">Azure AI Vision</a> &mdash; image analysis, OCR, face detection</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/speech-service/overview" target="_blank" rel="noopener">Azure AI Speech</a> &mdash; speech-to-text, text-to-speech, translation</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/language-service/overview" target="_blank" rel="noopener">Azure AI Language</a> &mdash; NLP, sentiment, entity recognition, summarization</li>
            <li><a href="https://learn.microsoft.com/azure/search/search-what-is-azure-search" target="_blank" rel="noopener">Azure AI Search</a> &mdash; vector and hybrid search for RAG patterns</li>
          </ul>
        </div>
      </div>
```

- [ ] **Step 2: Verify in browser** — click "Build" and "Models" nav links, confirm both sections expand correctly.

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add Build with Foundry and Models & Services sections"
```

---

### Task 7: Sections 7–8 — Evaluate & Improve and Architecture & Best Practices

**Files:**
- Modify: `microsoft-foundry/index.html`

- [ ] **Step 1: Add sections 7 and 8**

```html
      <!-- ── EVALUATE & IMPROVE ── -->
      <div class="section-card" id="evaluate">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-evaluate" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg></span>
          <span class="section-title">Evaluate and improve</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Evaluations</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-generative-ai-app" target="_blank" rel="noopener">Evaluate your generative AI app in Microsoft Foundry</a> &mdash; built-in and custom evaluators</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/evaluate-sdk-code-only" target="_blank" rel="noopener">Azure AI Evaluation SDK</a> &mdash; run evaluations in code without the portal</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/concepts/evaluation-metrics-built-in" target="_blank" rel="noopener">Built-in evaluation metrics</a> &mdash; groundedness, relevance, coherence, fluency, similarity</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/monitor-deployments" target="_blank" rel="noopener">Monitor deployed models</a> &mdash; track quality, latency, and token usage in production</li>
          </ul>
          <h3 class="sub-heading">Fine-tuning</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/fine-tuning" target="_blank" rel="noopener">Fine-tune Azure OpenAI models</a> &mdash; customize GPT-4o, GPT-4o mini, and more</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-model-llama" target="_blank" rel="noopener">Fine-tune Meta Llama models in Microsoft Foundry</a></li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/fine-tune-phi-3" target="_blank" rel="noopener">Fine-tune Phi-3 models in Microsoft Foundry</a></li>
          </ul>
          <h3 class="sub-heading">Content safety and responsible AI</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/content-filter" target="_blank" rel="noopener">Content filtering in Azure OpenAI</a> &mdash; default and configurable safety layers</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/content-safety/overview" target="_blank" rel="noopener">Azure AI Content Safety</a> &mdash; detect harmful content across text and images</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/responsible-ai-overview" target="_blank" rel="noopener">Responsible AI tools in Microsoft Foundry</a> &mdash; safety evaluations, red-teaming, dashboards</li>
          </ul>
        </div>
      </div>

      <!-- ── ARCHITECTURE & BEST PRACTICES ── -->
      <div class="section-card" id="architecture">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-arch" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg></span>
          <span class="section-title">Architecture and best practices</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Cloud Adoption Framework (CAF)</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/" target="_blank" rel="noopener">AI adoption scenario</a> &mdash; strategy, planning, readiness, governance, and management for AI at scale</li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/azure-ai-foundry-landing-zone" target="_blank" rel="noopener">Microsoft Foundry landing zone accelerator</a> &mdash; enterprise-ready reference implementation</li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/ready" target="_blank" rel="noopener">Prepare your landing zone for AI workloads</a></li>
            <li><a href="https://learn.microsoft.com/azure/cloud-adoption-framework/scenarios/ai/govern" target="_blank" rel="noopener">Govern AI workloads</a> &mdash; policies, controls, and compliance for AI in the enterprise</li>
          </ul>
          <h3 class="sub-heading">Well-Architected Framework (WAF)</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/well-architected/ai/" target="_blank" rel="noopener">AI workloads on Azure</a> &mdash; WAF guidance for reliability, security, cost, performance, and operations</li>
            <li><a href="https://learn.microsoft.com/azure/well-architected/ai/get-started" target="_blank" rel="noopener">Get started with AI workload design</a></li>
            <li><a href="https://learn.microsoft.com/azure/well-architected/ai/security" target="_blank" rel="noopener">Security for AI workloads</a> &mdash; WAF security pillar applied to AI</li>
          </ul>
          <h3 class="sub-heading">Reference architectures</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/architecture/ai-ml/architecture/rag-azure-ai-foundry-openai" target="_blank" rel="noopener">RAG baseline architecture with Microsoft Foundry</a> &mdash; production-ready retrieval-augmented generation</li>
            <li><a href="https://learn.microsoft.com/azure/architecture/ai-ml/" target="_blank" rel="noopener">Azure Architecture Center: AI + Machine Learning</a> &mdash; patterns, guides, and reference architectures</li>
            <li><a href="https://learn.microsoft.com/azure/architecture/ai-ml/architecture/baseline-openai-e2e-chat" target="_blank" rel="noopener">Baseline OpenAI end-to-end chat architecture</a></li>
          </ul>
          <h3 class="sub-heading">Security and networking</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/configure-private-link" target="_blank" rel="noopener">Configure private link for Microsoft Foundry</a> &mdash; network isolation with private endpoints</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/rbac-ai-foundry" target="_blank" rel="noopener">Role-based access control in Microsoft Foundry</a> &mdash; built-in roles and custom role assignments</li>
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/troubleshoot-secure-connection-project" target="_blank" rel="noopener">Secure your Microsoft Foundry hub</a> &mdash; managed virtual networks and outbound rules</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/managed-identity" target="_blank" rel="noopener">Use managed identity with Azure OpenAI</a> &mdash; keyless authentication best practice</li>
          </ul>
        </div>
      </div>
```

- [ ] **Step 2: Verify in browser** — click "Evaluate" and "Architecture" nav links.

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add Evaluate & Improve and Architecture sections"
```

---

### Task 8: Sections 9–11 — Stories, Samples, and Community

**Files:**
- Modify: `microsoft-foundry/index.html` — add final three sections and remove the remaining-sections comment

- [ ] **Step 1: Add sections 9–11 and remove the placeholder comment**

```html
      <!-- ── REAL-WORLD CUSTOMER STORIES ── -->
      <div class="section-card" id="stories">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-stories" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg></span>
          <span class="section-title">Real-world customer stories</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <ul class="link-list">
            <li><a href="https://customers.microsoft.com/en-us/search?sq=azure%20ai%20foundry&ff=&p=0&so=story_publish_date%20desc" target="_blank" rel="noopener">Customer stories: Microsoft Foundry</a> &mdash; browse published case studies</li>
            <li><a href="https://customers.microsoft.com/en-us/search?sq=azure%20openai&ff=industry%2FFinancial%20services&p=0&so=story_publish_date%20desc" target="_blank" rel="noopener">Financial services AI stories</a> &mdash; banking, insurance, and capital markets</li>
            <li><a href="https://customers.microsoft.com/en-us/search?sq=azure%20openai&ff=industry%2FHealth" target="_blank" rel="noopener">Healthcare AI stories</a> &mdash; clinical, administrative, and patient-facing AI</li>
            <li><a href="https://customers.microsoft.com/en-us/search?sq=azure%20openai&ff=industry%2FRetail%20%26%20consumer%20goods" target="_blank" rel="noopener">Retail and consumer goods AI stories</a></li>
            <li><a href="https://azure.microsoft.com/en-us/resources/customer-stories/" target="_blank" rel="noopener">All Azure customer stories</a></li>
          </ul>
        </div>
      </div>

      <!-- ── SAMPLES ── -->
      <div class="section-card" id="samples">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-samples" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg></span>
          <span class="section-title">Samples</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <h3 class="sub-heading">Official sample repositories</h3>
          <ul class="link-list">
            <li><a href="https://github.com/azure-samples/azureai-samples" target="_blank" rel="noopener">azure-samples/azureai-samples</a> &mdash; official Microsoft Foundry sample collection</li>
            <li><a href="https://github.com/azure-samples/azure-ai-agent-service-toolkit" target="_blank" rel="noopener">azure-samples/azure-ai-agent-service-toolkit</a> &mdash; Azure AI Agent Service starter kit</li>
            <li><a href="https://github.com/azure/openai-samples" target="_blank" rel="noopener">azure/openai-samples</a> &mdash; Azure OpenAI code samples</li>
            <li><a href="https://github.com/microsoft/promptflow/tree/main/examples" target="_blank" rel="noopener">microsoft/promptflow — examples</a> &mdash; Prompt Flow sample flows</li>
            <li><a href="https://github.com/azure-samples/rag-postgres-openai-python" target="_blank" rel="noopener">azure-samples/rag-postgres-openai-python</a> &mdash; RAG with PostgreSQL and Azure OpenAI</li>
            <li><a href="https://github.com/azure-samples/azure-search-openai-demo" target="_blank" rel="noopener">azure-samples/azure-search-openai-demo</a> &mdash; ChatGPT + Azure AI Search reference app</li>
          </ul>
          <h3 class="sub-heading">Solution accelerators</h3>
          <ul class="link-list">
            <li><a href="https://learn.microsoft.com/azure/ai-foundry/how-to/develop/ai-template-get-started" target="_blank" rel="noopener">Azure AI templates</a> &mdash; production-ready starter templates from the Foundry portal</li>
            <li><a href="https://github.com/azure/ai-app-templates" target="_blank" rel="noopener">azure/ai-app-templates</a> &mdash; AI application scaffolding templates</li>
          </ul>
        </div>
      </div>

      <!-- ── COMMUNITY & SUPPORT ── -->
      <div class="section-card" id="community">
        <button class="section-header" aria-expanded="false">
          <span class="section-icon icon-comm" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg></span>
          <span class="section-title">Community and support</span>
          <svg class="chevron" viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9" /></svg>
        </button>
        <div class="section-body">
          <ul class="link-list">
            <li>Azure AI Tech Community &mdash; <a href="https://techcommunity.microsoft.com/category/azure-ai-services" target="_blank" rel="noopener">latest blog posts and discussions</a></li>
            <li><a href="https://techcommunity.microsoft.com/category/azure-ai-services/blog/azure-ai-services-blog" target="_blank" rel="noopener">Azure AI Services blog</a> &mdash; product announcements and how-tos from the team</li>
            <li><a href="https://github.com/azure/azure-ai-foundry/discussions" target="_blank" rel="noopener">Microsoft Foundry GitHub Discussions</a> &mdash; ask questions and share ideas</li>
            <li><a href="https://feedback.azure.com/d365community/forum/a28c4d87-5cfa-ec11-a81c-000d3a5e4b03" target="_blank" rel="noopener">Microsoft Foundry feedback</a> &mdash; vote on feature requests and report issues</li>
            <li><a href="https://stackoverflow.com/questions/tagged/azure-ai-studio" target="_blank" rel="noopener">Stack Overflow: azure-ai-studio</a> &mdash; community Q&amp;A</li>
            <li><a href="https://learn.microsoft.com/azure/ai-services/openai/support" target="_blank" rel="noopener">Azure OpenAI support</a> &mdash; service limits, quotas, and support channels</li>
          </ul>
        </div>
      </div>
```

- [ ] **Step 2: Verify all 11 sections in browser**

Open `microsoft-foundry/index.html`. Check:
- All 11 nav links scroll to and expand the correct section
- Search: type "fine-tun" — the Evaluate section auto-expands showing the fine-tuning links
- Search: type "CAF" — the Architecture section auto-expands
- Search: clear — all sections collapse and return to normal
- No console errors

- [ ] **Step 3: Commit**

```bash
git add microsoft-foundry/index.html
git commit -m "feat(foundry): add Stories, Samples, and Community sections — site complete"
```

---

### Task 9: Final smoke-test and update spec

**Files:**
- Read: `microsoft-foundry/index.html` (verify final state)

- [ ] **Step 1: Verify nav link count matches section count**

```bash
grep -c 'href="#' microsoft-foundry/index.html
grep -c 'class="section-card"' microsoft-foundry/index.html
```

Both should output `11`.

- [ ] **Step 2: Verify all external links have `rel="noopener"`**

```bash
grep -c 'target="_blank"' microsoft-foundry/index.html
grep -c 'rel="noopener"' microsoft-foundry/index.html
```

Both counts must be equal.

- [ ] **Step 3: Verify main.js is identical to agent365**

```bash
diff microsoft-foundry/assets/js/main.js agent365/assets/js/main.js
```

Expected: no output (files are identical).

- [ ] **Step 4: Final commit**

```bash
git add -A
git status
# Confirm only microsoft-foundry/ files are staged; nothing unintended
git commit -m "feat(foundry): complete microsoft-foundry resource site"
```
