# Bar Chart Pattern (Vertical + Horizontal)

Use this default for **all bar charts** unless the user asks otherwise.

> Always apply global rules from [master_style.md](master_style.md) first.

## Core Style Rules

1. Use **purple as the primary highlight** (`#6D28D9`) for the most important category/bar.
2. Use **complementary colors** for other categories (teal/orange/green/blue family).
3. Keep bars with **light spacing** between each other (avoid touching bars).
4. Remove chart junk:
   - No grid lines by default
   - No top/right border lines
   - **No border/edge on bars** (bars must be solid fill only, no outline)
5. Keep structure in black:
   - Axis lines (left/bottom), axis ticks, labels, titles in black
6. Add value labels on bars in **bold** with a subtle white rounded background for readability.

## Typography Defaults

- Prefer Calibri when available (fallback to system sans-serif).
- Title: **14** (bold) baseline; scale up only when explicitly requested.
- Axis title(s): **10** baseline.
- Tick labels: **8** baseline.
- Bar value labels: **10 bold** baseline.
- If user asks “increase all text by +2”, apply consistently to every text element.

## Axis & Label Conventions

- Y-axis title should be explicit, usually: **"Quantidade de demandas"** (or equivalent metric name).
- Add extra padding so Y-axis title does not collide with axis line.
- Omit X-axis title when not needed.
- Keep category names legible and proportional to chart size.
- Date labels must always use these formats:
  - **MM/YY** for monthly/annual views
  - **DD/MM/YY** when day granularity is required

## Legend Placement

- For grouped/stacked bars, center legend below the chart.
- Place legend close to the X-axis label area, but not overlapping labels.
- Keep legend text readable and proportional.

## Layout Rules (Readability First)

- Maintain proportional spacing for title, plot area, labels, and legend.
- All elements must be proportional to each other (title, axis labels, ticks, value labels, bars, and legend).
- Leave enough top margin for value labels.
- Use 16:9 export for slides and optionally square/mobile export when useful.

## Vertical vs Horizontal

### Vertical bars (default)
- Use when category names are short/medium and time-period comparisons are central.
- Charts with dates (daily, monthly, or annual) must always be vertical.

### Horizontal bars
- Use when category names are long or many categories are present.
- Keep same color hierarchy and typography rules.
- Do not use horizontal bars for date-based categories.

## Quick Checklist Before Sending

- [ ] Purple highlight used for key category/bar
- [ ] Complementary colors used for remaining bars
- [ ] Light spacing between bars
- [ ] No grid + no top/right borders
- [ ] No border/edge on bars (solid fill only)
- [ ] Axis structure and text in black
- [ ] Value labels bold and readable
- [ ] Legend centered below (when needed)
- [ ] Proportions look clean in final export
