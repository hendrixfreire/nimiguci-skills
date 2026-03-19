# Area Chart Pattern

Use this guide for area and stacked area charts.

> Always apply global rules from [master_style.md](master_style.md) first.

## When to use

### Area chart
Use when:
- the chart shows trend over time
- cumulative magnitude or filled volume supports the message
- exact line-to-line comparison is not the main task

### Stacked area chart
Use when:
- composition changes over time matter
- the audience needs to read broad composition shifts rather than precise segment values
- the number of segments is limited

## When not to use

- when exact comparison between several series matters
- when overlapping fills or many segments reduce legibility
- when a simple line chart would communicate the message more clearly

## Core style rules

1. Use purple `#6D28D9` for the primary highlighted series or top story layer.
2. Use complementary colors for other series.
3. Keep fill opacity moderate so boundaries remain readable.
4. Use clean outlines where helpful, but avoid heavy strokes.
5. Avoid stacking too many categories.
6. Remove top/right borders by default.
7. Use grid lines only when they improve reading.

## Typography defaults

- Follow [master_style.md](master_style.md).
- Keep title, axis labels, and annotations proportional.

## Axis and label conventions

- Time should remain the x-axis for most area-chart use cases.
- Label scale and units clearly.
- If using stacked area, indicate whether values are absolute or share-based.
- For 100% composition-over-time cases, make the percentage basis explicit.

## Label strategy

- Prefer endpoint labels for a few series.
- Avoid labeling every point on dense area charts.
- Use annotations selectively for turning points or major composition shifts.

## Quick checklist

- [ ] Trend or composition is the real story
- [ ] Filled area adds meaning rather than drama
- [ ] Number of series/segments is limited
- [ ] Labels remain readable
- [ ] Simpler line chart was considered and rejected for a reason
