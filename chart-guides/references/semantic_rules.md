# Semantic Rules for Honest, Professional Charts

Use this file before styling. A chart can look polished and still be analytically wrong.

## 1. Match chart type to the analytical question

Choose the chart that matches the question being asked:
- comparison
- ranking
- trend
- composition
- distribution
- relationship
- contribution to change
- target tracking
- profile comparison

Do not choose based on visual novelty.

## 2. Respect baseline rules

### Bars and columns
- Start at zero by default.
- If a non-zero baseline is used, justify it explicitly and make the truncation obvious.
- Do not use truncated bars when the audience may infer magnitude by length.

### Lines and scatter
- Non-zero baselines are acceptable when they do not distort the intended comparison.
- Still avoid manipulative cropping that exaggerates volatility.

## 3. Sort categories intentionally

- Sort descending when ranking is the story.
- Preserve natural order for time, process steps, or predefined business order.
- Do not leave arbitrary source-data order unless the order itself carries meaning.

## 4. Use stacked visuals only when composition is the story

- If comparing segment sizes precisely across categories is the main task, prefer grouped bars or small multiples.
- Use 100% stacked only when proportion/share matters more than absolute totals.

## 5. Limit categories and series

- If there are too many categories, group minor ones into `Other` only when analytically honest and clearly labeled.
- If there are too many series, split into small multiples or prioritize the key ones.
- More data shown is not automatically better communication.

## 6. Handle long labels properly

- Prefer horizontal bars, dot plots, wrapping, or abbreviation with support notes.
- Do not squeeze labels until they become decoration.

## 7. Use log scales carefully

Use log scale only when:
- values span multiple orders of magnitude
- multiplicative relationships matter
- the audience can reasonably interpret the scale

When log is used:
- mark it explicitly in the axis title
- avoid mixing log-transformed and linear interpretations casually
- do not use log just to make ugly ranges fit better

## 8. Treat percentages, indexes, and normalized values explicitly

- Mark whether values are absolute, percentage, indexed, or normalized.
- If data is normalized or indexed, say so in title or subtitle.
- Do not compare normalized and raw values in the same visual without explanation.

## 9. Prefer direct labels when the chart is simple

- For one or a few series, direct labels often outperform legends.
- Use legends when direct labeling would clutter the chart.
- If the viewer must bounce between the plot and a distant legend repeatedly, reconsider the design.

## 10. Use color for meaning, not decoration

- Reserve highlight color for the main series, category, or exception.
- Keep non-highlight elements neutral or supportive.
- Avoid introducing many saturated colors without categorical need.

## 11. Annotate selectively

Annotate when it helps the reader notice:
- outliers
- turning points
- target breaches
- major changes
- final values

Do not annotate every point if the result is noise.

## 12. Avoid dual-axis charts unless absolutely necessary

- Dual axes often create false comparisons.
- Prefer indexing, normalization, separate panels, or small multiples.
- If dual axis is unavoidable, state the reason and make axis mapping unmistakable.

## 13. Preserve comparability across related charts

- Reuse scales when panels are intended to be compared directly.
- Keep color meaning consistent across a deck or report.
- Keep the same category order when comparing across visuals.

## 14. Build titles that state the takeaway

Prefer:
- `Search conversions grew 28% after campaign restructuring`

Over:
- `Search conversions by month`

A professional chart does not just name the data; it frames the point.
