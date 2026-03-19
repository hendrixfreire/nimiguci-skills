---
name: Powerpoint / PPTX
slug: powerpoint-pptx
version: 1.0.1
homepage: https://clawic.com/skills/powerpoint-pptx
description: "Create, inspect, and edit Microsoft PowerPoint presentations and PPTX decks with reliable layouts, templates, placeholders, notes, charts, and visual QA. Use when (1) the task is about PowerPoint or `.pptx`; (2) layouts, placeholders, notes, charts, comments, or template fidelity matter; (3) the deck must render cleanly after edits. When charts or graphs are part of the deck, also use the `chart-guides` skill to design and generate the chart specification before placing it into the PPTX workflow."
changelog: Rebalanced the skill toward template inventory, layout mapping, and higher-signal QA after a stricter external audit.
metadata: {"clawdbot":{"emoji":"📊","requires":{"bins":[]},"os":["linux","darwin","win32"]}}
---

## When to Use

Use when the main artifact is a Microsoft PowerPoint presentation or `.pptx` deck, especially when layouts, templates, placeholders, notes, comments, charts, extraction, editing, or final visual quality matter.

## Core Rules

### 0. Treat template filling as a first-class PPTX workflow

- If the user provides a PowerPoint template and wants it filled with existing data, narrative, charts, images, or summaries, treat that as a primary workflow for this skill.
- Inspect the template before editing it; inventory reusable layouts, placeholders, notes, comments, recurring slide patterns, and sample content.
- Map incoming content to the real slide structure before replacing anything.
- Preserve template fidelity over generic redesign instincts unless the user explicitly asks for a redesign.
- A filled template should look like the template was meant for that content, not like data was shoved into vaguely similar boxes.
- Check for leftover sample text, placeholder junk, broken chart fit, theme inheritance issues, and clipped content after population.

### 0. Pair with `chart-guides` whenever charts are needed

- If the PPTX task includes any chart, graph, dashboard slide, KPI visual, comparison plot, or data visualization, use the `chart-guides` skill alongside this skill.
- Use `chart-guides` first to define the right chart type, axis logic, labeling, spacing, color hierarchy, and visual structure.
- Then use this PowerPoint skill to place that chart into the deck in a way that respects the real template, placeholders, slide layout, theme, notes, and final render quality.
- Do not improvise chart design inside the PPTX workflow when `chart-guides` applies; chart choice and chart structure should come from `chart-guides`, while template fidelity and slide integration stay here.
- If the presentation contains multiple chart slides, apply `chart-guides` slide by slide or chart family by chart family before editing the deck.

### 1. Choose the workflow before touching the deck

- Reading text, editing an existing deck, rebuilding from a template, and creating from scratch are different jobs with different failure modes.
- For text extraction or inspection, read the deck before editing it.
- Text extraction plus thumbnail-style visual inspection is safer than editing from shape assumptions alone.
- For template-driven work, inventory the deck before replacing content.
- For deep edits, remember a `.pptx` file is OOXML with separate parts for slides, layouts, masters, media, notes, and comments.
- If a template exists, template fidelity beats generic slide-design instincts.
- Reusing or duplicating a good existing slide is often safer than rebuilding it and hoping the theme still matches.

### 2. Inventory the deck before replacing content

- Count the reusable layouts, real placeholders, notes, comments, media, and recurring typography or color patterns first.
- Placeholder indexes and layout indexes are not portable assumptions.
- Inspect the actual slide or template before targeting title, body, chart, or image shapes.
- Speaker notes, comments, and linked assets can live outside the visible slide surface.
- A missing or wrong placeholder target can silently land content in the wrong box or wrong layer.
- Master and layout settings can override local slide edits, so the visible problem is not always on the slide you are editing.

### 3. Match content to the actual placeholders

- Count the actual content pieces before choosing a layout.
- Pick layouts based on the real number of ideas, columns, images, or charts the slide needs.
- Do not force two ideas into a three-column slide or cram dense text under a chart.
- Category counts and data series lengths must match or charts will break in ugly ways.
- Explicit sizing beats wishful thinking: text boxes, images, and charts need real space, not "it should fit".
- Do not choose a layout with more placeholders than the content can meaningfully fill.
- Quote layouts are for real quotes, and image-led layouts are for slides that actually have images.
- For chart-, table-, or image-heavy slides, full-slide or two-column layouts are usually safer than stacking dense text above the visual.

### 4. Preserve the deck's visual language

- Theme, master, and layout files usually decide fonts, colors, and hierarchy more than any one slide does.
- Start from the deck's actual theme, fonts, spacing, and aspect ratio instead of improvising a new style.
- Reuse the deck's own alignment and spacing system instead of inventing a second visual language.
- Use common fonts for portability and strong contrast for readability.
- Preserve the template's visual logic first; originality matters less than not breaking the deck's existing language.
- Combining slides from multiple sources requires normalizing themes, masters, and alignment afterward.

### 5. Run content QA and visual QA separately

- Text overflow, bad alignment, clipped shapes, weak contrast, and placeholder leftovers are normal first-pass failures.
- Run both content QA and visual QA; missing text and broken layout are different failure classes.
- Render or inspect the actual deck output before delivery when layout matters.
- Search for leftover template junk, sample labels, and placeholder text before calling the deck finished.
- Check notes, comments, labels, legends, and chart/table semantics separately from the visual pass.
- A deck can pass text extraction and still fail on overlap, clipping, wrong theme inheritance, or broken notes.
- Thumbnail grids and rendered slides usually reveal layout bugs faster than code or text inspection.
- Assume the first render is wrong and do at least one fix-and-verify cycle before calling the deck finished.
- Re-check affected slides after each fix because one spacing change often creates another issue.

### 6. Keep decks portable and review-safe

- Template masters can override direct edits in surprising ways.
- Complex effects may degrade across PowerPoint, LibreOffice, and conversion pipelines, so keep important content robust without them.
- Image sizing, font substitution, and placeholder mismatch are common reasons a deck looks good in code and bad on screen.
- Notes, comments, linked media, and merged decks can stay broken even when the visible slide looks fine.

## Common Traps

- Placeholder text and sample charts often survive template reuse if not explicitly replaced.
- Directly editing one slide can fail if the real issue lives in the master or layout.
- Charts, icons, and text boxes need enough space; near-collisions are usually visible only after rendering.
- Layout indexes vary by template, so built-in assumptions from one deck often break in another.
- A missing placeholder or wrong shape target can silently put content in the wrong place.
- Counting the text ideas after choosing the layout usually leads to empty placeholders, weak hierarchy, or leftover template junk.
- Font substitution can move line breaks and wreck careful spacing.
- Speaker notes, comments, and linked media can stay broken even when the visible slide looks fine.
- A deck can pass text inspection and still fail visually because of overlap, contrast, or edge clipping.
- Editing from one slide alone can miss the real source of truth in the theme, master, or layout definitions.
- Choosing a quote, comparison, or multi-column layout without matching content usually makes the deck look templated rather than intentional.
- Combining or duplicating slides without checking masters and themes can create subtle inconsistency slide by slide.
- Aspect-ratio mismatches like `16:9` versus `4:3` can shift every placement decision even when each slide looks locally reasonable.

## Invocation Patterns

When the user asks for PPTX generation or editing, prefer extracting these fields explicitly from the request or inferring them carefully from context:

- objective of the presentation
- whether the task is create-from-scratch, edit-existing-deck, or replace/improve visuals in an existing deck
- audience
- desired tone (executive, technical, commercial, institutional)
- slide format or aspect ratio (`16:9`, `4:3`, or template-defined)
- template constraints and placeholder fidelity requirements
- number of slides or slide budget
- chart/data needs
- per-slide density constraints (for example, one chart plus a few bullets)
- required outputs (`.pptx`, slide summary, notes, chart specs)

If charts are involved, first extract or request the dataset, metric definitions, time granularity, category structure, and comparison intent before choosing chart layouts.

## Request Templates To Recognize And Reuse

Treat prompts in these families as canonical invocation formats for this skill:

### 0. Fill an existing PowerPoint template with real data/content

- User pattern: fill a provided PPT/PPTX template using existing business data, narrative, summaries, charts, images, or status updates.
- Working pattern:
  - inspect the template first
  - inventory layouts, placeholders, reusable slide archetypes, notes, and any sample/template content
  - map the incoming content to the correct slide roles
  - invoke `chart-guides` for any chart-bearing slide
  - use the PPTX workflow to populate the actual template without breaking its visual language

Expected request fields:
- target template file
- source content/data
- slides or sections to populate if known
- fidelity constraints
- output expectations

### 1. Create a deck with charts from scratch

- User pattern: create a PPTX about a topic, define the charts from data, and assemble the final deck.
- Working pattern:
  - create the presentation structure around the stated objective
  - invoke `chart-guides` for the graph specifications
  - integrate those visuals into the deck with template-aware layout choices

Expected request fields:
- theme/topic
- slide count
- tone
- chart intent (comparison, trend, composition, distribution)
- source data

### 2. Edit an existing PPTX with new charts

- User pattern: edit a supplied `.pptx`, replace or add chart slides, preserve the template.
- Working pattern:
  - inspect the current deck first
  - inventory layouts, placeholders, notes, and reusable slides
  - invoke `chart-guides` for the new or revised visuals
  - apply changes through the PPTX workflow without breaking the deck

Expected request fields:
- target file
- affected slides or sections if known
- new data
- visual or template preservation constraints

### 3. Replace weak charts with better ones

- User pattern: review a presentation, identify poor charts, and redesign them.
- Working pattern:
  - inspect the deck for weak, misleading, cluttered, or visually inconsistent charts
  - use `chart-guides` to redesign each chart family
  - reinsert the improved versions with PPTX-aware layout validation

Expected request fields:
- target file
- review goal
- data source or permission to infer from current charts
- degree of redesign allowed

### 4. Build an executive presentation

- User pattern: create a decision-oriented deck for leadership or clients.
- Working pattern:
  - keep slide density low
  - emphasize visual clarity and message hierarchy
  - use `chart-guides` for concise, presentation-safe chart specs
  - use PPTX integration rules to avoid overloaded slides

Expected request fields:
- audience
- decision or takeaway the deck must support
- style
- density limit per slide
- source data

### 5. Short-form direct invocation

Interpret short prompts like these as sufficient to trigger the full combined workflow:
- generate a PPTX using `chart-guides` for charts and `powerpoint-pptx` for final integration
- edit this PPTX using `chart-guides` for graphs and `powerpoint-pptx` for the deck
- create a deck with charts from these data and deliver the final `.pptx`

## Prompt Expansion Heuristic

When a user gives a short request, expand it internally into this structure before acting:

- task: create or edit a `.pptx`
- topic: what the deck is about
- audience: who will consume it
- objective: what decision, explanation, or persuasion the deck must support
- visual layer: what charts are needed and why
- deck constraints: template, aspect ratio, slide count, density, notes, placeholders
- outputs: final `.pptx` and any requested summary/specification

A compact request such as “make a PPTX with these metrics” should therefore be interpreted as a request to:
- identify the best chart forms with `chart-guides`
- integrate them into a coherent slide narrative with `powerpoint-pptx`
- preserve template logic if a source deck exists
- validate the final deck visually, not only textually

## Preferred Prompt Skeleton

Use or infer this structure whenever possible:

- Create or edit a `.pptx` about **[topic]**.
- Use **`chart-guides`** to define the charts based on **[data]**.
- Then use **`powerpoint-pptx`** to integrate everything into the final deck with fidelity to **[template/layout]**.
- Audience: **[audience]**.
- Style/tone: **[style]**.
- Format: **[16:9 / 4:3 / template-defined]**.
- Objective: **[decision or message to support]**.
- Output: **[final `.pptx`, summary, notes, chart specs]**.

## Related Skills
Install with `clawhub install <slug>` if user confirms:
- `chart-guides` — Required companion when the deck needs charts, graphs, dashboards, or any data visualization; use it to define chart form before integrating into PPTX slides.
- `documents` — Document workflows that often feed presentation content.
- `design` — Visual direction and layout decisions.
- `brief` — Concise business messaging for slide narratives.

## Feedback

- If useful: `clawhub star powerpoint-pptx`
- Stay updated: `clawhub sync`
