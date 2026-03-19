# Line Chart Pattern (Single + Multi-Series)

Use this default for **all line charts** unless the user asks otherwise.

> Always apply global rules from [master_style.md](master_style.md) first.

## Core Style Rules

1. Use **purple as the primary highlight** (`#6D28D9`) for the most important series.
2. Use **complementary colors** for remaining series (teal/orange/green/blue family).
3. Keep lines clean and readable:
   - **No smoothing/curves**
   - Use straight segments between real points only
4. Always show a **marker on every data point**.
5. Remove chart junk:
   - No grid lines by default (enable only when it improves reading)
   - No top/right border lines
6. Keep structure in black:
   - Axis lines (left/bottom), ticks, labels, and titles in black
7. Add value labels only when they improve readability:
   - Prefer labeling the final point of each series
   - For sparse charts, label all points in **bold** with subtle white rounded background

## Typography Defaults

- Prefer Calibri when available (fallback to system sans-serif).
- Title: **14** (bold) baseline; scale up only when explicitly requested.
- Axis title(s): **10** baseline.
- Tick labels: **8** baseline.
- Data labels: **10 bold** baseline.
- If user asks “increase all text by +2”, apply consistently to every text element.

## Axis & Label Conventions

- Y-axis title should be explicit and metric-based (example: **"Quantidade de demandas"**, **"Conversões"**, **"CTR (%)"**).
- Add extra padding so Y-axis title does not collide with axis line.
- X-axis title may be omitted when date labels are self-explanatory.
- Date labels must always use these formats:
  - **MM/YY** for monthly/annual views
  - **DD/MM/YY** when day granularity is required
- Keep category/date labels legible and proportional to chart size.

## Legend Placement

- For multi-series lines, place legend in **top-right** by default.
- If lines end near top-right, move legend to a clear corner (usually bottom-right).
- Keep legend text readable and proportional.
- For single-series charts, omit legend unless user explicitly wants it.

## Layout Rules (Readability First)

- Maintain proportional spacing for title, plot area, labels, and legend.
- All elements must be proportional to each other (title, axis labels, ticks, value labels, lines, markers, legend).
- Leave enough top margin for point labels.
- Use 16:9 export for slides and optionally square/mobile export when useful.

## Single vs Multi-Series

### Single-series line (default)
- Use when showing trend of one metric over time.
- Highlight line in purple (`#6D28D9`).
- Use point markers on every observation.

### Multi-series line
- Use when comparing 2–4 related trends over time.
- Keep one priority series in purple and others in complementary colors.
- Ensure enough contrast between lines and markers.
- Avoid more than 4 series in one chart (split if needed).

## When to Use Line Charts

- Showing trends over time
- Comparing trajectory of a few series
- Highlighting divergence/convergence or crossings
- Continuous or ordered temporal sequences

## When NOT to Use Line Charts

- Discrete categories with no temporal order (use bar charts)
- Too many series causing clutter (split charts)
- Single-point comparisons (use bar/scatter)

## Quick Checklist Before Sending

- [ ] Purple highlight used for key series
- [ ] Complementary colors used for remaining series
- [ ] Straight segments only (no smoothing)
- [ ] Marker on every point
- [ ] No top/right borders
- [ ] Grid only if it improves readability
- [ ] Axis structure and text in black
- [ ] Labels are readable and proportional
- [ ] Legend placement avoids overlap
- [ ] Date format follows MM/YY or DD/MM/YY rule
- [ ] Final export looks clean and consistent with bar chart style
