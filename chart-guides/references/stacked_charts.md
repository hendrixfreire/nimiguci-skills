# Stacked Chart Pattern

Use this guide for stacked bar, stacked column, and 100% stacked variants.

> Always apply global rules from [master_style.md](master_style.md) first.

## When to use

### Stacked bars / columns
Use when:
- part-to-whole composition matters
- totals matter and segment makeup also matters
- the number of categories and segments is controlled

### 100% stacked bars / columns
Use when:
- share/proportion matters more than absolute totals
- the audience must compare composition rather than size

## When not to use

- when precise comparison of internal segment values across categories matters
- when there are too many segments
- when color decoding becomes heavy work
- when grouped bars or small multiples would communicate more honestly

## Core style rules

1. Keep one segment or story highlight in purple when there is a strategic segment to emphasize.
2. Use stable, repeatable color mapping for other segments.
3. Keep segment order consistent across categories.
4. Put legends in a clean, easy-to-scan position; below or top-right depending on chart footprint.
5. Remove top/right borders by default.
6. Use grid lines only when they genuinely help.

## Semantic rules

- Keep segment order consistent across all bars.
- Avoid too many tiny segments.
- In 100% stacked views, make it explicit that totals are normalized to 100%.
- If absolute totals also matter strongly, consider pairing with a simple total bar/line or using a different chart family.

## Label strategy

- Label total values when useful.
- Label internal segments only when large enough to read clearly.
- Avoid stuffing labels into thin slices or narrow segments.

## Quick checklist

- [ ] Composition is the main story
- [ ] Segment order is consistent
- [ ] Number of segments is manageable
- [ ] 100% normalization is explicit when used
- [ ] Grouped bar or small multiples were considered
