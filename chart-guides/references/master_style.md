# Master Style Guide (Global)

Use this as the **single source of truth** for all chart types unless a destination-specific constraint requires an intentional override.

## 1) Visual Hierarchy & Colors

- Primary highlight color: **Purple `#6D28D9`**
- Secondary/complementary palette: blue/teal/orange/green family
- Use purple for the most important series, category, or annotation
- Keep non-highlight structure neutral and visually secondary
- Use color semantically; do not assign saturated colors without a categorical or hierarchical reason

## 2) Typography

- Prefer **Calibri** for PowerPoint/Office-bound charts
- For non-Office contexts, use a clean sans-serif consistent with the destination medium
- Title: **14 bold** baseline
- Axis titles: **10** baseline
- Tick labels: **8** baseline
- Data labels: **10 bold** baseline
- Apply size changes consistently across all text elements

## 3) Clean Layout (Anti-Chart-Junk)

- Remove top/right borders by default
- No unnecessary decorative elements
- Grid lines off by default; turn them on only when they improve readability
- Keep spacing proportional between title, plot, axes, labels, and legend
- Prefer honest simplicity over ornamental styling

## 4) Axis/Text Conventions

- Axis lines, ticks, labels, and titles in black by default unless the destination theme requires adaptation
- Axis labels must be explicit and metric-based
- Mark scale behavior when relevant: log, normalized, indexed, percentage, or rolling average
- Date formats:
  - `MM/YY` for monthly/annual
  - `DD/MM/YY` for day-level data

## 5) Labels & Legend

- Label intentionally, not exhaustively
- If labels are used on dense visuals, prefer selective labeling of key points, outliers, totals, or final points
- Value labels should be readable, sometimes with subtle white rounded background when contrast is needed
- Prefer direct labels over legends when the chart is simple enough
- Place legend where it does not overlap data; top-right is a default, not a law

## 6) Export Defaults

- Use 16:9 for slide-ready outputs
- Provide square/mobile variant when useful
- Ensure final chart is readable at a glance in the actual destination medium

## 7) Final QA Checklist

- [ ] Highlight color used intentionally
- [ ] Supporting palette used consistently
- [ ] Typography follows destination-aware defaults
- [ ] No unnecessary visual noise
- [ ] Axis labels and units are explicit and readable
- [ ] Legend/direct-label strategy is clean
- [ ] Date formatting follows standard when applicable
- [ ] Scale behavior is clearly marked when needed
- [ ] Output is consistent with the rest of the project or deck
