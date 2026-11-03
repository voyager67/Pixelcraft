<div align="center">

# PIXELCRAFT
### Detect the tells. Fix the design.

**A focused AI-slop recognition and remediation skill library for ChatGPT, Codex, and compatible agents.**

[![Skills](https://img.shields.io/badge/skills-51-6C5CE7?style=for-the-badge)](#the-skill-library)
[![Targets](https://img.shields.io/badge/ChatGPT-Codex-111827?style=for-the-badge)](#quick-start)
[![License](https://img.shields.io/badge/original%20skills-CC%20BY--NC%204.0-0F766E?style=for-the-badge)](LICENSES/CC-BY-NC-4.0.txt)
[![Security](https://img.shields.io/badge/security-audit%20included-16A34A?style=for-the-badge)](SECURITY.md)

</div>

---

> AI can generate a screen in seconds. Pixelcraft helps an agent recognise when that screen is generic, inconsistent, misleading, or unfinished—and improve it with evidence, not random decoration.

## What Pixelcraft is

Pixelcraft is a specialized skill library for **recognising and removing AI slop from interfaces**. It covers visual clichés, template convergence, spacing, typography, color, icons, copy, imagery, charts, dashboards, landing pages, responsive layouts, interactions, forms, empty states, and design-system drift.

It is not an AI-authorship detector. A purple gradient, a rounded card, or an emoji does not prove that AI created a screen. Pixelcraft evaluates observable design quality and asks whether each choice serves the product and its users.

## The skill library

**51 focused skills.** Use `unslop-ui` for an end-to-end pass, or select a specialist for a specific problem.

| Area | Skills |
|---|---|
| Detection & diagnosis | `slop-detection`, `slop-audit`, `slop-severity-triage`, `visual-cliche-detection`, `template-convergence-review` |
| Visual cleanup | `effects-overuse-repair`, `card-bloat-repair`, `spacing-rhythm-repair`, `typography-slop-repair`, `color-system-repair`, `emoji-icon-cleanup`, `visual-hierarchy-repair`, `content-density-repair` |
| Copy & trust | `microcopy-slop-repair`, `ai-copy-tell-review`, `fabricated-proof-detector` |
| Data & dashboards | `chart-slop-repair`, `dashboard-slop-repair`, `data-viz-integrity-repair`, `table-density-repair` |
| Pages & flows | `landing-page-slop-repair`, `hero-visual-repair`, `ecommerce-ui-slop-repair`, `pricing-page-slop-repair`, `onboarding-ui-slop-repair`, `settings-page-slop-repair` |
| Interaction & accessibility | `interaction-state-repair`, `form-ui-slop-repair`, `empty-state-repair`, `navigation-slop-repair`, `modal-dialog-slop-repair`, `button-cta-slop-repair`, `accessibility-slop-repair`, `motion-slop-repair` |
| Responsive & assets | `responsive-slop-repair`, `mobile-ui-slop-repair`, `visual-asset-slop-audit`, `synthetic-image-cliche-review`, `illustration-and-icon-slop-review`, `screenshot-redline-review` |
| Design system & code | `product-specific-direction`, `component-consistency-repair`, `token-sprawl-repair`, `tailwind-slop-cleanup`, `react-ui-slop-refactor`, `design-system-slop-repair`, `multi-page-consistency-review` |
| Verification | `slop-remediation-quality-gate`, `visual-regression-guard`, `slop-regression-review` |

See every skill's `SKILL.md` for activation guidance, workflow, constraints, and completion criteria.

## Quick start

### Codex — user-wide install

```bash
git clone https://github.com/voyager67/pixelcraft.git
cd pixelcraft
./scripts/install_codex_skills.sh user
```

### Codex — project-local install

```bash
./scripts/install_codex_skills.sh project /path/to/your-project
```

### ChatGPT

In ChatGPT surfaces with Skills enabled, type `@` and select a skill, or let its description match the task. In Codex, use `/skills` to inspect available skills or `$skill-name` to invoke one. If your ChatGPT environment has no skill importer, attach the selected `SKILL.md` or paste it into project instructions. To package individual skill folders for compatible skill importers, run `python3 scripts/package_skills.py`; it creates one ZIP per skill and requires no API key. See the official [Codex skill guide](https://developers.openai.com/codex/build-skills).

### Try it

```text
Use slop-detection on this screen. Inspect the actual rendered UI if possible.
List observable patterns, evidence, confidence, user impact, and benign explanations.
Do not guess whether a human or AI authored it.
```

```text
Use unslop-ui on this dashboard. Preserve functionality and real content.
Audit first, derive a product-specific direction, fix in ordered passes, and verify mobile.
```

```text
Use fabricated-proof-detector on this landing page. Verify every metric, testimonial,
logo, rating, and integration claim against supplied evidence. Do not invent replacements.
```

## Full skill index

| Skill | Focus |
|---|---|
| [`accessibility-slop-repair`](skills/accessibility-slop-repair/SKILL.md) | Finds accessibility failures frequently introduced by decorative AI UI: low-contrast text, icon-only buttons, missing labels, fake controls, focus traps, and color-only status. |
| [`ai-copy-tell-review`](skills/ai-copy-tell-review/SKILL.md) | Reviews UI and marketing copy for common synthetic-writing tells such as vague superlatives, formulaic parallelism, empty benefits, and repetitive cadence. |
| [`button-cta-slop-repair`](skills/button-cta-slop-repair/SKILL.md) | Fixes generic or misleading buttons and calls to action, including vague labels, duplicate primaries, decorative button variants, and weak action feedback. |
| [`card-bloat-repair`](skills/card-bloat-repair/SKILL.md) | Finds and fixes over-cardification: unnecessary panels, nested cards, stat tiles, pill containers, and surfaces that fragment content without adding structure. |
| [`chart-slop-repair`](skills/chart-slop-repair/SKILL.md) | Repairs decorative or misleading chart components, rainbow palettes, meaningless sparklines, unexplained axes, and dashboard chart clutter. |
| [`color-system-repair`](skills/color-system-repair/SKILL.md) | Repairs arbitrary color usage, over-saturated accents, gradients, low contrast, inconsistent semantic colors, and AI-style rainbow interfaces. |
| [`component-consistency-repair`](skills/component-consistency-repair/SKILL.md) | Finds visually similar components implemented with inconsistent padding, radius, typography, variants, and state behavior; repairs component drift. |
| [`content-density-repair`](skills/content-density-repair/SKILL.md) | Balances information density when AI-built interfaces are either excessively sparse with decorative whitespace or overcrowded with repeated cards and labels. |
| [`dashboard-slop-repair`](skills/dashboard-slop-repair/SKILL.md) | De-generifies AI-built dashboards by removing meaningless stat cards, redundant charts, generic greetings, ungrounded trends, and weak information hierarchy. |
| [`data-viz-integrity-repair`](skills/data-viz-integrity-repair/SKILL.md) | Reviews charts and data visualizations for misleading scale, arbitrary color, fake sample numbers, unexplained units, inaccessible encodings, and visual noise. |
| [`design-system-slop-repair`](skills/design-system-slop-repair/SKILL.md) | Repairs inconsistent, overgrown, and token-poor design systems that produce repetitive AI UI slop across multiple pages. |
| [`ecommerce-ui-slop-repair`](skills/ecommerce-ui-slop-repair/SKILL.md) | Repairs generic e-commerce UI patterns such as fake urgency, redundant product cards, ambiguous pricing, noisy badges, weak filters, and low-trust checkout affordances. |
| [`effects-overuse-repair`](skills/effects-overuse-repair/SKILL.md) | Reduces gratuitous gradients, glows, blur, glassmorphism, shadows, borders, and decorative effects while preserving intentional brand expression. |
| [`emoji-icon-cleanup`](skills/emoji-icon-cleanup/SKILL.md) | Identifies emoji-as-icon, mixed icon families, inconsistent sizes, and decorative glyphs; replaces them with a consistent semantic icon system. |
| [`empty-state-repair`](skills/empty-state-repair/SKILL.md) | Replaces generic empty-state filler and decorative illustrations with clear explanations, next actions, and honest zero-data states. |
| [`fabricated-proof-detector`](skills/fabricated-proof-detector/SKILL.md) | Finds unsupported testimonials, logos, customer counts, ratings, benchmark claims, trust badges, and fictional metrics in AI-built UI and marketing pages. |
| [`form-ui-slop-repair`](skills/form-ui-slop-repair/SKILL.md) | Repairs generic and incomplete AI-built forms, including placeholder-only labels, excessive fields, unclear validation, weak errors, and ambiguous submit actions. |
| [`hero-visual-repair`](skills/hero-visual-repair/SKILL.md) | Recognizes generic AI hero visuals and rebuilds the first screen around product meaning, composition, credible imagery, and clear text placement. |
| [`illustration-and-icon-slop-review`](skills/illustration-and-icon-slop-review/SKILL.md) | Finds inconsistent illustration languages, random 3D icon sets, mismatched stroke styles, and decorative icon clutter in AI-built interfaces. |
| [`interaction-state-repair`](skills/interaction-state-repair/SKILL.md) | Finds polished-looking but fake or incomplete interactions in AI-built UI and adds coherent behavior for focus, loading, disabled, success, empty, and error states. |
| [`landing-page-slop-repair`](skills/landing-page-slop-repair/SKILL.md) | Fixes generic AI-generated landing pages: centered-template heroes, vague value propositions, repetitive feature cards, fake social proof, and weak product demonstrations. |
| [`microcopy-slop-repair`](skills/microcopy-slop-repair/SKILL.md) | Rewrites generic, hype-heavy, repetitive, or robotically phrased UI copy into concise and product-specific interface language. |
| [`mobile-ui-slop-repair`](skills/mobile-ui-slop-repair/SKILL.md) | Improves mobile interfaces that look like desktop layouts compressed into a phone, with cramped cards, tiny charts, oversized headers, and awkward navigation. |
| [`modal-dialog-slop-repair`](skills/modal-dialog-slop-repair/SKILL.md) | Finds overused or poorly structured AI-built modals, oversized dialog shells, unclear actions, missing focus management, and destructive confirmation noise. |
| [`motion-slop-repair`](skills/motion-slop-repair/SKILL.md) | Removes gratuitous animation, pulsing, parallax, hover theatrics, and scroll effects while preserving motion that explains state or spatial relationships. |
| [`multi-page-consistency-review`](skills/multi-page-consistency-review/SKILL.md) | Finds cross-route AI design drift, inconsistent components, typography, spacing, icon usage, navigation, and repeated generic sections across an application. |
| [`navigation-slop-repair`](skills/navigation-slop-repair/SKILL.md) | Identifies and repairs bloated sidebars, generic navigation labels, arbitrary icons, nested menu clutter, and inconsistent active states. |
| [`onboarding-ui-slop-repair`](skills/onboarding-ui-slop-repair/SKILL.md) | Repairs generic onboarding flows with excessive steps, vague progress, forced personalization, fake welcome screens, and unclear setup completion. |
| [`pricing-page-slop-repair`](skills/pricing-page-slop-repair/SKILL.md) | Finds generic SaaS pricing-table slop: arbitrary plan tiers, feature-checkmark walls, misleading savings, fake popularity, and unclear billing terms. |
| [`product-specific-direction`](skills/product-specific-direction/SKILL.md) | Derives a distinctive visual direction from an existing product so AI-assisted redesigns stop collapsing into generic template aesthetics. |
| [`react-ui-slop-refactor`](skills/react-ui-slop-refactor/SKILL.md) | Refactors React UI code that produces generic or inconsistent screens, including giant components, duplicated markup, ad hoc variants, and state styling drift. |
| [`responsive-slop-repair`](skills/responsive-slop-repair/SKILL.md) | Finds and fixes responsive slop such as desktop UI squeezed into mobile, overflow, hidden content, awkward stacking, and broken fixed elements. |
| [`screenshot-redline-review`](skills/screenshot-redline-review/SKILL.md) | Performs a visual redline pass from screenshots or browser captures, mapping visible AI-slop patterns to precise implementation changes. |
| [`settings-page-slop-repair`](skills/settings-page-slop-repair/SKILL.md) | Repairs bloated settings pages with arbitrary cards, inconsistent toggles, unclear categories, hidden save behavior, and decorative controls. |
| [`slop-audit`](skills/slop-audit/SKILL.md) | Produces a detailed evidence-based AI-slop audit of one or more UI screens, grouping findings by visual, content, interaction, and implementation symptoms. |
| [`slop-detection`](skills/slop-detection/SKILL.md) | Detects observable AI-slop patterns in UI screenshots, live interfaces, and frontend code without claiming to determine authorship. Use for first-pass recognition across a product surface. |
| [`slop-regression-review`](skills/slop-regression-review/SKILL.md) | Reviews later AI-generated changes for reintroduced slop patterns and protects the design decisions established by a previous remediation pass. |
| [`slop-remediation-quality-gate`](skills/slop-remediation-quality-gate/SKILL.md) | Verifies an AI-slop remediation pass has actually improved the interface without breaking behavior, accessibility, responsiveness, or product identity. |
| [`slop-severity-triage`](skills/slop-severity-triage/SKILL.md) | Ranks AI-slop findings by user harm, trust impact, visibility, recurrence, and repair effort. Use after a slop audit to decide what to fix first. |
| [`spacing-rhythm-repair`](skills/spacing-rhythm-repair/SKILL.md) | Detects arbitrary margins, padding, gaps, row heights, and alignment drift that make AI-built interfaces feel uneven; repairs the spacing rhythm. |
| [`synthetic-image-cliche-review`](skills/synthetic-image-cliche-review/SKILL.md) | Reviews illustrations and imagery for generic synthetic-looking visual tropes and recommends more product-specific art without claiming forensic AI-image detection. |
| [`table-density-repair`](skills/table-density-repair/SKILL.md) | Repairs AI-generated tables with weak alignment, inconsistent number formatting, needless card wrappers, excessive controls, and unreadable mobile behavior. |
| [`tailwind-slop-cleanup`](skills/tailwind-slop-cleanup/SKILL.md) | Cleans AI-generated Tailwind CSS marked by arbitrary values, class soup, duplicated utilities, inconsistent spacing, and fragile responsive overrides. |
| [`template-convergence-review`](skills/template-convergence-review/SKILL.md) | Detects when multiple screens or products converge on the same generic AI/SaaS template despite different purposes. Use for originality and differentiation reviews. |
| [`token-sprawl-repair`](skills/token-sprawl-repair/SKILL.md) | Finds duplicated, near-duplicate, unused, and contradictory design tokens produced by iterative AI edits and consolidates them into a coherent system. |
| [`typography-slop-repair`](skills/typography-slop-repair/SKILL.md) | Fixes AI-looking typography: arbitrary font stacks, too many weights and sizes, shouty uppercase labels, compressed small text, weak hierarchy, and inconsistent number styles. |
| [`unslop-ui`](skills/unslop-ui/SKILL.md) | Turns generic, AI-looking interfaces into coherent, product-specific UI through an evidence-based audit and ordered redesign passes. Use when asked to unslop, polish, or redesign an existing screen while preserving product behavior. |
| [`visual-asset-slop-audit`](skills/visual-asset-slop-audit/SKILL.md) | Audits images, stock art, illustrations, textures, and product screenshots for generic, irrelevant, inconsistent, or misleading visual assets. |
| [`visual-cliche-detection`](skills/visual-cliche-detection/SKILL.md) | Finds generic visual clichés that make an interface feel interchangeable, including overused gradients, floating panels, glass cards, stock hero compositions, and ornamental badges. |
| [`visual-hierarchy-repair`](skills/visual-hierarchy-repair/SKILL.md) | Repairs flat or chaotic AI-built hierarchy by clarifying primary task, scan path, grouping, contrast, scale, and information density. |
| [`visual-regression-guard`](skills/visual-regression-guard/SKILL.md) | Creates a repeatable visual regression check for anti-slop redesigns so later AI edits do not reintroduce generic styles or damage established layouts. |

## How Pixelcraft works

1. **Inspect** the rendered screen and relevant code.
2. **Detect** concrete symptoms using the signal taxonomy in [`references/slop-signals.md`](references/slop-signals.md).
3. **Explain** evidence, confidence, impact, and plausible benign explanations.
4. **Prioritize** root causes above isolated cosmetic symptoms.
5. **Repair** the smallest effective set of changes while preserving real product behavior.
6. **Verify** responsive layout, accessibility, behavior, and visual consistency.
7. **Report** what changed and what could not be verified.

## Publish to GitHub

After extracting this repository into a new, empty directory, install and authenticate the GitHub CLI (`gh auth login`), review the files, and run:

```bash
./scripts/publish.sh
```

The script verifies the authenticated account is `voyager67`, runs both checks, refuses to overwrite an existing repository, creates a **public** `voyager67/pixelcraft` repository, and pushes the initial `main` branch. It never embeds or asks you to commit a token. It also configures the initial commit with GitHub's account-specific `noreply` email instead of reading your global Git email, and refuses to reuse an existing `.git` history. Review the script before running it.

## Security and privacy

Pixelcraft contains plain-text agent instructions and a small standard-library validation/security scanner. It does not require API keys, accounts, third-party services, telemetry, or runtime network access.

Before publishing or using it in a project:

- Run `python3 scripts/security_audit.py`.
- Read [`PRIVACY.md`](PRIVACY.md) before using the skills on private or customer projects.
- Run `python3 scripts/validate_skills.py`.
- Never commit `.env` files, credentials, customer data, screenshots containing personal information, or private source files.
- Do not paste secrets into issue reports or audit output. The scanner reports only file paths and line numbers, never matched values.

See [`SECURITY.md`](SECURITY.md) for limitations and reporting guidance. Static scanners cannot guarantee that a repository is free of all secrets; review the complete Git diff and enable GitHub secret scanning where available.

## Repository layout

```text
pixelcraft/
├── README.md
├── LICENSE
├── THIRD_PARTY_NOTICES.md
├── LICENSES/
├── references/
├── docs/
├── examples/
├── scripts/
│   ├── validate_skills.py
│   ├── security_audit.py
│   ├── install_codex_skills.sh
│   ├── package_skills.py
│   └── publish.sh
└── skills/
    └── <skill-name>/
        ├── SKILL.md
        └── agents/openai.yaml (ChatGPT/Codex display metadata)
```

## License

Original Pixelcraft skills and documentation are licensed **CC BY-NC 4.0** unless a file says otherwise. `skills/unslop-ui/SKILL.md` is an adaptation of Unslop by Damir Sokolovsky and remains under the original **CC BY 4.0** terms. See [`LICENSE`](LICENSE), [`LICENSES/`](LICENSES/), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). No blanket licence is imposed on third-party material.

Pixelcraft is independent and is not affiliated with or endorsed by Damir Sokolovsky, OpenAI, Anthropic, or GitHub.

## Contributing

Contributions should improve AI-slop recognition, evidence quality, or remediation. New generic product-management or unrelated coding skills do not belong here. Read [`CONTRIBUTING.md`](CONTRIBUTING.md).
