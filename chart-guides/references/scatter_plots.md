# Scatter Plot Pattern (Dispersão: Single + Multi-Category)

Use this default for **all scatter/dispersão charts** unless the user asks otherwise.

> Always apply global rules from [master_style.md](master_style.md) first.

## Core Style Rules

1. Use **purple as the primary highlight** (`#6D28D9`) for the most important category/series.
2. Use **complementary colors** for remaining categories.
3. Keep points visually clean:
   - Solid fill circles by default
   - No marker border unless overlap requires contrast
4. Keep marker sizing intentional:
   - Fixed size for 2D comparisons
   - Variable size only when encoding a third metric that materially improves interpretation
5. Remove chart junk:
   - No grid lines by default (enable only when it improves reading)
   - No top/right border lines
6. Keep structure in black:
   - Axis lines (left/bottom), ticks, labels, and titles in black
7. Add labels selectively:
   - Label only outliers/key points by default
   - If few points, label all with subtle white rounded background

## Typography Defaults

- Prefer Calibri for PowerPoint/Office-bound charts; otherwise use a clean sans-serif consistent with the destination medium.
- Title: **14** (bold) baseline; scale up only when explicitly requested.
- Axis title(s): **10** baseline.
- Tick labels: **8** baseline.
- Data labels/annotations: **10 bold** baseline.
- If user asks “increase all text by +2”, apply consistently to every text element.

## Axis & Label Conventions

- Label both axes clearly with units/context (example: **"Alcance"**, **"Seguidores"**, **"CPA (R$)"**).
- Add scale type in axis labels whenever log scale is used:
  - Example: **"Reach (log)"**, **"Follows (log)"**
- Add extra padding so axis titles do not collide with axis lines.
- Keep tick labels legible and proportional.

## Legend Placement

- For multi-category scatter, place legend in **top-right** by default.
- Move legend to another corner if it overlaps dense point clusters.
- For single-category scatter, omit legend unless explicitly requested.

## Layout Rules (Readability First)

- Maintain proportional spacing for title, plot area, labels, and legend.
- All elements must be proportional to each other (title, axis labels, ticks, markers, labels, legend).
- Leave enough margin for annotations and outlier labels.
- Use 16:9 export for slides and optionally square/mobile export when useful.

## Overplotting Strategy

When many points overlap, do not pretend the chart is still clean.

Use one or more of these strategies:
- reduce marker opacity
- apply limited jitter when discrete values stack on top of each other
- reduce marker size
- aggregate/bin when point-level detail is no longer interpretable
- facet into small multiples when categories need separation

If overplotting remains severe, consider whether a different chart family is more honest.

## Scale Selection (Linear vs Log)

### Use **LOG scale** when:
- data spans multiple orders of magnitude
- ratio/percentage growth patterns matter more than absolute deltas
- small and large values need equal visual visibility

### Use **LINEAR scale** when:
- data range is compact
- absolute differences are the story
- audience needs more intuitive direct reading

### Quick Rule
- If `max / min > 100`, prefer log scale.
- If `max / min < 10`, prefer linear scale.
- In between, choose based on narrative focus (growth pattern vs absolute difference).

## When to Use Scatter Plots

- Showing relationship/correlation between two metrics
- Detecting clusters, dispersion, and outliers
- Comparing categories in the same 2D metric space
- Adding optional third dimension via marker size/color when justified

## When NOT to Use Scatter Plots

- Time-series trends (use line charts)
- Simple categorical comparisons (use bar charts)
- Overcrowded points with no aggregation strategy

## Quick Checklist Before Sending

- [ ] Purple highlight used for key category/series
- [ ] Complementary colors used for remaining categories
- [ ] Marker size strategy is intentional and consistent
- [ ] No top/right borders
- [ ] Grid only if it improves readability
- [ ] Axis structure and text in black
- [ ] Scale type clearly marked when log is used
- [ ] Labels/annotations are readable and non-overlapping
- [ ] Legend placement avoids overlap
- [ ] Overplotting is handled honestly
- [ ] Final export looks clean and consistent with bar/line style
