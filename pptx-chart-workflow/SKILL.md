---
name: pptx-chart-workflow
description: Orchestrate PowerPoint `.pptx` work when the request is specifically about building, editing, or filling a presentation deck that contains data-driven slides, charts, dashboards, or template-based content population. Use when the deliverable is a PowerPoint file and the task requires coordinating chart design plus PPTX integration, especially for: (1) creating a deck from data, (2) editing an existing `.pptx`, (3) replacing weak charts in a presentation, or (4) filling a PowerPoint template with existing data/content. Do NOT use for generic mentions of PPT/PPTX, simple file conversion, casual discussion about presentations, or non-PowerPoint chart requests. This skill should trigger only when the main artifact is an actual PowerPoint deck and the task needs a structured workflow across `chart-guides` and `powerpoint-pptx`.
---

# PPTX Chart Workflow

Use this skill as the top-level coordinator when the user wants a PowerPoint deck that includes data visuals or when an existing PowerPoint template must be populated with real content.

## Activation Boundary

Trigger this skill only if **all** of these are true:

1. The main deliverable or edited artifact is a PowerPoint file (`.pptx`, PowerPoint deck, presentation template).
2. The task is operational, not conversational — the user wants the deck created, edited, filled, repaired, or reworked.
3. At least one of these applies:
   - charts/graphs/dashboards/data visuals are part of the request
   - an existing PPT/PPTX template must be filled with data or content
   - an existing presentation must be updated while preserving template fidelity
   - the deck requires coordinated narrative + visualization + layout integration

Do **not** trigger this skill for:
- simple questions about PowerPoint
- requests to explain what a PPT/PPTX file is
- pure chart requests with no PowerPoint destination
- simple format conversion with no deck-design workflow
- generic mentions of "slides" where no `.pptx` deliverable is intended

If the user only wants chart design and no PowerPoint output, use `chart-guides` instead.
If the user only wants PPTX inspection/editing with no data-visual workflow, use `powerpoint-pptx` instead.

## Core Orchestration Rule

This skill coordinates the order of work:

1. classify the PPTX task
2. normalize the briefing
3. inspect any existing deck/template before editing
4. use `chart-guides` for chart logic and visual design when charts are needed
5. use `powerpoint-pptx` for template-aware deck integration, editing, and QA
6. run final content + visual QA at the deck level

Do not skip deck inspection when a source `.pptx` exists.
Do not design charts directly inside the PPTX step when `chart-guides` applies.
Do not treat template filling as a generic copy-paste job; placeholders, slide masters, and layout constraints matter.

## Task Classification

Classify the request into one of these flows before acting:

### A. Create a new data-driven deck
Use when the user wants a fresh PowerPoint presentation generated from a topic, dataset, or analysis.

### B. Edit an existing deck
Use when a `.pptx` already exists and the user wants changes, additions, or cleanup.

### C. Replace or improve charts in an existing presentation
Use when the deck exists but the visuals are weak, cluttered, misleading, or outdated.

### D. Fill a PowerPoint template with existing data/content
Use when the user provides a template deck and expects it to be populated with real metrics, charts, summaries, images, or narrative blocks while preserving template fidelity.

### E. Create an executive presentation from existing data
Use when the deck must support a decision, leadership review, client update, or concise business narrative.

## Required Briefing Fields

Extract or request these fields before doing substantial work. Infer only when the context is strong.

### Always collect if possible
- topic / subject of the deck
- end goal or decision the presentation must support
- target audience
- whether the task is create, edit, replace visuals, or fill template
- source data and metric definitions
- required output (`.pptx`, notes, summary, chart spec)

### If a source deck or template exists
- file path / target deck
- whether it is a reusable template or a live presentation
- slides/sections to update if known
- template fidelity constraints
- whether notes/comments/placeholders must be preserved

### If charts are involved
- chart intent: comparison, trend, composition, ranking, distribution, profile
- time grain / category grain
- metric semantics
- number of chart slides or approximate chart count
- density constraints per slide

### Presentation-level constraints
- slide count or budget
- aspect ratio (`16:9`, `4:3`, or template-defined)
- style/tone (executive, technical, commercial, institutional)
- language
- branding or theme constraints

## Template-Fill Workflow

When the user asks to fill a PowerPoint template with existing data, follow this exact logic:

1. inspect the template before planning replacements
2. inventory reusable layouts, placeholders, recurring slide patterns, notes, and any sample content
3. map incoming content/data to the actual destination slides or placeholder families
4. identify which slides require charts versus text/image/table content
5. for chart slides, use `chart-guides` to define the visuals according to the available space and presentation purpose
6. use `powerpoint-pptx` to populate the real template without breaking its theme, master/layout logic, or placeholder targeting
7. run QA for leftover sample text, placeholder junk, clipping, bad chart fit, theme mismatch, and broken narrative flow

Treat template population as a first-class workflow, not a side case.
Do not assume placeholder indexes from one template apply to another.
Do not force data into a visually wrong layout just because the template contains a matching box.

## Flow Selection Rules

### Flow A — New deck from data
- plan the slide narrative around the presentation objective
- identify which slides need charts
- use `chart-guides` to define chart forms
- use `powerpoint-pptx` to build/integrate the deck

### Flow B — Existing deck edit
- inspect the deck first
- identify reusable slides/layouts/placeholders
- decide whether each requested change is text-only, layout-sensitive, or chart-sensitive
- call `chart-guides` only for the chart-sensitive parts
- use `powerpoint-pptx` for all deck edits and final validation

### Flow C — Replace weak charts
- inspect current charts for readability and semantic quality
- redesign each chart family with `chart-guides`
- reinsert with `powerpoint-pptx`
- re-check slide density and narrative coherence

### Flow D — Fill template with existing data
- inspect template structure first
- map data to slide roles and placeholders
- use `chart-guides` only where visuals are actually needed
- use `powerpoint-pptx` to perform template-faithful population
- validate against leftover template artifacts and bad content fit

### Flow E — Executive deck
- reduce density aggressively
- keep visuals high-signal and presentation-safe
- use `chart-guides` for compact chart design
- use `powerpoint-pptx` for final slide hierarchy and polish

## Handoff Rules

### To `chart-guides`
Use `chart-guides` when the deck needs:
- bar charts
- line charts
- scatter plots
- radar charts
- KPI comparison visuals
- dashboard-like summary slides
- any decision about axes, labels, scales, color hierarchy, or chart family

`chart-guides` owns:
- chart type selection
- axis logic
- label strategy
- spacing logic
- color hierarchy
- visual simplification for readability

### To `powerpoint-pptx`
Use `powerpoint-pptx` for:
- deck inspection
- layout and placeholder mapping
- template fidelity
- notes/comments awareness
- inserting charts into real slides
- final visual QA inside the deck
- template population with real content/data

`powerpoint-pptx` owns:
- integration into the actual `.pptx`
- slide-level layout decisions
- master/layout/theme compatibility
- preservation of template logic
- deck rendering sanity checks

## Short Prompt Expansion

If the user gives a short request, expand it internally before acting.

Examples:

### “make a PPTX with these metrics”
Interpret as:
- create a PowerPoint deck
- determine what charts are needed from the metrics
- use `chart-guides` for the visuals
- use `powerpoint-pptx` for the actual deck and QA

### “fill this PPT template with our quarterly data”
Interpret as:
- inspect the template
- map quarterly data to target slides/placeholders
- design chart slides with `chart-guides` when needed
- populate the template via `powerpoint-pptx`
- validate for leftover sample content and layout breakage

### “fix the graphs in this presentation”
Interpret as:
- inspect the existing deck
- identify weak chart slides
- redesign with `chart-guides`
- reinsert and validate with `powerpoint-pptx`

## Canonical Request Patterns

Treat prompts in these families as strong matches for this skill:

- create a `.pptx` presentation from these data and include the necessary charts
- edit this PowerPoint and update the graphs using the new metrics
- fill this PPT/PPTX template with the data/content I already have
- rebuild the chart slides in this presentation but keep the template intact
- create an executive PowerPoint deck from these KPIs and deliver the final `.pptx`

## Preferred Working Skeleton

Normalize the task into this structure whenever possible:

- task type: **[new deck / edit deck / replace charts / fill template / executive deck]**
- topic: **[subject]**
- objective: **[decision/message]**
- audience: **[who will see it]**
- source deck/template: **[path or none]**
- data: **[dataset/metrics]**
- chart needs: **[chart roles]**
- slide constraints: **[count, aspect ratio, density, branding]**
- outputs: **[final `.pptx`, notes, summary, chart spec]**

## Final QA Checklist

Before considering the task done, ensure:
- no leftover template/sample text remains
- chart type matches the message it needs to convey
- labels and legends are readable at slide-viewing distance
- slide density is appropriate for presentation use
- placeholders were targeted correctly
- theme/master/layout behavior did not silently break the result
- notes/comments were preserved if required
- the deck supports the stated objective rather than merely containing data

## Positive vs Negative Trigger Examples

### Strong positive matches — trigger this workflow

- create a `.pptx` with these KPIs and include the necessary charts
- edit this PowerPoint and update the graphs with the new data
- fill this PPT/PPTX template with the quarterly metrics
- replace the weak charts in this deck but keep the template intact
- build an executive PowerPoint from this spreadsheet
- make slides with these metrics and deliver the final deck
- fill these slides with the existing data from our report
- update these slides using the new numbers while preserving the template

### Negative matches — do not trigger this workflow

- what is a PPTX file?
- what is the difference between PPT and PPTX?
- make a chart of sales by region
- convert this presentation to PDF
- summarize the contents of this presentation
- help me brainstorm a talk outline

### Boundary cases

- If the user says `slides`, treat that as PowerPoint/PPTX intent in this workspace unless the context clearly points to another medium.
- If the user says `presentation` without mentioning slides, PowerPoint, PPT, or `.pptx`, infer carefully from context instead of assuming.
- If the user wants only a chart and does not indicate slides/deck/PPTX output, use `chart-guides` instead.
- If the user wants deck editing/filling without data-visual work, use `powerpoint-pptx` instead.
- If the user mentions slides plus real data, template filling, chart updates, deck editing, or final deck delivery, this workflow should trigger.

## Decision Rule For Ambiguous Prompts

Use this routing logic:

1. If the user mentions `.pptx`, `ppt`, `PowerPoint`, `deck`, or `template`, strongly prefer this workflow when the task is operational and deck-focused.
2. If the user mentions `slides`, treat that as a PowerPoint/PPTX request by default for this user/workspace unless another destination is explicit.
3. If the user mentions `slides` plus data, charts, a template, an existing deck, or a final presentation deliverable, trigger this workflow.
4. If the user mentions only chart creation with no slide/deck destination, use `chart-guides`.
5. If the user mentions only PPTX inspection or structural editing with no chart/template-population workflow, use `powerpoint-pptx`.
6. If the request is conceptual rather than operational, do not trigger this workflow.

## Precision Rule

This skill exists to improve routing precision.
If the user request is only loosely related to PowerPoint, do **not** over-trigger this workflow.
Use it only when the main job is a real `.pptx`/slides production, editing, or template-filling pipeline with charts or template population as meaningful parts of the work.
