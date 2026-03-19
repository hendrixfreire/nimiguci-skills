# Chart Selection Guide

Use this file to choose the chart family before styling.

## 1. Start from the communication goal

### Comparison
Use when the user wants to compare values across categories, teams, channels, products, regions, or periods.

Preferred charts:
- Vertical bar for a moderate number of short category labels
- Horizontal bar for long labels or clear ranking
- Dot/lollipop when a lighter visual is enough
- Grouped bar when comparing a few subgroups per category

Avoid:
- Radar for simple category comparison
- Pie-like thinking when exact comparison matters
- Stacked bars if the real question is subgroup-to-subgroup comparison

### Trend over time
Use when the x-axis is temporal or ordered and the goal is to show direction, stability, acceleration, seasonality, or change.

Preferred charts:
- Single-series line for one metric over time
- Multi-series line for 2 to 4 related metrics
- Small multiples when too many lines would overlap
- Area chart only when total magnitude emphasis is important and exact line comparison is secondary

Avoid:
- Bar charts for long or dense time series unless discrete periods are few and comparison is the point
- Multi-series line with too many series

### Composition / part-to-whole
Use when the goal is to show how pieces contribute to a total.

Preferred charts:
- Stacked bar for a few categories or periods
- 100% stacked bar when share matters more than absolute values
- Stacked area for composition changing over time, only if trend and composition remain readable

Avoid:
- Stacked visuals when comparing internal segment values precisely is the main task
- Too many segments with similar colors

### Relationship / correlation
Use when the goal is to show how one metric moves relative to another.

Preferred charts:
- Scatter plot
- Bubble chart if a justified third metric is encoded by size
- Small multiples if categories need separate views

Avoid:
- Line charts unless the sequence itself matters
- Bar charts for continuous-variable relationship

### Distribution
Use when the goal is to show spread, skew, concentration, frequency, quartiles, or outliers.

Preferred charts:
- Histogram for frequency distribution of a continuous metric
- Box plot for comparing distributions across groups
- Scatter/strip style overlays only if density remains readable

Avoid:
- Bar charts of many numeric bins pretending to be ordinary categories without stating that it is a distribution

### Contribution to change
Use when the goal is to explain how a starting value becomes an ending value through intermediate positive and negative drivers.

Preferred charts:
- Waterfall chart

Avoid:
- Stacked bars when the sequence of contributions is the actual story

### Target tracking
Use when the goal is to compare actual performance with target, benchmark, threshold, or qualitative range.

Preferred charts:
- Bullet chart
- Bar or dot chart with target/reference line

Avoid:
- Gauge-like metaphors unless the medium explicitly demands them and precision is secondary

### Before vs after / two-point change
Use when categories have two time points or two states and the change itself matters.

Preferred charts:
- Slope chart
- Grouped bar if exact bar length comparison is more important than trajectory

Avoid:
- Full line chart with only two points unless a consistent system across many visuals requires it

### Matrix intensity / cross-tab signal
Use when values are better read as a matrix or grid than as many individual bars.

Preferred charts:
- Heatmap

Avoid:
- Dense grouped bars that make the matrix unreadable

### Multidimensional profile
Use when multiple entities must be compared across the same normalized dimensions.

Preferred charts:
- Radar plot only when there are few dimensions and entities, and normalization is valid
- Small multiples or grouped bars if precise comparison matters more than shape comparison

Avoid:
- Radar for non-normalized or semantically incompatible metrics

## 2. Quick routing by dataset shape

- One categorical dimension + one metric → bar / dot / lollipop
- One temporal dimension + one metric → line
- One temporal dimension + several related metrics → multi-series line or small multiples
- Two continuous metrics → scatter
- One continuous metric → histogram
- Start + drivers + ending total → waterfall
- Categories + contribution shares → stacked or 100% stacked bar
- Groups + distribution comparison → box plot
- Matrix or category x time grid → heatmap
- Two states across categories → slope chart

## 3. Escalation rules

Escalate from a standard chart to a more specialized one only when justified:
- bar → grouped bar only if subgroup comparison matters
- grouped bar → stacked only if composition matters more than exact subgroup comparison
- line → small multiples if 5+ series create clutter
- scatter → bubble only if the third metric adds real value
- bar → bullet if the real story is actual vs target with performance zones
- bar → waterfall if sequential contribution to change is the story

## 4. Executive simplification rule

For executive slides, default to:
- bar
- line
- dot/lollipop
- bullet
- slope

Escalate to heatmap, waterfall, stacked visuals, radar, or dense scatter only when they clearly improve understanding.
