---
name: chart-guides
description: Design clear, professional charts and choose the most appropriate chart type from the data context and communication goal. Use when the user asks for a chart, graph, plot, visualization, gráfico, grafico, dispersão, scatter, dashboard visual, KPI visual, executive visual, or slide/report-ready data visualization. Covers bar, grouped bar, stacked bar, line, scatter, radar, area, histogram, box plot, heatmap, waterfall, dot/lollipop, bullet, slope, and small-multiples patterns. Use to decide which chart to use, how to structure axes and labels, how to avoid misleading visuals, and how to produce consistent slide-ready or report-ready outputs. When repeatability matters, prefer the validated JSON spec plus bundled Python renderer. When the destination is PowerPoint or `.pptx`, also use the `powerpoint-pptx` skill and read `references/pptx_handoff.md`.
---

# Chart Guides

Use this skill to decide, design, review, and when possible render charts so the output is analytically correct, visually clear, consistent with the destination medium, and more deterministic across runs.

## Operating Rule

Do not jump straight from raw data to a favorite chart type. First identify the communication goal, data structure, and reading context. Then choose the chart family, apply the style system, and run the legibility review.

When the chosen chart type is supported by the bundled Python renderer, prefer the deterministic script path over free-form handwritten plotting code.

## Available Chart Families

Read `references/master_style.md` first for global visual rules. Then choose the most appropriate chart family.

- **Bar charts** → `references/bar_charts.md`
  - Vertical bar
  - Horizontal bar
  - Grouped bar
- **Line charts** → `references/line_charts.md`
  - Single-series trend
  - Multi-series trend
- **Scatter plots** → `references/scatter_plots.md`
  - 2D relationship
  - Bubble chart when marker size encodes a third metric
- **Radar plots** → `references/radar_plots.md`
  - Multidimensional profile comparison
- **Area and stacked area charts** → `references/area_charts.md`
  - Emphasize cumulative trend or evolving composition over time
- **Stacked and 100% stacked bars** → `references/stacked_charts.md`
  - Part-to-whole comparison across categories or periods
- **Histograms and distribution charts** → `references/distribution_charts.md`
  - Histogram
  - Density-like frequency view when appropriate
- **Box plots** → `references/distribution_charts.md`
  - Median, spread, and outlier comparison
- **Heatmaps** → `references/heatmaps.md`
  - Matrix intensity, calendar heatmap, correlation-like tables
- **Waterfall charts** → `references/waterfall_charts.md`
  - Stepwise contribution to change from start to finish
- **Dot and lollipop charts** → `references/comparison_charts.md`
  - Clean ranking and value comparison
- **Bullet charts** → `references/comparison_charts.md`
  - Performance vs target with qualitative range bands
- **Slope charts** → `references/comparison_charts.md`
  - Before/after or two-point change
- **Small multiples** → `references/small_multiples.md`
  - Split cluttered comparisons into repeated aligned mini-charts

## Decision Section: Choose the Chart by Use Case

Use this section before reading a chart-specific guide.

### Narrative role → preferred chart family

- **Compare values across categories** → bar chart or dot/lollipop chart
- **Rank categories clearly** → horizontal bar or dot plot
- **Show change over time** → line chart
- **Show cumulative magnitude over time** → area chart only if exact comparisons remain readable
- **Show composition over time** → stacked area or stacked bars, only when segment comparison is still interpretable
- **Show part-to-whole at a few discrete points** → stacked bar or 100% stacked bar
- **Show contribution from start to end** → waterfall chart
- **Show relationship between two continuous variables** → scatter plot
- **Show distribution of a continuous variable** → histogram
- **Compare spread/distribution across groups** → box plot
- **Show intensity across a matrix** → heatmap
- **Compare target vs actual** → bullet chart, bar with target line, or dot plot with reference marker
- **Show before vs after or two-point change** → slope chart
- **Compare multidimensional normalized profiles** → radar plot only when dimensions are few and comparable
- **Show many similar trends or repeated category comparisons** → small multiples instead of overcrowding one chart

### Data structure → preferred chart family

- **Categorical + one metric** → vertical or horizontal bar; dot/lollipop when cleaner
- **Categorical + multiple subgroup metrics** → grouped bar; stacked only if composition matters more than exact subgroup comparison
- **Time + one metric** → single-series line
- **Time + a few related metrics** → multi-series line
- **Time + total plus composition** → stacked area or stacked bars depending on readability and number of time periods
- **Two continuous metrics** → scatter
- **One continuous metric needing frequency view** → histogram
- **Many values across categories/time in a matrix** → heatmap
- **Start, intermediate drivers, ending total** → waterfall
- **Two time points across many categories** → slope chart
- **Many categories with long labels** → horizontal bar or dot plot

### Reading context → adapt the choice

- **Executive slide** → prefer the lowest-density chart that still tells the story
- **Dashboard** → allow slightly more density, but preserve fast scan reading
- **Technical report** → allow fuller labels and supporting annotation when needed
- **Mobile or small footprint** → prefer bar, dot, bullet, or small multiples over dense multi-series visuals
- **PowerPoint / `.pptx`** → also read `references/pptx_handoff.md` and use `powerpoint-pptx`

## Mandatory Workflow

Follow this workflow every time a chart is requested.

### Step 1 — Identify the decision or message

Infer or extract:
- what question the chart must answer
- what the audience should notice first
- whether the chart is for comparison, trend, composition, distribution, relationship, change, target tracking, or profile comparison

Do not choose a chart before the message is clear.

### Step 2 — Inspect the data structure

Determine:
- whether the x-dimension is categorical, temporal, continuous, ordinal, or matrix-like
- how many metrics or series exist
- whether values are absolute, percentage, indexed, normalized, or mixed
- whether there are long labels, many categories, sparse points, outliers, or extreme skew

If units are incompatible, do not force them into one visual without transformation or normalization.

### Step 3 — Determine the reading environment

Infer or ask only if necessary:
- slide, dashboard, report, document, mobile, or social asset
- amount of space available
- expected reading distance and density tolerance
- whether branding or template constraints already exist

Treat slide contexts as low-density by default.

### Step 4 — Choose the chart family

Use `references/chart_selection.md` and the decision section above.

At this step:
- name the recommended chart type
- state why it fits the message and data
- reject misleading alternatives when relevant

### Step 5 — Apply semantic rules before styling

Read `references/semantic_rules.md` and apply the relevant constraints.

Check for:
- whether zero baseline is required
- whether sorting improves interpretation
- whether a stacked chart would hide the real comparison
- whether too many categories or series require filtering, grouping, or small multiples
- whether a log scale is justified and clearly marked
- whether direct labels are better than a legend

### Step 6 — Apply style system

Read:
- `references/master_style.md`
- the chosen chart reference

Then specify:
- axis design
- scale behavior
- sorting/order
- color hierarchy
- label strategy
- legend strategy
- annotation strategy
- export/layout format

### Step 7 — Convert the decision into a spec

Prefer a saved JSON spec over improvised plotting code.

If repeatability matters:
- read `references/spec_schema.md`
- create or edit a JSON spec
- validate it with `scripts/validate_chart_spec.py`
- if the output must be presentation-ready, read `references/executive_templates.md`; `scripts/render_chart.py` is now the single official renderer and prefers executive templates automatically when a supported scenario or `presentation_template` is present
- `scripts/render_exec_chart.py` remains only as a compatibility wrapper around the same render core
- otherwise render it with `scripts/render_chart.py` when the type is supported

### Step 8 — Run mandatory legibility review

Review the chart as if the audience has only a few seconds.

Validate:
- title states the message, not just the metric name
- axes are explicit and units are visible
- labels are intentional rather than excessive
- important values or series stand out immediately
- there is no clutter from redundant legends, dense labels, or decorative elements
- the chart remains readable at the destination size
- comparisons are not visually distorted by bad scales, misleading truncation, or unnecessary dual axes

### Step 9 — Produce the output in a structured format

Default output should include:
- **Objective/message**
- **Recommended chart type**
- **Why this chart**
- **Why not the obvious alternatives** when relevant
- **Data mapping**
- **Axis and scale rules**
- **Color and emphasis rules**
- **Labels / legend / annotations**
- **Readability and QA notes**
- **Destination-specific notes**
- **Saved spec path** when the deterministic path is used

If the final chart type is supported by the bundled renderer, prefer the validated spec plus script workflow.

If the user asked for implementation and the scripted path is not suitable, convert this structure into code/library-ready instructions.

## Mandatory Review Workflow

Use this review pass before finalizing any chart recommendation or design.

1. **Analytical integrity**
   - Does the chart answer the intended question?
   - Is the chart type semantically correct for the data?
2. **Scale integrity**
   - Are baselines, log scales, percentages, and normalization clearly handled?
3. **Density control**
   - Would fewer series, categories, or labels improve understanding?
4. **Highlight discipline**
   - Is there a single visual hierarchy, or are too many things screaming at once?
5. **Reading-distance test**
   - Can the chart still be understood quickly in its final medium?
6. **Alternative check**
   - Would a simpler chart family tell the story better?

If the review fails, simplify before finalizing.

## Output Quality Rules

- Prefer direct labels over legends when the chart is simple enough.
- Prefer fewer categories shown clearly over many categories shown badly.
- Prefer chart families that match the user question directly, not the most visually impressive option.
- Treat radar, stacked area, dual-axis, and dense multi-series visuals as higher-risk choices that require explicit justification.
- If the data story can be told with a simpler chart, choose the simpler chart.
- Prefer validated specs and bundled scripts when available.

## PowerPoint / PPTX Handoff

If the destination is PowerPoint or `.pptx`:
- read `references/pptx_handoff.md`
- design the chart for slide readability first
- then use `powerpoint-pptx` for template-aware integration, placeholder handling, layout fitting, and render QA

## Reference Map

- Global visual system → `references/master_style.md`
- Chart selection logic → `references/chart_selection.md`
- When to use / when not to use → `references/anti_patterns.md`
- Semantic correctness → `references/semantic_rules.md`
- Chart spec schema → `references/spec_schema.md`
- Deterministic script workflow → `references/scripts.md`
- PPTX handoff → `references/pptx_handoff.md`
- Bar charts → `references/bar_charts.md`
- Line charts → `references/line_charts.md`
- Scatter plots → `references/scatter_plots.md`
- Radar plots → `references/radar_plots.md`
- Area charts → `references/area_charts.md`
- Stacked charts → `references/stacked_charts.md`
- Distribution charts → `references/distribution_charts.md`
- Heatmaps → `references/heatmaps.md`
- Waterfall charts → `references/waterfall_charts.md`
- Dot/lollipop, bullet, slope → `references/comparison_charts.md`
- Small multiples → `references/small_multiples.md`

## Universal Design Principles

All charts should follow these principles:

1. **Clarity over decoration** — the message should be obvious quickly
2. **Label intentionally** — title, axes, legends, and values only when they improve reading
3. **Use color semantically** — color should encode hierarchy or categories, not random decoration
4. **Consistency matters** — keep patterns stable across a project or deck
5. **Mark scale behavior explicitly** — especially for log scales, normalization, indexing, or percentages
6. **Respect the medium** — a chart that works on a dashboard may fail on a slide
7. **Prefer honest simplicity** — authority comes from readability and correctness, not visual gymnastics
8. **Prefer deterministic rendering paths when available** — if a bundled script can render the chart reliably, use it instead of improvising new plotting code
