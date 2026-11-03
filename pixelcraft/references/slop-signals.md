# Observable AI-slop signal taxonomy

This taxonomy is a review aid, not an authorship detector. A signal can be appropriate in context; assess purpose, evidence, and user impact.

| Signal family | Common symptoms | What to verify |
|---|---|---|
| Template convergence | Identical centered hero, three feature cards, logo strip, testimonial band, repeated section rhythm | Does structure follow the product narrative or a default template? |
| Decorative surface noise | Gradient washes, glow, glass blur, neon borders, layered shadows | Does the effect communicate state, depth, or brand? |
| Container bloat | Cards around every paragraph, nested surfaces, pill badges, isolated stat tiles | Does each container represent a meaningful object or group? |
| Token entropy | Arbitrary gaps, radii, colors, font sizes, one-off overrides | Are values semantic and repeated consistently? |
| Typography drift | Too many weights, wide tracked labels, tiny metadata, inconsistent numbers | Can the hierarchy be explained and read at real scale? |
| Icon inconsistency | Emoji labels, mixed icon families, colored icons without meaning | Are icons semantic, aligned, accessible, and from one system? |
| Copy inflation | Generic hype, filler greetings, vague benefits, repetitive phrasing | Does every claim match the product and describe a real outcome? |
| Trust fabrication | Unsupported testimonials, logos, metrics, ratings, badges, guarantees | Is the claim traceable to supplied evidence? |
| Data decoration | Chart-shaped filler, random sparklines, unexplained units, fake sample values | What decision does it support and where did data come from? |
| Interaction incompleteness | Dead buttons, static toggles, missing loading/error/empty states | What actually happens for every action and failure path? |
| Responsive collapse | Desktop compressed onto mobile, clipped tables, tiny charts, hidden controls | Does the layout adapt to the mobile task and reading order? |
| Asset mismatch | Random 3D art, generic stock, irrelevant image, inconsistent illustration style | Does the asset have product meaning and valid provenance? |
| Accessibility regression | Low contrast, icon-only actions, keyboard traps, motion without opt-out | Can users perceive, understand, and operate the interface? |
| Code-induced drift | Giant components, scattered inline styles, duplicate variants, class soup | Do implementation choices create visible inconsistency or brittle fixes? |

## Evidence and confidence

- **High confidence:** directly observed defect with a clear user consequence (for example, clipped mobile CTA or dead button).
- **Medium confidence:** visible pattern that plausibly harms clarity but may be intentional in this product.
- **Low confidence:** subjective impression or incomplete context; ask for more evidence before changing.

For every finding record: route/region, observable evidence, user impact, confidence, benign explanation, and proposed correction.

## False positives to avoid

- A gradient may be a real brand asset.
- Cards may be necessary for comparing independent entities.
- Dense dashboards may be appropriate for expert users.
- Repeated components may express a deliberate design system.
- An illustration may be intentionally abstract or playful.
- AI tools may be part of a high-quality workflow.

Do not score authorship. Score usefulness, coherence, clarity, trustworthiness, accessibility, and craft.
