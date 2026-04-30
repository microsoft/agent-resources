# Changelog

All notable changes to the Agent Resources sites are documented in this file.

## 2026-04-30

### m365-copilot/
- **Real-world customer stories** — added new "Stories" section with curated collections (`aka.ms/AgentStories`, AI transformation stories hub, full M365 Copilot customer index, AI customer stories), featured stories (JCB, ECE Group, Wipro, LTM), and Microsoft blog roundups (1,000+ stories Cloud blog post, Revolutionizing work / Eaton). Added `#stories` nav link and `.icon-stories` style.

### copilot-studio/
- **Real-world customer stories** — updated curated customer stories link from `aka.ms/CopilotAgentStories` to `aka.ms/AgentStories`

## 2026-04-24

### / (root)
- **Architecture** — consolidated the five byte-identical `assets/js/main.js` files into a single shared file at the repo root (`assets/js/main.js`). Each child `index.html` now references `../assets/js/main.js`. Removes ~230 duplicated lines and the "keep in sync" convention. Updated `README.md`, `CLAUDE.md`, and `.github/copilot-instructions.md` to document the new shared layout.
- **README.md** — rewrote from a single heading into a full project overview: what the hub is, per-site table with short URLs, feature list, local-preview instructions, contribution conventions (CHANGELOG, shared `main.js`, Clarity tag IDs, OG image regeneration), architecture diagram, credits, and license/policy links
- **og-image** — regenerated as `images/og-image-v2.png` (renamed from `og-image.png` to bust LinkedIn/Facebook/Twitter OG caches) with a refreshed brand-aligned design showing all five product destinations (M365 Copilot, Copilot Studio, Microsoft Foundry, Agent Framework, Agent 365); updated `og:image` and `twitter:image` meta tags in `index.html`; added `scripts/generate_og_image.py` to make the image reproducible
- Fixed front-door short URL reference in `CLAUDE.md` and `.github/copilot-instructions.md` (aka.ms/airesources → aka.ms/agentresources)

### m365-copilot/
- **News and announcements** — added 4 entries: Copilot's agentic capabilities in Word/Excel/PowerPoint now GA (Apr 22), "Bring your everyday business apps into the flow of work with agents" covering Adobe Express / Figma / Optimizely / Dynamics 365 (Apr 13), M365 Copilot readiness and resiliency with SharePoint + M365 Backup (Tech Community), ICYMI Frontier Transformation and Wave 3 recap (Tech Community)
- **Copilot Cowork → Official announcements** — added 2 entries: "Available today: Anthropic Claude Opus 4.7 in Microsoft 365 Copilot" (Cowork + Studio + Excel) and Microsoft Mechanics blog "Claude + GPT: Multi-model intelligence in Copilot" covering Cowork, Work IQ, mid-run task injection, and Model Council
- **Copilot Cowork → MVP & community posts** — added 2 entries: Tom Arbuthnot's April 2026 Microsoft 365 AI Workplace Update and Rob Quickenden's "How to create Custom Skills in Copilot Cowork" (markdown SKILL.md files in OneDrive)
- **Copilot Cowork → Videos** — added Jeremy Chapman (Microsoft Mechanics) "Claude + GPT: Multi-model intelligence in Copilot" — Cowork briefing/deck/Excel generation, mid-run task injection, Work IQ auto-retrieval, Researcher Critique, Model Council
- **Extensibility → Get started extending Copilot** — added Voitanos (Andrew Connell) deep-dive on April 2026 declarative agent upgrades: MCP Apps, embedded knowledge, Agents Toolkit plugin

### copilot-studio/
- **Stay up to date on news and features** — added 2 entries: "New and improved: Multi-agent orchestration, connected experiences, and faster prompt iteration" (multi-agent GA across Fabric, M365 Agents SDK, A2A protocols) and the 2026 release wave 1 overview + planned features on Microsoft Learn
- **Community and support** — added launch of the Copilot Studio Tech Community Blog (`aka.ms/MCSblog`) — dedicated space for builders/admins on templates, governance, extensibility, and production operations

### agent365/
- **News and announcements** — added "Save the date for Agent 365 Live AMA" (Tech Community, Apr 15) — official team announcement for the May 12 AMA
- **Community and support → MVP and community blogs** — added Steve Corey's "Microsoft Agent 365: The Features Nobody Is Talking About (But Should Be)" (Apr 8) — deep-dive on MCP server interoperability, agentic authentication, and agent instancing

### develop-agents/
- **Microsoft SDKs → Microsoft Agent Framework** — added 2 entries: Microsoft Agent Framework **Version 1.0** release announcement (Apr 3) and Foundry **"From Local to Production"** developer journey post (Apr 22)
- **Learning and videos → Blog posts & articles** — added 10 April 2026 entries: Agent Framework 1.0 announcement, Foundry "From Local to Production", "Introducing Toolboxes in Foundry", "Introducing the new hosted agents in Foundry Agent Service", "Agent Skills in .NET: Three Ways to Author", "Building a Real-Time Multi-Agent UI with AG-UI", "CodeAct in Agent Framework", "Chat History Storage Patterns in Microsoft Agent Framework", M365 Dev Blog "MCP Apps now available in Copilot chat", and Voitanos "What's new with M365 Copilot declarative agents — April 2026"

### microsoft-foundry/
- **News and announcements** — added 2 entries: "What's new in Microsoft Foundry | March 2026" monthly roundup (Apr 9) and "What's new in Foundry Labs | April 2026" (MAI-Transcribe-1, MAI-Voice-1, MAI-Image-2)
- **Building with Foundry → Azure AI Agent Service** — added 2 entries: "Introducing hosted agents in Foundry Agent Service" (Apr 22) and "Introducing Toolboxes in Foundry" (Apr 22)
- **Building with Foundry → Foundry Local** — added "Foundry Local is now Generally Available" (Apr 9)
- **Building with Foundry → Microsoft Agent Framework** — added "From Local to Production: the complete developer journey for AI agents" (Apr 22) — Agent Framework v1.0 + Foundry Toolkit for VS Code GA
- **Evaluations and fine-tuning → Fine-tuning blogs** — added "What's New in Microsoft Foundry Fine-Tuning | April 2026" (Apr 16) — Global Training for o4-mini, GPT-4.1 model graders, RFT best practices

## 2026-04-09

### agent365/
- **Get Started** — added "Introducing Microsoft Agent 365" video and "Use and collaborate with agents" end-user guide
- **Get Started** — updated "Agent 365 Overview" entry to credit John Savill's Technical Training
- **News** — added Microsoft Entra innovations at RSAC 2026 blog post and RSAC 2026 shadow AI protection announcement
- **Developer** — added "Introduction to Agent 365 SDK" video
- **Community** — added Agent 365 Discussions forum link and new "MVP and community blogs" sub-section with 8 entries: Jukka Niiranen FAQ site, Rob Quickenden GA deep-dive and Ignite recap, Simon Doy first-agent walkthrough, Steve Corey dashboard walkthrough video, Corsica Tech governance article, Devoteam expert view, IT PRO analyst overview

## 2026-04-07

### m365-copilot/
- **News section** — added 3 Cowork entries: "Copilot Cowork: Now available in Frontier", "Copilot Cowork: A new way of getting work done", "What's New in Microsoft 365 Copilot — March 2026"
- Swapped section order in nav and page: Training now appears before Adoption

### copilot-studio/
- Updated "Agent in a Day" links to short URL `https://aka.ms/AgIAD` in Get Started and Adoption sections

## 2026-04-06

### m365-copilot/
- **New section: Copilot Cowork** — added nav item and full section with four sub-headings:
  - *Overview* — 4 documentation entries: Cowork overview, Get started, Use Cowork, FAQ
  - *Official announcements* — 4 entries: "Now available in Frontier" blog, "A new way of getting work done" blog, Charles Lamanna LinkedIn demo post, Charles Lamanna TBPN Live LinkedIn post
  - *MVP & community posts* — 4 entries: Rob Quickenden MVP walkthrough, Christian Buckley MVP/RD strategic analysis, Tom Arbuthnot MVP March 2026 roundup, C5 Insight plan-act-approve explainer
  - *Videos* — Lisa Crosbie explainer, John Savill walkthrough
- Moved Copilot Cowork out of the Agents → Frontier sub-section into its own dedicated section

### copilot-studio/
- **New section: Governance and administration** — added nav item and full section with four sub-headings:
  - *Documentation* — 14 entries covering security/governance overview, governance architecture models, DLP policy config, zoned governance strategy, sharing controls, tenant-wide agent inventory, Purview audit logs, monitoring/compliance, licensing & capacity, ALM strategy, security maturity model, Copilot Studio Kit Compliance Hub, PPAC Copilot Hub, and Global Secure Access
  - *Official blog posts* — 6 entries: Agent Governance Whitepaper, March 2025 managed governance launch, robust security for agents post, and three Ignite 2025 recaps (Copilot Control System, AI admin capabilities, security & governance innovations)
  - *Build 2025 sessions* — BRK159: Secure and govern your enterprise-scale agents
  - *Ignite 2025 sessions* — BRK293 (oversharing/oversight), BRK324 (Power Platform governance), PBRK307 (managed solutions), THR759 (Copilot Trust & Safety)
  - *Community and MVP resources* — 4 entries: two Ragnar Heil MVP posts (governance best practices + DLP tips), Mikko Koskinen's governance checklist, powertricks.io complete admin reference

## 2026-03-31

### Root hub (/)
- Added **Agent Platform Advisor** card — links to the interactive tool that helps users choose the right platform for their agent scenario

### develop-agents/
- **New section: Learning and videos** — added nav item and full section with five sub-headings:
  - *Courses & curricula* — AI Agents for Beginners course, Agent Framework lesson, Microsoft Learn get-started guide, Generative AI for Beginners .NET v2, M365 Agents SDK training path, Copilot Developer Camp labs
  - *Microsoft Build 2025* — Agent Framework session, Agent Factory session, keynote blog, full YouTube playlist, Book of News
  - *Microsoft Ignite 2025* — full YouTube playlist, Copilot & agents playlist, LAB513, LAB518, BRK319 Agents Toolkit session, Ignite developer guide blog
  - *Video tutorials* — On .NET Live, KodeKloud complete course, Tech with Kirk, .NET tutorials, BRK319 session, Voitanos Build 2025 recap
  - *Blog posts & articles* — 21 entries covering official Microsoft blogs (Foundry, .NET, Azure, Tech Community, Developer Blog), MVP posts (Johan Rin, Anuraj, Anto Subash), migration guides, Visual Studio Magazine, Nanddeep Nachan, AI ML Insider, M365 Dev Blog posts
- **Enhanced Microsoft Agent Framework sub-section** — added 9 entries: Foundry blog deep-dive, .NET Blog post, SK↔MAF relationship blog, Workflows documentation, Framework overview, Agent-Framework-Samples repo, real-world example walkthrough, Multi-Agent Reference Architecture, orchestration patterns post
- **Enhanced Microsoft 365 Agents SDK sub-section** — added 7 entries: SDK overview, Agents Toolkit blog, custom engine agents guide, create & deploy guide, Bot Framework migration guide, Microsoft Learn training path, Agents Toolkit overview
- **Enhanced Samples section** — added 5 entries: Agent-Framework-Samples repo, Ignite LAB513, LAB518, Build25-BRK117, multi-agent reference architecture
- **Enhanced Community section** — added 4 entries: Agent Framework team blog, Agent Framework GitHub Discussions, M365 Agents SDK blog tag feed, M365 Agents SDK GitHub Discussions

### m365-copilot/
- **Enhanced Agent Builder section** — expanded from 2 sub-headings (5 entries) to 6 sub-headings (21 entries):
  - *Get started* — added Agent Builder overview, Microsoft Support walkthrough, Agent Builder vs Copilot Studio decision guide
  - *Templates & examples* — added Awesome Copilot Studio Agents community gallery
  - *Share, manage & govern* (new) — 6 entries covering sharing/publishing, admin center management, agents admin guide, deployment checklist, governance whitepaper, admin experience blog
  - *Videos & tutorials* (new) — 4 entries: official Microsoft walkthrough, Lisa Crosbie tutorial, HelpingAll guide, Agent Academy
  - *Blog posts & articles* (new) — 2 entries: Agent Builder vs Studio vs Foundry comparison, Copilot pricing/licensing

### copilot-studio/
- **Enhanced Building section** — added "Autonomous agents & advanced capabilities" sub-heading with 6 entries: autonomous agent capabilities, agent flows, Build 2025 multi-agent announcements, CUA computer use, Microsoft Mechanics video, Agent Governance Whitepaper
- **Enhanced News section** — added 4 entries: March 2025 recap, autonomous agents blog, agent flows blog, Build 2025 multi-agent orchestration blog
- **Enhanced Community section** — added 2 entries: Power Platform community walkthrough, Agent Academy
- Fixed MCS Labs link

### agent365/
- **Enhanced News section** — added 2 entries: Build 2025 announcement blog, Agent Governance Whitepaper
- **Enhanced Admin section** — added "Agent governance resources" sub-heading with 4 entries: M365 agents checklist, governance whitepaper, admin center management, new admin experience blog
- **Enhanced Security section** — added "Governance and compliance" sub-heading with Purview security blog post
- **Enhanced Developer section** — added 2 entries: documentation hub, product overview
- **Enhanced Community section** — added 2 entries: documentation hub, YouTube playlist

### microsoft-foundry/
- **Enhanced Build section** — added 4 entries to Azure AI Agent Service (GA announcement, Tech Community deep-dive, Ignite 2025 recap, product page) and new "Microsoft Agent Framework" sub-heading with 4 entries (documentation, GitHub repo, Foundry DevBlog announcement, real-world example walkthrough)
- **Enhanced News section** — added 2 entries: Foundry Agent Service GA, Agent Framework introduction
- **Enhanced Community section** — added 2 entries: Foundry DevBlog, Agent Framework team blog

## 2026-03-30

### Root hub (/)
- Added Microsoft Foundry card to root hub
- Reordered hub cards — Foundry to 3rd position, Agent 365 to 5th
- Renamed Developer Resources card, simplified Ignite URLs

### microsoft-foundry/ (new site)
- Scaffolded full Microsoft Foundry resource site with 11 sections:
  - Get Started, News, Adoption, Training, Build, Models, Evaluate, Architecture, Stories, Samples, Community
- Added cobalt blue color scheme in `styles.css`
- Populated all sections with documentation, blog posts, tutorials, samples, and reference architectures
- Added Ignite 2025 sessions across 5 sections
- Added Build 2025 sessions
- Added fine-tuning resources: blogs, videos, samples, and advanced techniques (RFT, distillation, DPO)
- Added Foundry Local (on-device inference) resources
- Added Model Router resources
- Added evaluation and responsible AI resources

### All sites — design and accessibility improvements (round 2)
- Replaced `transition: all` with explicit properties for performance
- Added `prefers-reduced-motion` support
- Increased footer link touch targets
- Bumped body text to 16px minimum
- Added scroll fade affordance to nav strip
- Differentiated duplicate icon colors

### develop-agents/
- Differentiated duplicate icon colors in section headers

### All sites
- Fixed hash nav scrolling behind sticky nav (ISSUE-001)

## 2026-03-26

### Root hub (/)
- Fixed H1 text overflow on mobile
- Replaced rainbow gradient with brand colors
- Fixed orphaned 4th card with 2×2 grid layout
- Added tablet breakpoint (641–1024px)
- Added spacing and font-size design tokens
- Flattened icon gradients and left-aligned root hero
- Removed `text-wrap: balance` from root H1
- Removed `max-width` constraint from hero-inner

### All sites — design and accessibility improvements (round 1)
- Fixed broken HTML in footer and hero elements
- Increased CTA badge touch target size
- Added `focus-visible` styles across all sites
- Used semantic H2 for card titles
- Increased footer link touch target padding
- Aligned copyright text with child sites
- Increased touch targets on hero-back and nav-strip
- Normalized Copilot Studio `main.js` formatting

## 2026-03-25

### All sites
- Updates for clarity across content

## 2026-03-20

### agent365/
- Updated Agent 365 text

## 2026-03-19

### copilot-studio/
- Fixed subheader

## 2026-03-18

### develop-agents/ (new site)
- Created Agent Developer Resources site (initially named `agent-developer/`)
- Added SDK resources: Semantic Kernel, Foundry Agent Service, Microsoft Agent Framework, M365 Agents SDK, Copilot Studio developer tools, Agent 365 SDK
- Added Protocols & Standards section (A2A, MCP)
- Added Open Source & Third-party section (LangChain, AutoGen, CrewAI, LlamaIndex)
- Added Samples and Community sections
- Renamed directory from `agent-developer/` to `develop-agents/`
- Removed `en-us` locale from documentation URLs

### agent365/
- Added Agent 365 AMA link

## 2026-03-17

### All sites
- Merged the three agent resources sites (M365 Copilot, Copilot Studio, Agent 365) into one repository
- Added home button navigation between sites
- Standardized site structure

## 2026-03-16

### Root hub (/)
- Initial site with hero, product cards, and footer
- Added Open Graph metadata and footer

## 2026-03-13

- Repository created with initial commit
- Added README, MIT License, Code of Conduct, and Security policy
