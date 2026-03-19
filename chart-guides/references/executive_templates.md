# Executive Templates

Use this reference when chart output must be presentation-ready rather than merely analytically correct.

## Goal

Render charts through fixed executive templates instead of a generic chart renderer whenever visual quality and repeatability matter more than broad type coverage.

## Current templates

- `single_bar_exec` — one highlighted horizontal bar
- `ranking_bar_exec` — horizontal ranking with long labels
- `line_exec_short` — short time or ordered series
- `scatter_exec_few` — scatter plot with few points and controlled labeling
- `grouped_bar_exec` — grouped categorical comparison
- `stacked_bar_exec` — stacked composition comparison
- `histogram_exec` — frequency distribution
- `heatmap_exec` — matrix intensity view
- `waterfall_exec` — start-to-end contribution bridge
- `slope_exec` — two-point change comparison

## Script

Primary path:
```bash
python3 skills/chart-guides/scripts/render_chart.py \
  --spec path/to/spec.json \
  --output path/to/output.png
```

Compatibility wrapper still available:
```bash
python3 skills/chart-guides/scripts/render_exec_chart.py \
  --spec path/to/spec.json \
  --output path/to/output.png
```

## Routing rule

If the chart is presentation-oriented, prefer an executive template. Set `presentation_template` explicitly when needed. When omitted, the renderer should infer the most likely template from chart type and shape.

## Why this exists

The generic renderer is still useful for broader coverage and experimentation, but fixed templates are a better fit for charts that must look intentional in a deck.
