# Deterministic Script Workflow

Use these scripts whenever repeatability matters more than free-form chart generation.

## Goal

Move the repetitive, exact work of chart rendering into Python so the skill becomes more deterministic, cheaper in token usage, and less dependent on the current model improvising style details.

## Available scripts

### `scripts/make_chart_spec.py`
Generate a starter JSON spec template.

Example for CSV-driven charts:
```bash
python3 skills/chart-guides/scripts/make_chart_spec.py \
  --csv data/example.csv \
  --chart-type grouped_bar \
  --output output/chart_spec.json
```

Example for heatmap template:
```bash
python3 skills/chart-guides/scripts/make_chart_spec.py \
  --chart-type heatmap \
  --output output/heatmap_spec.json
```

### `scripts/validate_chart_spec.py`
Validate and normalize a JSON spec before rendering.

Example:
```bash
python3 skills/chart-guides/scripts/validate_chart_spec.py \
  --spec output/chart_spec.json
```

### `scripts/render_chart.py`
Single official renderer. Render a chart image deterministically from a validated JSON spec. It now prefers executive templates automatically when a presentation-oriented template applies.

Example:
```bash
python3 skills/chart-guides/scripts/render_chart.py \
  --spec output/chart_spec.json \
  --output output/chart.png
```

## Current scripted support

The renderer currently supports:
- `bar`
- `grouped_bar`
- `stacked_bar`
- `line`
- `scatter`
- `histogram`
- `heatmap`
- `waterfall`
- `slope`

## Deterministic contract

If the same spec JSON and same input data are used, the script should generate the same chart layout and styling parameters across runs in the same environment.

Determinism is strongest when:
- the spec passes validation first
- sorting, labels, and titles are explicit
- dimensions and DPI are fixed
- the same Python/matplotlib environment is used
- the output depends on the script path instead of handwritten plotting code

## Recommended workflow

1. Use the skill decision workflow to choose the chart family.
2. Create a spec template with `make_chart_spec.py` when useful.
3. Edit the JSON spec deliberately.
4. Validate with `validate_chart_spec.py`.
5. Render with `render_chart.py`.
6. Save the spec alongside the rendered chart for reproducibility.
7. If the destination is PowerPoint, pass the rendered output to `powerpoint-pptx`.

## Why this helps

- removes repeated plotting boilerplate from the model
- centralizes style defaults
- rejects malformed or ambiguous specs before rendering
- reduces accidental drift in color, labels, ordering, and layout
- makes chart creation auditable through saved spec files
- gives the skill a low-freedom deterministic path when consistency matters most

## When not to use the scripts

Do not force the scripts when:
- the chosen chart type is not yet supported
- the user needs a one-off highly custom visual that exceeds the current renderer
- the workflow requires a visualization library not covered by this deterministic path

In those cases, still use the references for selection, semantics, and QA.
