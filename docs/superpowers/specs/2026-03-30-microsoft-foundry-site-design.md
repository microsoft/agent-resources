# Microsoft Foundry Resource Site — Design Spec
_Date: 2026-03-30_

## Overview

Create a new child site at `microsoft-foundry/` following the established pattern of the other resource hubs (m365-copilot, copilot-studio, agent365, develop-agents). The site provides curated learning resources for Microsoft AI Foundry — the Azure-based platform for building, evaluating, and deploying AI models and agents.

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

Based on the Azure AI Foundry icon's warm orange-to-amber palette — clearly distinct from the cool blues (M365 Copilot), purples (develop-agents), and indigos (Agent 365).

| Token | Value | Usage |
|-------|-------|-------|
| `--brand-deep` | `#7a2500` | Footer background, deep shadows |
| `--brand-mid` | `#c84b0a` | Hover states |
| `--brand-accent` | `#e07020` | Links, badges, focus rings |
| `--brand-light` | `#f5a623` | Session grid hover borders |
| `--teal-accent` | `#f5c842` | Accent highlights |
| `--surface-alt` | `#fff8f0` | Section hover backgrounds |
| `--surface-hover` | `#ffeedd` | Link list row hover |
| `--border` | `#f5d9b8` | Card borders |
| Shadow colors | `rgba(122,37,0,…)` | Replaces blue-tinted shadows |

**Hero gradient:** `135deg, #c84b0a 0%, #e07020 30%, #f5a623 65%, #fcd385 100%`

**Hero overlay radial gradients** (the `::before` ambient layer): two ellipses using the burnt-orange and amber values, mirroring the pattern from other sites.

**Search bar text/placeholder colors:** warm dark (`#3d1500`) instead of the indigo dark used in agent365.

---

## Sections (11 total)

Nav strip order matches section order.

### 1. Get Started
**ID:** `get-started` | **Nav label:** Get Started

What is Microsoft AI Foundry, where to find official docs, a quickstart, and an overview video. Mirrors the "I am new" framing from Copilot Studio but uses a direct title.

Content:
- What is Microsoft AI Foundry? (overview doc link)
- Official documentation hub (`learn.microsoft.com/azure/ai-foundry`)
- Quickstart: create a project in Foundry
- Overview / intro video
- Product page / marketing site
- Azure AI Foundry in the Azure portal (direct link)
- Key concepts: projects, hubs, connections, deployments

### 2. News & Announcements
**ID:** `news` | **Nav label:** News

Latest blog posts, feature releases, and conference announcements (Build, Ignite).

Content:
- Azure AI Blog (`techcommunity.microsoft.com/category/azure-ai-services/blog/azure-ai-services-blog`)
- What's new in Azure AI Foundry (release notes / changelog page)
- Ignite and Build announcement blog posts (by date, most recent first)
- Microsoft AI platform announcements section in Book of News where applicable

### 3. Successful Adoption
**ID:** `adoption` | **Nav label:** Adoption

Guidance and frameworks for organizations adopting Foundry at scale — change management, planning, CAF adoption scenarios.

Content:
- Cloud Adoption Framework: AI adoption scenario for Azure AI Foundry
- Azure AI Foundry adoption guide / deployment accelerator (if available)
- Planning and readiness resources
- Organizational readiness for AI workloads

### 4. Training & Certification
**ID:** `training` | **Nav label:** Training

Microsoft Learn paths, instructor-led training, hands-on labs, and formal certifications relevant to Foundry.

Content:
- **Learn paths:** "Get started with Azure AI Foundry", Azure AI Engineer path
- **Certifications:**
  - AI-102: Designing and Implementing a Microsoft Azure AI Solution
  - DP-100: Designing and Implementing a Data Science Solution on Azure
  - AI-050: Develop Generative AI solutions (if applicable)
- **Labs:** Applied Skills for Azure AI Foundry / generative AI
- **Microsoft Learn sandbox** / guided exercises

### 5. Build with Foundry
**ID:** `building` | **Nav label:** Build

Developer-facing resources for building applications and agents using Foundry's core tooling — prompt flow, the Azure AI Agent Service, the Foundry SDK, and related tools.

Content:
- Azure AI Agent Service documentation
- Prompt Flow: getting started, authoring flows
- Foundry SDK (Python, JavaScript, .NET) — reference and quickstart
- Azure AI Foundry VS Code extension
- MCP (Model Context Protocol) integration with Foundry
- Evaluation SDK (developer-oriented evaluation tooling)
- Tracing and observability for AI apps
- RAG (retrieval-augmented generation) patterns and how-tos

### 6. Models & Services
**ID:** `models` | **Nav label:** Models

The model catalog, Azure OpenAI Service, and the broader AI services portfolio accessible from Foundry.

Content:
- **Model catalog:** browse and deploy models from Azure AI Foundry
- **Azure OpenAI Service:** docs hub, model reference (GPT-4o, o-series, etc.)
- **Azure AI Services:** vision, speech, language, document intelligence, content safety
- Serverless API deployments (MaaS) vs. managed compute (MaaP)
- Model benchmarks and comparisons
- What's new in Azure OpenAI

### 7. Evaluate & Improve
**ID:** `evaluate` | **Nav label:** Evaluate

Resources for measuring, improving, and governing AI model and application quality — evaluations, fine-tuning, content safety, and monitoring.

Content:
- Evaluation in Azure AI Foundry (built-in evaluators, custom evaluators)
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
- **CAF:** Azure AI Foundry adoption scenario in Cloud Adoption Framework
- **WAF:** AI workload guidance in Azure Well-Architected Framework
- Azure AI Foundry landing zone accelerator
- Azure AI Foundry reference architectures (RAG baseline, multi-agent, etc.)
- Security baseline for Azure AI Foundry
- Network isolation and private endpoints
- Identity and access management for Foundry
- Cost management and optimization

### 9. Real-World Customer Stories
**ID:** `stories` | **Nav label:** Stories

Published case studies, partner success stories, and customer showcases using Azure AI Foundry.

Content:
- Azure customer stories filtered to AI Foundry
- Partner spotlights
- Industry-specific implementations (healthcare, finance, retail, etc.)

### 10. Samples
**ID:** `samples` | **Nav label:** Samples

GitHub repositories, solution accelerators, notebooks, and templates.

Content:
- `azure-samples/azureai-samples` — official samples repo
- Azure AI Foundry solution accelerators
- Prompt Flow sample flows gallery
- Azure OpenAI samples
- RAG solution accelerators
- Multi-agent sample applications
- Azure AI Foundry GitHub org overview

### 11. Community & Support
**ID:** `community` | **Nav label:** Community

Tech Community blog, GitHub Discussions, support channels, and office hours.

Content:
- Azure AI Tech Community (`techcommunity.microsoft.com/category/azure-ai-services`)
- Azure AI Foundry GitHub Discussions
- Azure AI Foundry feedback / UserVoice
- Azure support options
- Office hours / live Q&A sessions (if recurring)
- AI Foundry Discord or community channels (if applicable)

---

## OG / Social Metadata

- `og:title`: "Microsoft AI Foundry Resources"
- `og:description`: "Curated learning materials to help you build, evaluate, and deploy AI models and agents with Microsoft AI Foundry — curated by the Microsoft Copilot Acceleration Team (CAT)."
- `og:image`: `microsoft-foundry/images/og-image.png` (1200×630, to be created)
- Clarity tag ID: TBD (new tag needed for this site)

---

## Root Hub Update

The root `index.html` will need a new card added for Foundry (`card-foundry` class with orange accent color), pointing to `microsoft-foundry/`. This is a separate task and not part of this spec.

---

## Constraints

- No build step — plain HTML/CSS/JS only
- `main.js` must be an identical copy of the shared script (per CLAUDE.md)
- `favicon.ico` is required (copy from another site as placeholder until a Foundry-specific one is available)
- All external links must use `target="_blank" rel="noopener"`
- Clarity tag ID for analytics is TBD — leave a `<!-- TODO: Clarity tag ID -->` comment in `<head>`
