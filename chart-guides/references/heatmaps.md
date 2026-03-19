# Heatmap Pattern

Use this guide for matrix-style charts where color intensity encodes value.

> Always apply global rules from [master_style.md](master_style.md) first.

## When to use

Use when:
- the data forms a matrix or grid
- intensity patterns, hot spots, seasonality blocks, or correlation-like structures matter
- a bar chart would become too dense or repetitive

Common examples:
- category by month matrix
- calendar activity map
- correlation-style table
- hour by day behavioral matrix

## When not to use

- when exact value reading is more important than pattern detection
- when the matrix is tiny and bars/tables would be clearer
- when color scale labeling would be ambiguous

## Core style rules

1. Use an ordered palette with clear low-to-high progression.
2. Avoid rainbow palettes.
3. Keep cell borders subtle or absent.
4. Label both axes clearly.
5. Provide a readable color scale legend.
6. Use annotations only when cell count is small enough.

## Semantic rules

- Make it explicit whether values are absolute, percentage, index, or score.
- Keep the color scale consistent across related heatmaps.
- If zero, midpoint, or target has semantic meaning, reflect that intentionally in the scale.

## Quick checklist

- [ ] Matrix pattern is easier to read by intensity than by bars
- [ ] Palette is perceptually ordered
- [ ] Color scale legend is clear
- [ ] Cell labels are used only when readable
- [ ] Related heatmaps share a comparable scale when needed
