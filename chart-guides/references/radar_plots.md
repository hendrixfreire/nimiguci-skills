# Radar Plot Pattern (Spider / Teia de Aranha)

Use this guide for radar charts **only when a radar is genuinely the right tool**.

> Always apply global rules from [master_style.md](master_style.md) first.

## When to Use Radar Plots

Use when you need to compare entities across a fixed set of dimensions and the **profile shape itself** helps interpretation.

Good fits:
- 5 to 10 dimensions
- 1 to 3 entities/series
- Normalized scales (same range across all axes)
- Executive/profile views where approximate shape comparison is acceptable

Avoid when:
- Too many dimensions (>10)
- Too many entities (>3)
- Metrics have very different scales and were not normalized
- Precise value comparison matters more than overall profile shape

If a grouped bar chart, small multiples, or table would be more precise and easier to read, prefer those instead.

## Core Style Rules

1. Highlight key entity in **purple `#6D28D9`**.
2. Use complementary colors for additional entities.
3. Prefer semi-transparent fill (`alpha ~0.15–0.30`) + clear outline stroke.
4. Keep radial grid subtle; no heavy decoration.
5. Keep labels around the circle legible and horizontal when possible.
6. Treat radar as a higher-risk chart family that requires explicit justification.

## Scale & Normalization Rules

- **Normalize data before plotting (mandatory).**
- All axes must share the same numerical range **after normalization**.
- Prefer normalized scale:
  - `0–100` for percentage-like scoring
  - `0–10` for rating scales
- If normalization was applied, mention method + scale in subtitle (ex.: "Normalizado min-max em escala 0–100").
- Never compare raw metrics with incompatible units on the same radar without normalization.

## Typography & Labels

- Follow [master_style.md](master_style.md) typography defaults.
- Title should state comparison context clearly.
- Subtitle should describe scale and period/context.
- Value labels on every vertex are optional; use only if not cluttered.

## Legend Placement

- Top-right default.
- Move outside plot area if overlap occurs.
- For single-series radar, legend can be omitted.
- **Legend must be proportional to chart size**:
  - Keep legend font aligned with chart typography baseline
  - Reduce legend size for compact charts and increase for large exports
  - Avoid oversized legend boxes that dominate the visual
  - Keep marker/line sample length proportional to text size

## Layout Rules

- Keep equal angular spacing between dimensions.
- Start first axis at top (12 o’clock) when possible.
- Rotate clockwise for readability consistency.
- Maintain enough margin so category labels are not clipped.

## Quick Checklist Before Sending

- [ ] Dimensions are comparable and on same scale
- [ ] Primary series highlighted in purple
- [ ] Fill + stroke are readable and not too dense
- [ ] Category labels are legible and unclipped
- [ ] Legend does not overlap data
- [ ] Subtitle explains scale/normalization
- [ ] Radar is justified over grouped bars or small multiples
- [ ] Visual matches global style consistency
