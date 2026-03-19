#!/usr/bin/env python3
import argparse
import csv
import json
import os
import textwrap
from typing import Any, Dict, List, Tuple

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.patches import FancyBboxPatch

from chart_schema import validate_or_raise
from render_core import render_exec, infer_template_name

PURPLE = '#6D28D9'
SECONDARY = ['#0F766E', '#EA580C', '#2563EB', '#16A34A', '#9333EA', '#DC2626']
NEUTRAL = '#111111'
MUTED = '#5B6470'
BG = '#FFFFFF'
POSITIVE = '#16A34A'
NEGATIVE = '#DC2626'
TOTAL = '#2563EB'
DEFAULT_BAR_ROUNDING = 0.08


def round_bar_patches(ax, rounding: float = DEFAULT_BAR_ROUNDING):
    patches = list(ax.patches)
    for patch in patches:
        x, y = patch.get_x(), patch.get_y()
        w, h = patch.get_width(), patch.get_height()
        if w == 0 or h == 0:
            continue
        fc = patch.get_facecolor()
        ec = patch.get_edgecolor()
        alpha = patch.get_alpha()
        z = patch.get_zorder()
        patch.remove()
        rounded = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={rounding}",
            linewidth=0,
            facecolor=fc,
            edgecolor=ec,
            alpha=alpha,
            mutation_aspect=1,
            zorder=z,
        )
        ax.add_patch(rounded)


def load_json(path: str) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_csv_rows(path: str) -> List[Dict[str, str]]:
    with open(path, 'r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))


def load_data(spec: Dict[str, Any]) -> List[Dict[str, Any]]:
    if 'data' in spec:
        return spec['data']
    data_path = spec.get('data_path')
    if not data_path:
        return []
    return load_csv_rows(data_path)


def apply_style(style: Dict[str, Any]) -> None:
    plt.rcParams.update({
        'font.family': style.get('font_family', 'DejaVu Sans'),
        'font.size': style.get('tick_size', 8),
        'axes.facecolor': BG,
        'figure.facecolor': BG,
        'axes.edgecolor': NEUTRAL,
        'axes.labelcolor': NEUTRAL,
        'xtick.color': NEUTRAL,
        'ytick.color': NEUTRAL,
        'text.color': NEUTRAL,
        'figure.autolayout': False,
    })


def make_figure(style: Dict[str, Any]):
    width = float(style.get('width', 13.33))
    height = float(style.get('height', 7.5))
    fig, ax = plt.subplots(figsize=(width, height), dpi=int(style.get('dpi', 150)))
    return fig, ax


def wrap_label(text: str, width: int = 26) -> str:
    text = str(text)
    return '\n'.join(textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)) or text


def maybe_compact_date(text: str) -> str:
    s = str(text)
    if len(s) == 10 and s[4] == '-' and s[7] == '-':
        return f"{s[8:10]}/{s[5:7]}"
    return s


def format_value(value: float, spec: Dict[str, Any]) -> str:
    kind = spec.get('value_format', 'number')
    decimals = int(spec.get('value_decimals', 0))
    if kind == 'percent':
        return f'{value:.{decimals}f}%'
    if kind == 'currency_brl':
        s = f'{value:,.{decimals}f}'
        s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'R$ {s}'
    if decimals > 0:
        return f'{value:.{decimals}f}'
    if float(value).is_integer():
        return str(int(value))
    return str(value)


def sort_rows(rows: List[Dict[str, Any]], field: str, direction: str) -> List[Dict[str, Any]]:
    reverse = direction.lower() == 'desc'
    return sorted(rows, key=lambda r: float(r[field]), reverse=reverse)


def choose_colors(n: int, highlight_index: int = 0) -> List[str]:
    colors = []
    secondary_iter = iter(SECONDARY)
    for i in range(n):
        if i == highlight_index:
            colors.append(PURPLE)
        else:
            try:
                colors.append(next(secondary_iter))
            except StopIteration:
                colors.append(SECONDARY[(i - 1) % len(SECONDARY)])
    return colors


def detect_variant(spec: Dict[str, Any], rows: List[Dict[str, Any]]) -> str:
    chart_type = spec['chart_type']
    if chart_type == 'bar':
        if spec.get('orientation') == 'horizontal':
            if len(rows) == 1:
                return 'bar_single_horizontal'
            return 'bar_ranking_horizontal'
        if len(rows) == 1:
            return 'bar_single_vertical'
        return 'bar_standard_vertical'
    if chart_type == 'line':
        return 'line_short_series' if len(rows) <= 18 else 'line_dense_series'
    if chart_type == 'scatter':
        return 'scatter_few_points' if len(rows) <= 8 else 'scatter_many_points'
    return chart_type


def draw_titles(fig, spec: Dict[str, Any], style: Dict[str, Any], variant: str) -> None:
    title = spec.get('title')
    subtitle = spec.get('subtitle')
    title_width = 68 if variant.startswith('bar_single') else 74
    subtitle_width = 88 if variant.startswith('bar_single') else 96
    if title:
        fig.suptitle(
            wrap_label(title, int(spec.get('title_wrap', title_width))),
            x=0.01,
            y=0.975,
            ha='left',
            va='top',
            fontsize=style.get('title_size', 14),
            fontweight='bold'
        )
    if subtitle:
        fig.text(
            0.01,
            0.925,
            wrap_label(subtitle, int(spec.get('subtitle_wrap', subtitle_width))),
            ha='left',
            va='top',
            fontsize=style.get('axis_size', 10),
            color=MUTED
        )


def setup_axes(ax, spec: Dict[str, Any], style: Dict[str, Any], variant: str) -> None:
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(NEUTRAL)
    ax.spines['bottom'].set_color(NEUTRAL)
    ax.spines['left'].set_linewidth(0.8)
    ax.spines['bottom'].set_linewidth(0.8)
    ax.tick_params(axis='x', labelsize=style.get('tick_size', 8), length=0)
    ax.tick_params(axis='y', labelsize=style.get('tick_size', 8), length=0)

    if variant == 'bar_single_horizontal':
        ax.spines['left'].set_visible(False)
        ax.set_yticks([])
        ax.set_ylabel('')
    else:
        if spec.get('y_label'):
            ax.set_ylabel(spec['y_label'], fontsize=style.get('axis_size', 10), labelpad=10)

    if spec.get('x_label'):
        ax.set_xlabel(spec['x_label'], fontsize=style.get('axis_size', 10), labelpad=10)

    yfmt = spec.get('y_format')
    if yfmt == 'percent':
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))
    elif yfmt == 'percent_100':
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=100.0))


def compute_margins(spec: Dict[str, Any], rows: List[Dict[str, Any]], variant: str) -> Dict[str, float]:
    margins = {'left': 0.10, 'right': 0.95, 'top': 0.78, 'bottom': 0.18}

    title_lines = max(1, len(wrap_label(spec.get('title', ''), 74).splitlines())) if spec.get('title') else 0
    subtitle_lines = len(wrap_label(spec.get('subtitle', ''), 96).splitlines()) if spec.get('subtitle') else 0
    top = 0.83 - max(0, title_lines - 1) * 0.045 - subtitle_lines * 0.028
    margins['top'] = max(0.66, top)

    if variant == 'bar_single_horizontal':
        margins.update({'left': 0.10, 'right': 0.90, 'top': max(0.70, margins['top']), 'bottom': 0.28})
    elif variant == 'bar_ranking_horizontal':
        label_len = max(len(str(r[spec['x']])) for r in rows) if rows else 0
        margins['left'] = min(0.34, 0.15 + label_len * 0.003)
        margins['right'] = 0.90 if spec.get('show_values', True) else 0.95
        margins['bottom'] = 0.16
    elif variant.startswith('line_'):
        margins['left'] = 0.08
        margins['right'] = 0.97
        margins['bottom'] = 0.24 if len(rows) > 8 else 0.18
    elif variant.startswith('scatter_'):
        margins['left'] = 0.10
        margins['right'] = 0.84 if spec.get('label_key') else 0.95
        margins['bottom'] = 0.18
    return margins


def apply_axis_limits(ax, spec: Dict[str, Any]) -> None:
    if spec.get('y_min') is not None or spec.get('y_max') is not None:
        bottom = spec.get('y_min', ax.get_ylim()[0])
        top = spec.get('y_max', ax.get_ylim()[1])
        ax.set_ylim(bottom=bottom, top=top)
    if spec.get('x_min') is not None or spec.get('x_max') is not None:
        left = spec.get('x_min', ax.get_xlim()[0])
        right = spec.get('x_max', ax.get_xlim()[1])
        ax.set_xlim(left=left, right=right)


def render_bar_single_horizontal(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    row = rows[0]
    label = str(row[spec['x']])
    value = float(row[spec['y']])
    max_val = value if value else 1

    ax.barh([0], [value], color=PURPLE, edgecolor='none', height=0.30)
    ax.set_xlim(left=spec.get('x_min', 0), right=spec.get('x_max', max_val * 1.20))
    ax.set_ylim(-0.7, 0.7)
    ax.set_yticks([])
    ax.set_xticks([0, max_val / 2 if max_val > 1 else 0.5, max_val])
    ax.tick_params(axis='x', labelsize=8, colors=MUTED, pad=6)

    wrapped = wrap_label(label, int(spec.get('label_wrap', 38)))
    ax.text(0, 0.33, wrapped, ha='left', va='bottom', fontsize=10, fontweight='bold', color=NEUTRAL)
    ax.text(value, 0, format_value(value, spec), ha='left', va='center', fontsize=11, fontweight='bold', color=NEUTRAL)


def render_bar_ranking_horizontal(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    if spec.get('sort_by'):
        rows = sort_rows(rows, spec['sort_by'], spec.get('sort_order', 'desc'))
    labels = [wrap_label(str(r[spec['x']]), int(spec.get('label_wrap', 24))) for r in rows]
    values = [float(r[spec['y']]) for r in rows]
    colors = choose_colors(len(values), int(spec.get('highlight_index', 0)))
    ypos = list(range(len(labels)))
    ax.barh(ypos, values, color=colors, edgecolor='none', height=0.56)
    ax.set_yticks(ypos, labels)
    ax.invert_yaxis()
    max_val = max(values) if values else 1
    ax.set_xlim(left=spec.get('x_min', 0), right=spec.get('x_max', max_val * 1.18))
    ax.tick_params(axis='y', pad=8)
    if spec.get('show_values', True):
        for y, v in zip(ypos, values):
            ax.text(v + max(max_val * 0.015, 0.05), y, format_value(v, spec), va='center', ha='left', fontsize=9.5, fontweight='bold')


def render_bar_vertical(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    if spec.get('sort_by'):
        rows = sort_rows(rows, spec['sort_by'], spec.get('sort_order', 'desc'))
    labels = [maybe_compact_date(str(r[spec['x']])) for r in rows]
    values = [float(r[spec['y']]) for r in rows]
    colors = choose_colors(len(values), int(spec.get('highlight_index', 0)))
    xpos = list(range(len(labels)))
    bar_width = 0.48 if len(labels) == 1 else 0.62
    ax.bar(xpos, values, color=colors, edgecolor='none', width=bar_width)
    rotation = spec.get('x_tick_rotation', 0)
    if len(labels) > 8 and rotation == 0:
        rotation = 45
    ax.set_xticks(xpos, labels, rotation=rotation, ha='right' if rotation else 'center')
    max_val = max(values) if values else 1
    ax.set_ylim(bottom=spec.get('y_min', 0), top=spec.get('y_max', max_val * 1.18))
    if spec.get('show_values', True):
        offset = max(max_val * 0.02, 0.1)
        for x, v in zip(xpos, values):
            ax.text(x, v + offset, format_value(v, spec), ha='center', va='bottom', fontsize=9.5, fontweight='bold')


def render_grouped_bar(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    labels = [str(r[spec['x']]) for r in rows]
    series = spec['series']
    colors = choose_colors(len(series), int(spec.get('highlight_index', 0)))
    n = len(series)
    width = 0.72 / max(n, 1)
    xpos = list(range(len(labels)))
    max_seen = 0
    for i, s in enumerate(series):
        vals = [float(r[s]) for r in rows]
        max_seen = max(max_seen, max(vals) if vals else 0)
        offset = (i - (n - 1) / 2) * width
        ax.bar([x + offset for x in xpos], vals, width=width, color=colors[i], edgecolor='none', label=s)
    ax.set_xticks(xpos, [maybe_compact_date(l) for l in labels], rotation=spec.get('x_tick_rotation', 0))
    ax.set_ylim(bottom=spec.get('y_min', 0), top=spec.get('y_max', max_seen * 1.15 if max_seen else 1))
    if spec.get('show_legend', True):
        ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(0, 1.02), fontsize=9, ncol=min(len(series), 3))


def render_stacked_bar(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    labels = [str(r[spec['x']]) for r in rows]
    series = spec['series']
    colors = choose_colors(len(series), 0)
    normalize = spec.get('normalize', False)
    bottom = [0.0] * len(rows)
    xpos = list(range(len(labels)))
    totals = [sum(float(r[s]) for s in series) for r in rows]
    for i, s in enumerate(series):
        vals = [float(r[s]) for r in rows]
        if normalize:
            vals = [(v / t * 100) if t else 0 for v, t in zip(vals, totals)]
        ax.bar(xpos, vals, bottom=bottom, color=colors[i], edgecolor='none', label=s, width=0.56)
        bottom = [b + v for b, v in zip(bottom, vals)]
    round_bar_patches(ax)
    ax.set_xticks(xpos, [maybe_compact_date(l) for l in labels], rotation=spec.get('x_tick_rotation', 0))
    if normalize:
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=100.0))
    if spec.get('show_legend', True):
        ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(0, 1.02), fontsize=9, ncol=min(len(series), 3))


def render_line(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]], variant: str):
    x_key = spec['x']
    y_keys = spec['y'] if isinstance(spec['y'], list) else [spec['y']]
    xs = [maybe_compact_date(r[x_key]) for r in rows]
    colors = choose_colors(len(y_keys), int(spec.get('highlight_index', 0)))
    max_seen = 0
    for idx, y_key in enumerate(y_keys):
        ys = [float(r[y_key]) for r in rows]
        if ys:
            max_seen = max(max_seen, max(ys))
        ax.plot(xs, ys, color=colors[idx], marker='o', linewidth=2.1 if variant == 'line_short_series' else 1.8, markersize=5, label=y_key)
    if len(xs) > 8:
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
            tick.set_horizontalalignment('right')
    if max_seen:
        ax.set_ylim(bottom=spec.get('y_min', 0), top=spec.get('y_max', max_seen * 1.20))
    if spec.get('show_values', False) and y_keys:
        ys = [float(r[y_keys[0]]) for r in rows]
        offset = max(max_seen * 0.025, 0.1)
        for i, (x, y) in enumerate(zip(xs, ys)):
            if i in {0, len(xs)-1} or y == max_seen:
                ax.text(x, y + offset, format_value(y, spec), ha='center', va='bottom', fontsize=8.5, fontweight='bold')
    if len(y_keys) > 1 and spec.get('show_legend', True):
        ax.legend(frameon=False, loc='upper left', bbox_to_anchor=(0, 1.02), fontsize=9, ncol=min(len(y_keys), 3))


def render_scatter(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]], variant: str):
    x_key = spec['x']
    y_key = spec['y']
    label_key = spec.get('label_key')
    xs = [float(r[x_key]) for r in rows]
    ys = [float(r[y_key]) for r in rows]
    labels = [str(r.get(label_key, '')) for r in rows] if label_key else []
    ax.scatter(xs, ys, s=spec.get('marker_size', 50), color=PURPLE, edgecolors='white', linewidths=0.8, alpha=spec.get('alpha', 0.9))
    if xs:
        xmax = max(xs) if max(xs) else 1
        ax.set_xlim(left=spec.get('x_min', 0), right=spec.get('x_max', xmax * 1.20))
    if ys:
        ymax = max(ys) if max(ys) else 1
        ax.set_ylim(bottom=spec.get('y_min', 0), top=spec.get('y_max', ymax * 1.25))
    if label_key:
        ranked = sorted(zip(xs, ys, labels), key=lambda t: (t[1], t[0]), reverse=True)
        max_labels = int(spec.get('max_labels', 3 if variant == 'scatter_few_points' else 4))
        for i, (x, y, label) in enumerate(ranked[:max_labels]):
            dx = (max(xs) * 0.02 if xs else 0.1)
            dy = (max(ys) * 0.05 if ys else 0.1) * (1 if i % 2 == 0 else -1)
            ax.text(x + dx, y + dy, wrap_label(label, 20), fontsize=8, va='center', ha='left')


def render_histogram(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    values = [float(r[spec['x']]) for r in rows]
    ax.hist(values, bins=spec.get('bins', 10), color=PURPLE, edgecolor='white')


def render_heatmap(ax, spec: Dict[str, Any]):
    matrix = spec['matrix']
    im = ax.imshow(matrix, cmap=spec.get('cmap', 'Purples'), aspect='auto')
    x_labels = spec.get('x_labels', [str(i) for i in range(len(matrix[0]))])
    y_labels = spec.get('y_labels', [str(i) for i in range(len(matrix))])
    ax.set_xticks(range(len(x_labels)), x_labels)
    ax.set_yticks(range(len(y_labels)), y_labels)
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    if spec.get('show_values', False):
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                ax.text(j, i, format_value(float(val), spec), ha='center', va='center', fontsize=9, fontweight='bold', color=NEUTRAL)


def render_waterfall(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    labels = [wrap_label(str(r[spec['x']]), 18) for r in rows]
    values = [float(r[spec['y']]) for r in rows]
    types = spec.get('measure_types', ['relative'] * len(rows))
    starts = []
    heights = []
    running = 0.0
    colors = []
    for v, mtype in zip(values, types):
        if mtype == 'total':
            start = 0.0
            height = v
            running = v
            colors.append(TOTAL)
        else:
            start = running if v >= 0 else running + v
            height = abs(v)
            running += v
            colors.append(POSITIVE if v >= 0 else NEGATIVE)
        starts.append(start)
        heights.append(height)
    xpos = list(range(len(labels)))
    ax.bar(xpos, heights, bottom=starts, color=colors, edgecolor='none', width=0.56)
    round_bar_patches(ax)
    ax.set_xticks(xpos, labels, rotation=0)
    if spec.get('show_values', True) and heights:
        max_top = max(s + h for s, h in zip(starts, heights))
        offset = max(max_top * 0.02, 0.1)
        for x, s, h, raw in zip(xpos, starts, heights, values):
            ax.text(x, s + h + offset, format_value(raw, spec), ha='center', va='bottom', fontsize=9, fontweight='bold')


def render_slope(ax, spec: Dict[str, Any], rows: List[Dict[str, Any]]):
    label_key = spec['label_key']
    start_key = spec['start_key']
    end_key = spec['end_key']
    colors = choose_colors(len(rows), int(spec.get('highlight_index', 0)))
    ax.set_xlim(-0.2, 1.2)
    ax.set_xticks([0, 1], [spec.get('left_label', 'Before'), spec.get('right_label', 'After')])
    for idx, row in enumerate(rows):
        start = float(row[start_key])
        end = float(row[end_key])
        color = colors[idx]
        ax.plot([0, 1], [start, end], color=color, linewidth=2.0)
        ax.scatter([0, 1], [start, end], color=color, s=35)
        ax.text(-0.03, start, f"{row[label_key]}  {format_value(start, spec)}", ha='right', va='center', fontsize=9)
        ax.text(1.03, end, f"{format_value(end, spec)}  {row[label_key]}", ha='left', va='center', fontsize=9)


def should_use_exec_template(spec: Dict[str, Any], rows: List[Dict[str, Any]]) -> bool:
    if spec.get('presentation_template'):
        return True
    if spec.get('destination') in {'presentation', 'ppt', 'pptx', 'slide', 'slides'}:
        return True
    try:
        infer_template_name(spec, rows)
        return True
    except Exception:
        return False


def render(spec: Dict[str, Any], out_path: str) -> None:
    spec = validate_or_raise(spec)
    rows = load_data(spec)
    if should_use_exec_template(spec, rows):
        try:
            render_exec(spec, out_path, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
            return
        except Exception:
            pass

    style = spec.get('style', {})
    apply_style(style)
    variant = detect_variant(spec, rows)
    fig, ax = make_figure(style)
    draw_titles(fig, spec, style, variant)
    setup_axes(ax, spec, style, variant)

    chart_type = spec['chart_type']
    if chart_type == 'bar':
        if variant == 'bar_single_horizontal':
            render_bar_single_horizontal(ax, spec, rows)
        elif variant == 'bar_ranking_horizontal':
            render_bar_ranking_horizontal(ax, spec, rows)
        else:
            render_bar_vertical(ax, spec, rows)
    elif chart_type == 'grouped_bar':
        render_grouped_bar(ax, spec, rows)
    elif chart_type == 'stacked_bar':
        render_stacked_bar(ax, spec, rows)
    elif chart_type == 'line':
        render_line(ax, spec, rows, variant)
    elif chart_type == 'scatter':
        render_scatter(ax, spec, rows, variant)
    elif chart_type == 'histogram':
        render_histogram(ax, spec, rows)
    elif chart_type == 'heatmap':
        render_heatmap(ax, spec)
    elif chart_type == 'waterfall':
        render_waterfall(ax, spec, rows)
    elif chart_type == 'slope':
        render_slope(ax, spec, rows)
    else:
        raise ValueError(f'Unsupported chart_type: {chart_type}')

    apply_axis_limits(ax, spec)
    margins = compute_margins(spec, rows, variant)
    fig.subplots_adjust(left=margins['left'], right=margins['right'], top=margins['top'], bottom=margins['bottom'])
    fig.savefig(out_path)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description='Render deterministic charts from a validated JSON spec.')
    parser.add_argument('--spec', required=True, help='Path to JSON chart spec')
    parser.add_argument('--output', required=True, help='Output image path (png, jpg, etc.)')
    args = parser.parse_args()

    spec = load_json(args.spec)
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    render(spec, args.output)


if __name__ == '__main__':
    main()

