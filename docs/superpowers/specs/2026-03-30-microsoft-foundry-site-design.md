# Microsoft Foundry Resource Site — Design Spec
_Date: 2026-03-30_

## Overview

Create a new child site at `microsoft-foundry/` following the established pattern of the other resource hubs (m365-copilot, copilot-studio, agent365, develop-agents). The site provides curated learning resources for Microsoft Foundry — Microsoft's platform for building, evaluating, and deploying AI models and agents.

The site is self-contained, published via GitHub Pages with no build step, and identical in structure to the other child sites. It is scoped similarly to the Copilot Studio site but expanded to reflect Foundry's greater product complexity.

---

## Architecture

Mirrors all other child sites exactly:

```
microsoft-foundry/
  index.html
  assets/
    css/styles.css
    js/main.js
  images/
  favicon.ico
```

- `index.html` — all content; hero, sticky nav, accordion sections, footer
- `styles.css` — Foundry color identity; otherwise identical tokens and layout rules to other sites
- `main.js` — identical copy of the shared accordion + hash-nav + search logic (kept in sync with other sites per CLAUDE.md)
- `images/` — placeholder directory for header image, OG image, favicon source
- `favicon.ico` — Foundry favicon (to be added as asset)

No build step. Push to `main` to deploy.

---

## Color Identity

Based on the Microsoft Foundry icon's cobalt blue palette — a saturated electric blue distinct from M365 Copilot's lighter sky blue (`#0078d4`), Agent 365's blue-indigo (`#3b5bdb`), and the purple tones of Copilot Studio / develop-agents.

| Token | Value | Usage |
|-------|-------|-------|
| `--brand-deep` | `#071e75` | Footer background, deep shadows |
| `--brand-mid` | `#1038c8` | Hover states |
| `--brand-accent` | `#1a4fe0` | Links, badges, focus rings |
| `--brand-light` | `#4c80f5` | Session grid hover borders |
| `--teal-accent` | `#3d6be0` | Accent highlights |
| `--surface-alt` | `#eef2ff` | Section hover backgrounds |
| `--surface-hover` | `#dce5ff` | Link list row hover |
| `--border` | `#c0ccf5` | Card borders |
| Shadow colors | `rgba(7,30,117,…)` | Replaces blue-tinted shadows |

**Hero gradient:** `135deg, #071e75 0%, #1038c8 30%, #1a4fe0 65%, #3d6be0 100%`

**Hero overlay radial gradients** (the `::before` ambient layer): two ellipses using the deep navy and cobalt blue values, mirroring the pattern from other sites.

**Search bar text/placeholder colors:** deep navy (`#071e75`) to maintain legibility on the blue gradient.

---

## Sections (11 total)

Nav strip order matches section order.

### 1. Get Started
**ID:** `get-started` | **Nav label:** Get Started

What is Microsoft Foundry, where to find official docs, a quickstart, and an overview video. Mirrors the "I am new" framing from Copilot Studio but uses a direct title.

Content:
- What is Microsoft Foundry? (overview doc link)
- Official documentation hub (`learn.microsoft.com/azure/ai-foundry`)
- Quickstart: create a project in Foundry
- Overview / intro video
- Product page / marketing site
- Microsoft Foundry in the Azure portal (direct link)
- Key concepts: projects, hubs, connections, deployments

### 2. News & Announcements
**ID:** `news` | **Nav label:** News

Latest blog posts, feature releases, and conference announcements (Build, Ignite).

Content:
- Azure AI Blog (`techcommunity.microsoft.com/category/azure-ai-services/blog/azure-ai-services-blog`)
- What's new in Microsoft Foundry (release notes / changelog page)
- Ignite and Build announcement blog posts (by date, most recent first)
- Microsoft AI platform announcements section in Book of News where applicable

### 3. Successful Adoption
**ID:** `adoption` | **Nav label:** Adoption

Guidance and frameworks for organizations adopting Foundry at scale — change management, planning, CAF adoption scenarios.

Content:
- Cloud Adoption Framework: AI adoption scenario for Microsoft Foundry
- Microsoft Foundry adoption guide / deployment accelerator (if available)
- Planning and readiness resources
- Organizational readiness for AI workloads

### 4. Training & Certification
**ID:** `training` | **Nav label:** Training

Microsoft Learn paths, instructor-led training, hands-on labs, and formal certifications relevant to Foundry.

Content:
- **Learn paths:** "Get started with Microsoft Foundry", Azure AI Engineer path
- **Certifications:**
  - AI-102: Designing and Implementing a Microsoft Azure AI Solution
  - DP-100: Designing and Implementing a Data Science Solution on Azure
  - AI-050: Develop Generative AI solutions (if applicable)
- **Labs:** Applied Skills for Microsoft Foundry / generative AI
- **Microsoft Learn sandbox** / guided exercises

### 5. Build with Foundry
**ID:** `building` | **Nav label:** Build

Developer-facing resources for building applications and agents using Foundry's core tooling — prompt flow, the Azure AI Agent Service, the Foundry SDK, and related tools.

Content:
- Azure AI Agent Service documentation
- Prompt Flow: getting started, authoring flows
- Foundry SDK (Python, JavaScript, .NET) — reference and quickstart
- Microsoft Foundry VS Code extension
- MCP (Model Context Protocol) integration with Foundry
- Evaluation SDK (developer-oriented evaluation tooling)
- Tracing and observability for AI apps
- RAG (retrieval-augmented generation) patterns and how-tos

### 6. Models & Services
**ID:** `models` | **Nav label:** Models

The model catalog, Azure OpenAI Service, and the broader AI services portfolio accessible from Foundry.

Content:
- **Model catalog:** browse and deploy models from Microsoft Foundry
- **Azure OpenAI Service:** docs hub, model reference (GPT-4o, o-series, etc.)
- **Azure AI Services:** vision, speech, language, document intelligence, content safety
- Serverless API deployments (MaaS) vs. managed compute (MaaP)
- Model benchmarks and comparisons
- What's new in Azure OpenAI

### 7. Evaluate & Improve
**ID:** `evaluate` | **Nav label:** Evaluate

Resources for measuring, improving, and governing AI model and application quality — evaluations, fine-tuning, content safety, and monitoring.

Content:
- Evaluation in Microsoft Foundry (built-in evaluators, custom evaluators)
- Azure AI Evaluation SDK
- Fine-tuning models in Foundry
- Distillation
- Content filtering and Azure AI Content Safety
- Monitoring deployed models and AI apps
- Responsible AI dashboard

### 8. Architecture & Best Practices
**ID:** `architecture` | **Nav label:** Architecture

Cloud Adoption Framework, Well-Architected Framework, reference architectures, landing zones, and security/governance guidance for Foundry workloads.

Content:
- **CAF:** Microsoft Foundry adoption scenario in Cloud Adoption Framework
- **WAF:** AI workload guidance in Azure Well-Architected Framework
- Microsoft Foundry landing zone accelerator
- Microsoft Foundry reference architectures (RAG baseline, multi-agent, etc.)
- Security baseline for Microsoft Foundry
- Network isolation and private endpoints
- Identity and access management for Foundry
- Cost management and optimization

### 9. Real-World Customer Stories
**ID:** `stories` | **Nav label:** Stories

Published case studies, partner success stories, and customer showcases using Microsoft Foundry.

Content:
- Azure customer stories filtered to Microsoft Foundry
- Partner spotlights
- Industry-specific implementations (healthcare, finance, retail, etc.)

### 10. Samples
**ID:** `samples` | **Nav label:** Samples

GitHub repositories, solution accelerators, notebooks, and templates.

Content:
- `azure-samples/azureai-samples` — official samples repo
- Microsoft Foundry solution accelerators
- Prompt Flow sample flows gallery
- Azure OpenAI samples
- RAG solution accelerators
- Multi-agent sample applications
- Microsoft Foundry GitHub org overview

### 11. Community & Support
**ID:** `community` | **Nav label:** Community

Tech Community blog, GitHub Discussions, support channels, and office hours.

Content:
- Azure AI Tech Community (`techcommunity.microsoft.com/category/azure-ai-services`)
- Microsoft Foundry GitHub Discussions
- Microsoft Foundry feedback / UserVoice
- Azure support options
- Office hours / live Q&A sessions (if recurring)
- Microsoft Foundry Discord or community channels (if applicable)

---

## OG / Social Metadata

- `og:title`: "Microsoft Foundry Resources"
- `og:description`: "Curated learning materials to help you build, evaluate, and deploy AI models and agents with Microsoft Foundry — curated by the Microsoft Copilot Acceleration Team (CAT)."
- `og:image`: `microsoft-foundry/images/og-image.png` (1200×630, to be created)
- Clarity tag ID: TBD (new tag needed for this site)

---

## Root Hub Update

The root `index.html` card for Foundry (`card-foundry` class, cobalt blue accent) has been added as part of this work — it is not a separate task.

---

## Constraints

- No build step — plain HTML/CSS/JS only
- `main.js` must be an identical copy of the shared script (per CLAUDE.md)
- `favicon.ico` is required (copy from another site as placeholder until a Foundry-specific one is available)
- All external links must use `target="_blank" rel="noopener"`
- Clarity tag ID for analytics is TBD — leave a `<!-- TODO: Clarity tag ID -->` comment in `<head>`
