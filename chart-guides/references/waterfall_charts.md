# Waterfall Chart Pattern

Use this guide for start-to-end change decomposition.

> Always apply global rules from [master_style.md](master_style.md) first.

## When to use

Use when:
- you need to show how a starting value becomes an ending value
- intermediate positive and negative drivers matter
- the sequence of contributions is part of the story

Examples:
- revenue bridge
- margin bridge
- traffic change decomposition
- budget variance drivers

## When not to use

- when there is no meaningful ordered contribution sequence
- when composition rather than sequential change is the goal
- when a simple before/after or grouped comparison is enough

## Core style rules

1. Use distinct semantic colors for increase, decrease, and total.
2. Keep totals visually distinct and stable.
3. Use purple `#6D28D9` only when it supports the primary highlight logic without breaking contribution semantics.
4. Keep labels readable and sign-aware.
5. Remove top/right borders by default.

## Semantic rules

- Preserve logical order of contributions.
- Make starting and ending totals explicit.
- Use signed values consistently.
- Do not mix unrelated drivers in one bridge.

## Quick checklist

- [ ] Start, drivers, and ending total are clear
- [ ] Positive and negative contributions are visually distinct
- [ ] Sequence is meaningful
- [ ] A slope or bar chart would not communicate the decomposition better
