# Distribution Chart Pattern

Use this guide for histograms and box plots.

> Always apply global rules from [master_style.md](master_style.md) first.

## Histogram

### Use when
- showing the frequency distribution of one continuous variable
- highlighting concentration, skew, spread, and rough modality

### Do not use when
- the audience needs ordinary category comparison instead of bin frequencies
- bin selection would dominate the interpretation and has not been considered carefully

### Style rules
1. Use a single main fill color by default; purple `#6D28D9` is preferred for the primary histogram.
2. Keep bins visually contiguous.
3. Remove unnecessary borders and decoration.
4. Label axes clearly: variable on x-axis, frequency/count or share on y-axis.

### Notes
- Be deliberate about bin width.
- If comparing multiple groups, prefer faceting/small multiples or box plots over overlapping histograms unless overlap is very limited.

## Box plot

### Use when
- comparing distributions across groups
- median, quartiles, spread, and outliers matter

### Do not use when
- the audience will not understand the summary and a simpler chart is enough
- sample size is too small for stable summary interpretation

### Style rules
1. Keep box outlines clear and uncluttered.
2. Use purple for the highlighted group and complementary colors sparingly for others.
3. Show outliers only when they add interpretive value.
4. Label groups and units clearly.

## Quick checklist

- [ ] Distribution is the real question
- [ ] Axis labels clarify what frequency or spread means
- [ ] Bin strategy or summary-stat meaning is defensible
- [ ] Overlap or clutter is controlled
