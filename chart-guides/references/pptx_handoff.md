# PPTX Handoff Guide

Read this file whenever the destination is PowerPoint or `.pptx`.

## Goal

Design the chart so it survives slide placement, template constraints, and presentation reading distance. Then hand off to `powerpoint-pptx` for actual deck integration.

## Required flow

1. Use `chart-guides` to decide the right chart type.
2. Simplify for slide readability.
3. Define chart specs, hierarchy, scale, labels, and annotation strategy.
4. Hand off to `powerpoint-pptx` for placeholder-aware insertion, slide fitting, theme alignment, and render QA.

## Extract or infer these fields

- presentation objective
- audience
- slide title or message
- destination slide footprint
- whether the chart is new, replacing an old chart, or adapting to a template
- narrative role: comparison, trend, composition, distribution, relationship, target, contribution, profile
- whether the slide will be read live, exported to PDF, or shared asynchronously

## Slide-specific rules

- Prefer lower-density charts than you would use in a dashboard.
- Prioritize one message per chart.
- Use fewer categories, fewer series, and fewer labels.
- Prefer direct labels or concise legends.
- Assume the chart may be viewed from a distance.
- Keep annotations large enough to survive projector or PDF downsizing.

## Preferred chart families for slides

Default preference order for executive slides:
- bar / horizontal bar
- line
- dot / lollipop
- bullet
- slope

Use with stronger justification:
- stacked charts
- heatmaps
- waterfall
- scatter with many points
- radar
- dense small multiples

## Handoff payload

When preparing for `powerpoint-pptx`, pass or preserve:
- chart objective/message
- chosen chart type
- data mapping
- scale and baseline behavior
- sorting/order logic
- highlight color and secondary palette use
- title/subtitle text
- labels, legend, and annotation rules
- slide-density constraints
- any template or placeholder constraints already known

## Final QA before handoff

- Is the main message readable in a few seconds?
- Would this chart still work if shrunk by 20 to 30 percent?
- Is any non-essential label removable?
- Does the chart rely on dashboard-style hover behavior that slides do not have?
- Is the chart type still the best choice for spoken presentation context?

If the answer is no, simplify before handing off.
