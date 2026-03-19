# Anti-Patterns: When to Use and When Not to Use Each Chart Type

Use this file to reject weak chart choices before styling.

## Bar charts

### Use when
- comparing category values directly
- showing rankings
- comparing a few discrete periods where category-like reading is acceptable

### Do not use when
- the x-axis is a long, dense time series better read as a line
- there are too many categories to label legibly
- the true story is distribution, relationship, or contribution to change

### Common mistakes
- truncating the y-axis baseline on bars without clear justification
- leaving categories unsorted when ranking is the real task
- stuffing too many colors into a simple comparison

## Grouped bars

### Use when
- comparing a few subgroups within each category
- exact subgroup comparison matters

### Do not use when
- there are too many subgroups or categories
- composition is more important than exact subgroup values

### Common mistakes
- using grouped bars with so many bars that legend decoding becomes the main task

## Stacked bars / 100% stacked bars

### Use when
- the goal is part-to-whole comparison
- the total and composition both matter
- share comparison matters more than exact internal segment alignment in 100% stacked views

### Do not use when
- the audience must compare middle segments precisely across many categories
- there are too many segments or categories
- the total itself is the only story and segmentation adds noise

### Common mistakes
- using stacked bars because they look sophisticated while hiding the actual comparison

## Line charts

### Use when
- showing ordered or temporal progression
- comparing a few related trends over time

### Do not use when
- categories are unordered and non-temporal
- there are too many series for one panel
- only one or two disconnected points exist and a simpler comparison would be clearer

### Common mistakes
- smoothing curves and inventing a trajectory not supported by the data
- using too many lines with similar colors

## Area charts

### Use when
- the sense of total magnitude over time matters
- cumulative volume is part of the story

### Do not use when
- exact line comparison is important
- multiple filled areas overlap and reduce readability
- the visual becomes visually heavier than the message requires

### Common mistakes
- using area instead of line just to make the chart feel more dramatic

## Scatter plots

### Use when
- the relationship between two continuous variables matters
- outliers, clusters, or dispersion are part of the analysis

### Do not use when
- time trend is the actual story
- the data is too dense and no overplotting strategy exists
- categories alone are being compared without continuous-variable reasoning

### Common mistakes
- not handling overplotting with transparency, jitter, aggregation, or faceting
- adding a bubble size encoding that no one can read reliably

## Histograms

### Use when
- frequency distribution of one continuous variable matters
- spread, skew, and concentration matter

### Do not use when
- the user needs direct category comparison rather than bins
- bin choice changes the story and is not considered carefully

### Common mistakes
- presenting arbitrary bins without explaining frequency context

## Box plots

### Use when
- comparing distributions across groups
- median, quartiles, and outliers matter more than every individual value

### Do not use when
- the audience is unfamiliar and needs a simpler summary without support
- sample size is tiny and summary statistics are unstable

### Common mistakes
- using box plots without clarifying what the whiskers or points represent

## Heatmaps

### Use when
- many values form a matrix better read by intensity than by bar length
- calendar, correlation-like, or category-by-time grids matter

### Do not use when
- exact value comparison is central and color decoding would slow reading
- the palette is not perceptually ordered

### Common mistakes
- using rainbow palettes that destroy ordinal meaning
- failing to label the scale clearly

## Waterfall charts

### Use when
- showing how a starting number changes through sequential positive and negative drivers to an ending number

### Do not use when
- there is no meaningful ordered sequence of contributions
- composition rather than sequential change is the story

### Common mistakes
- mixing unrelated categories into a waterfall just because deltas exist

## Bullet charts

### Use when
- comparing actual vs target/benchmark efficiently
- qualitative performance bands add meaning

### Do not use when
- the audience will not understand the target context and a simple bar with target line is clearer
- too many qualitative bands clutter the chart

### Common mistakes
- overloading the bullet with too many reference markers

## Slope charts

### Use when
- showing how categories changed between exactly two points or states
- direction and rank movement matter

### Do not use when
- more than two or three points need to be shown consistently
- labels cannot be kept readable at both ends

### Common mistakes
- forcing many categories into one slope chart until it becomes spaghetti with ambitions

## Radar plots

### Use when
- comparing a few entities across a shared, normalized set of dimensions
- shape comparison itself adds value

### Do not use when
- dimensions are not normalized
- units are incompatible
- more than a few entities or dimensions create clutter
- precise value comparison matters more than overall profile shape

### Common mistakes
- using radar because it looks premium while saying less than a grouped bar

## Small multiples

### Use when
- one chart would be overloaded by too many series or categories
- repeated aligned views enable faster comparison

### Do not use when
- the repeated panels become too tiny to read
- the viewer actually needs one integrated comparison with shared overlap

### Common mistakes
- changing scales between panels without making it explicit
