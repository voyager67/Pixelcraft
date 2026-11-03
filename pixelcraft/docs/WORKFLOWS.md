# Recommended workflows

## Whole-screen remediation

`slop-detection` → `slop-audit` → `slop-severity-triage` → `product-specific-direction` → `unslop-ui` → `slop-remediation-quality-gate`

## Diagnose without changing code

`slop-detection` → `slop-audit` → `slop-severity-triage`

## Remove visual cliché patterns

`visual-cliche-detection` → `effects-overuse-repair` → `card-bloat-repair` → `visual-hierarchy-repair`

## Improve a data-heavy UI

`dashboard-slop-repair` → `chart-slop-repair` → `data-viz-integrity-repair` → `table-density-repair`

## Fix responsive and accessible output

`responsive-slop-repair` → `mobile-ui-slop-repair` → `accessibility-slop-repair` → `visual-regression-guard`

## Clean up implementation-driven drift

`token-sprawl-repair` → `component-consistency-repair` → `tailwind-slop-cleanup` or `react-ui-slop-refactor` → `slop-regression-review`
