# Chart Spec Schema

Use this file when repeatability matters and the chart should follow a strict, validated contract before rendering.

## Goal

Separate chart **decision** from chart **rendering**.

- The skill decides the right chart and fills the spec.
- The validator checks whether the spec is structurally valid.
- The renderer draws the chart deterministically from the validated spec.

This reduces drift, improves auditability, and makes repeated runs more predictable.

## Core rule

Prefer a saved JSON spec over one-off handwritten plotting code.

## Required base fields

All specs must include:
- `chart_type`
- `title`

Most charts must also include either:
- `data_path`
- or inline `data`

Heatmaps may use inline `matrix` instead.

## Supported chart types in the validated schema

- `bar`
- `grouped_bar`
- `stacked_bar`
- `line`
- `scatter`
- `histogram`
- `heatmap`
- `waterfall`
- `slope`

## Per-type required fields

### `bar`
- `x`
- `y`

### `grouped_bar`
- `x`
- `series`

### `stacked_bar`
- `x`
- `series`

### `line`
- `x`
- `y`

### `scatter`
- `x`
- `y`

### `histogram`
- `x`

### `heatmap`
- `matrix`

### `waterfall`
- `x`
- `y`

### `slope`
- `label_key`
- `start_key`
- `end_key`

## Style block

If omitted, defaults are filled automatically:
- width: `13.33`
- height: `7.5`
- dpi: `150`
- font_family: `DejaVu Sans`
- title_size: `14`
- axis_size: `10`
- tick_size: `8`
- grid: `false`

## Validation flow

1. create or edit the JSON spec
2. run `scripts/validate_chart_spec.py`
3. only render after validation passes

Example:
```bash
python3 skills/chart-guides/scripts/validate_chart_spec.py \
  --spec output/chart_spec.json
```

## Why this matters

Without a schema, the model can still drift while filling specs.
With a schema, invalid or ambiguous instructions get rejected before rendering.

## Recommended deterministic pipeline

1. Use `chart-guides` to choose the chart type.
2. Fill a JSON spec.
3. Validate the spec.
4. Render with the bundled renderer if the type is supported.
5. Save the spec alongside the output chart for reproducibility.
