#!/usr/bin/env python3
import csv
import json
import os
import textwrap
from typing import Any, Dict, List

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from matplotlib.patches import FancyBboxPatch

from chart_schema import validate_or_raise

NEUTRAL = '#111111'
MUTED = '#5B6470'
DEFAULT_SECONDARY = ['#0F766E', '#EA580C', '#2563EB', '#16A34A', '#9333EA', '#DC2626']
DEFAULT_BAR_ROUNDING = 1.89


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
        # Clamp by the bar thickness so rounded corners stay visible without creating
        # a bump/capsule artifact at the bar end.
        thickness = min(abs(w), abs(h))
        rounding_size = min(thickness * 0.48, max(0.04, thickness * rounding * 0.18))
        patch.remove()
        rounded = FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f"round,pad=0,rounding_size={rounding_size}",
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
    if spec.get('data_path'):
        return load_csv_rows(spec['data_path'])
    return []


def wrap_text(text: str, width: int) -> str:
    return '\n'.join(textwrap.wrap(str(text), width=width, break_long_words=False, break_on_hyphens=False)) or str(text)


def format_value(value: float, spec: Dict[str, Any]) -> str:
    kind = spec.get('value_format', 'number')
    decimals = int(spec.get('value_decimals', 0))
    if kind == 'percent':
        return f'{value:.{decimals}f}%'
    if kind == 'currency_brl':
        s = f'{value:,.{decimals}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'R$ {s}'
    if decimals > 0:
        return f'{value:.{decimals}f}'
    if float(value).is_integer():
        return str(int(value))
    return str(value)


def choose_colors(n: int, palette: Dict[str, Any], highlight_index: int = 0):
    primary = palette.get('primary_color', palette.get('color', '#6D28D9'))
    secondary = palette.get('secondary_colors', DEFAULT_SECONDARY)
    colors = []
    sec_i = 0
    for i in range(n):
        if i == highlight_index:
            colors.append(primary)
        else:
            colors.append(secondary[sec_i % len(secondary)])
            sec_i += 1
    return colors


def apply_base_style(template: Dict[str, Any]):
    fig_cfg = template['figure']
    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'figure.facecolor': fig_cfg.get('background', '#FFFFFF'),
        'axes.facecolor': fig_cfg.get('background', '#FFFFFF'),
        'axes.edgecolor': NEUTRAL,
        'axes.labelcolor': NEUTRAL,
        'xtick.color': MUTED,
        'ytick.color': NEUTRAL,
        'text.color': NEUTRAL,
    })


def add_titles(fig, spec: Dict[str, Any], template: Dict[str, Any]):
    t = template['title']
    st = template['subtitle']
    if spec.get('title'):
        fig.suptitle(wrap_text(spec['title'], t.get('wrap', 72)), x=t['x'], y=t['y'], ha='left', va='top', fontsize=t['fontsize'], fontweight=t.get('fontweight', 'bold'))
    if spec.get('subtitle'):
        fig.text(st['x'], st['y'], wrap_text(spec['subtitle'], st.get('wrap', 90)), ha='left', va='top', fontsize=st['fontsize'], color=st.get('color', MUTED))


def style_axes(ax, spec: Dict[str, Any], template: Dict[str, Any]):
    axis = template['axis']
    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(axis.get('show_left_spine', True))
    ax.spines['bottom'].set_visible(axis.get('show_bottom_spine', True))
    if not axis.get('show_y', True):
        ax.set_yticks([])
        ax.set_ylabel('')
    elif spec.get('y_label'):
        ax.set_ylabel(spec['y_label'], fontsize=10, labelpad=10)
    if spec.get('x_label'):
        ax.set_xlabel(spec['x_label'], fontsize=10, labelpad=axis.get('xlabel_pad', 10))
    ax.tick_params(axis='x', length=0, labelsize=8)
    ax.tick_params(axis='y', length=0, labelsize=8, pad=template.get('category_label', {}).get('pad', 6))
    if not axis.get('show_xticks', True):
        ax.set_xticklabels([])
        ax.tick_params(axis='x', which='both', bottom=False)


def render_single_bar_exec(ax, spec, template, rows):
    row = rows[0]
    label = str(row[spec['x']])
    value = float(row[spec['y']])
    max_val = max(value, 1.0)
    bar_cfg = template['bar']; label_cfg = template['category_label']; value_cfg = template['value_label']
    x_start = max_val * bar_cfg.get('x_start_ratio', 0.08)
    x_end = max_val * bar_cfg.get('x_end_ratio', 0.82)
    bar_length = max(x_end - x_start, max_val * 0.3)
    scaled = bar_length if value == max_val else bar_length * (value / max_val)
    add_rounded_barh(ax, bar_cfg.get('y', 0.0), scaled, left=x_start, height=bar_cfg.get('height', 0.22), color=bar_cfg.get('color', '#6D28D9'))
    ax.set_xlim(0, max_val * 1.10)
    ax.set_ylim(-0.75, 0.75)
    ax.text(x_start, label_cfg.get('y', 0.34), wrap_text(label, label_cfg.get('wrap', 38)), ha=label_cfg.get('ha', 'left'), va='bottom', fontsize=label_cfg.get('fontsize', 10), fontweight=label_cfg.get('fontweight', 'bold'))
    ax.text(x_start + scaled, bar_cfg.get('y', 0.0), format_value(value, spec), ha=value_cfg.get('ha', 'center'), va=value_cfg.get('va', 'center'), fontsize=value_cfg.get('fontsize', 11), fontweight=value_cfg.get('fontweight', 'bold'))


def render_ranking_bar_exec(ax, spec, template, rows):
    if spec.get('sort_by'):
        reverse = spec.get('sort_order', 'desc').lower() == 'desc'
        rows = sorted(rows, key=lambda r: float(r[spec['sort_by']]), reverse=reverse)
    labels = [wrap_text(str(r[spec['x']]), template['category_label'].get('wrap', 24)) for r in rows]
    values = [float(r[spec['y']]) for r in rows]
    colors = choose_colors(len(values), template['bar'], int(spec.get('highlight_index', 0)))
    ypos = list(range(len(labels)))
    ax.barh(ypos, values, color=colors, edgecolor='none', height=template['bar'].get('height', 0.46))
    round_bar_patches(ax)
    ax.set_yticks(ypos, labels)
    ax.invert_yaxis()
    max_val = max(values) if values else 1
    ax.set_xlim(0, max_val * 1.15)
    value_cfg = template['value_label']
    dx = max(max_val * value_cfg.get('dx_ratio', 0.015), value_cfg.get('min_dx', 0.05))
    for y, v in zip(ypos, values):
        ax.text(v + dx, y, format_value(v, spec), ha=value_cfg.get('ha', 'left'), va=value_cfg.get('va', 'center'), fontsize=value_cfg.get('fontsize', 9.5), fontweight=value_cfg.get('fontweight', 'bold'))


def render_line_exec(ax, spec, template, rows):
    x_key = spec['x']; y_keys = spec['y'] if isinstance(spec['y'], list) else [spec['y']]
    xs = [str(r[x_key])[-5:].replace('-', '/') if len(str(r[x_key])) == 10 else str(r[x_key]) for r in rows]
    line_cfg = template['line']
    colors = choose_colors(len(y_keys), line_cfg, int(spec.get('highlight_index', 0)))
    max_seen = 0
    for idx, y_key in enumerate(y_keys):
        ys = [float(r[y_key]) for r in rows]
        max_seen = max(max_seen, max(ys) if ys else 0)
        ax.plot(xs, ys, color=colors[idx], marker='o', linewidth=line_cfg.get('linewidth', 2.2), markersize=line_cfg.get('markersize', 5), label=y_key)
    if len(xs) > template['labels'].get('tick_rotation_threshold', 8):
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_ylim(bottom=spec.get('y_min', 0), top=max_seen * 1.18 if max_seen else 1)
    if len(y_keys) > 1 or spec.get('show_legend', False):
        ax.legend(loc='upper left', bbox_to_anchor=(0, 1.02), frameon=False, fontsize=9, ncol=min(len(y_keys), 3))


def render_scatter_exec(ax, spec, template, rows):
    x_key, y_key = spec['x'], spec['y']
    xs = [float(r[x_key]) for r in rows]; ys = [float(r[y_key]) for r in rows]
    points_cfg = template['points']
    ax.scatter(xs, ys, s=points_cfg.get('size', spec.get('marker_size', 70)), color=points_cfg.get('color', '#6D28D9'), edgecolors=points_cfg.get('edgecolor', '#FFFFFF'), linewidths=points_cfg.get('linewidth', 0.8), alpha=spec.get('alpha', 0.9))
    ax.set_xlim(left=spec.get('x_min', 0), right=(max(xs) * 1.2 if xs else 1))
    ax.set_ylim(bottom=spec.get('y_min', 0), top=(max(ys) * 1.25 if ys else 1))
    label_key = spec.get('label_key')
    if label_key:
        ranked = sorted(rows, key=lambda r: (float(r[y_key]), float(r[x_key])), reverse=True)
        for i, r in enumerate(ranked[:template['labels'].get('max_labels', 4)]):
            x, y = float(r[x_key]), float(r[y_key])
            dx = max(xs) * 0.02 if xs else 0.1
            dy = (max(ys) * 0.05 if ys else 0.1) * (1 if i % 2 == 0 else -1)
            ax.text(x + dx, y + dy, wrap_text(str(r[label_key]), template['labels'].get('wrap', 20)), fontsize=8, ha='left', va='center')


def render_grouped_bar_exec(ax, spec, template, rows):
    labels = [str(r[spec['x']]) for r in rows]; series = spec['series']; xpos = list(range(len(labels)))
    n = len(series); width = template['bar'].get('group_width', 0.72) / max(n, 1)
    colors = choose_colors(len(series), template['bar'], int(spec.get('highlight_index', 0)))
    max_seen = 0
    for i, s in enumerate(series):
        vals = [float(r[s]) for r in rows]
        max_seen = max(max_seen, max(vals) if vals else 0)
        offset = (i - (n - 1) / 2) * width
        ax.bar([x + offset for x in xpos], vals, width=width * 0.88, color=colors[i], edgecolor='none', label=s)
    round_bar_patches(ax)
    ax.set_xticks(xpos, labels)
    ax.set_ylim(bottom=spec.get('y_min', 0), top=max_seen * 1.15 if max_seen else 1)
    lg = template.get('legend', {})
    ax.legend(loc=lg.get('loc', 'upper left'), bbox_to_anchor=tuple(lg.get('bbox_to_anchor', [0, 1.02])), frameon=False, fontsize=lg.get('fontsize', 9), ncol=min(len(series), 3))


def render_stacked_bar_exec(ax, spec, template, rows):
    labels = [str(r[spec['x']]) for r in rows]; series = spec['series']; xpos = list(range(len(labels)))
    colors = choose_colors(len(series), template['bar'], 0); bottom = [0.0] * len(rows)
    totals = [sum(float(r[s]) for s in series) for r in rows]; normalize = spec.get('normalize', False)
    for i, s in enumerate(series):
        vals = [float(r[s]) for r in rows]
        if normalize:
            vals = [(v / t * 100) if t else 0 for v, t in zip(vals, totals)]
        ax.bar(xpos, vals, bottom=bottom, color=colors[i], edgecolor='none', label=s, width=template['bar'].get('width', 0.56))
        bottom = [b + v for b, v in zip(bottom, vals)]
    round_bar_patches(ax)
    ax.set_xticks(xpos, labels)
    if normalize:
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=100.0))
    lg = template.get('legend', {})
    ax.legend(loc=lg.get('loc', 'upper left'), bbox_to_anchor=tuple(lg.get('bbox_to_anchor', [0, 1.02])), frameon=False, fontsize=lg.get('fontsize', 9), ncol=min(len(series), 3))


def render_histogram_exec(ax, spec, template, rows):
    values = [float(r[spec['x']]) for r in rows]
    ax.hist(values, bins=spec.get('bins', 10), color=template['bar'].get('color', '#6D28D9'), edgecolor='white', rwidth=0.92)
    round_bar_patches(ax, rounding=0.05)


def render_heatmap_exec(ax, spec, template):
    matrix = spec['matrix']; hm = template['heatmap']
    im = ax.imshow(matrix, cmap=hm.get('cmap', spec.get('cmap', 'Purples')), aspect='auto')
    ax.set_xticks(range(len(spec.get('x_labels', []))), spec.get('x_labels', [str(i) for i in range(len(matrix[0]))]))
    ax.set_yticks(range(len(spec.get('y_labels', []))), spec.get('y_labels', [str(i) for i in range(len(matrix))]))
    if hm.get('show_colorbar', True):
        plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)


def render_waterfall_exec(ax, spec, template, rows):
    labels = [wrap_text(str(r[spec['x']]), 16) for r in rows]; values = [float(r[spec['y']]) for r in rows]
    types = spec.get('measure_types', ['relative'] * len(rows)); starts=[]; heights=[]; colors=[]; running=0.0; cfg=template['colors']
    for v, mtype in zip(values, types):
        if mtype == 'total':
            start, height = 0.0, v; running = v; colors.append(cfg.get('total', '#2563EB'))
        else:
            start = running if v >= 0 else running + v; height = abs(v); running += v; colors.append(cfg.get('positive', '#16A34A') if v >= 0 else cfg.get('negative', '#DC2626'))
        starts.append(start); heights.append(height)
    xpos = list(range(len(labels)))
    ax.bar(xpos, heights, bottom=starts, color=colors, edgecolor='none', width=0.56)
    round_bar_patches(ax)
    ax.set_xticks(xpos, labels)
    max_top = max((s + h for s, h in zip(starts, heights)), default=1)
    for x, s, h, raw in zip(xpos, starts, heights, values):
        ax.text(x, s + h + max(max_top * 0.02, 0.1), format_value(raw, spec), ha='center', va='bottom', fontsize=9, fontweight='bold')


def render_slope_exec(ax, spec, template, rows):
    cfg = template['line']; colors = choose_colors(len(rows), cfg, int(spec.get('highlight_index', 0)))
    ax.set_xlim(-0.2, 1.2); ax.set_xticks([0, 1], [spec.get('left_label', 'Before'), spec.get('right_label', 'After')])
    for idx, row in enumerate(rows):
        start = float(row[spec['start_key']]); end = float(row[spec['end_key']]); color = colors[idx]
        ax.plot([0, 1], [start, end], color=color, linewidth=cfg.get('linewidth', 2.0)); ax.scatter([0, 1], [start, end], color=color, s=cfg.get('markersize', 35))
        ax.text(-0.03, start, f"{row[spec['label_key']]}  {format_value(start, spec)}", ha='right', va='center', fontsize=8.5)
        ax.text(1.03, end, f"{format_value(end, spec)}  {row[spec['label_key']]}", ha='left', va='center', fontsize=8.5)


def infer_template_name(spec: Dict[str, Any], rows: List[Dict[str, Any]]) -> str:
    if spec.get('presentation_template'):
        return spec['presentation_template']
    chart_type = spec['chart_type']
    if chart_type == 'bar' and spec.get('orientation') == 'horizontal':
        return 'single_bar_exec' if len(rows) == 1 else 'ranking_bar_exec'
    mapping = {'line': 'line_exec_short','scatter': 'scatter_exec_few','grouped_bar': 'grouped_bar_exec','stacked_bar': 'stacked_bar_exec','histogram': 'histogram_exec','heatmap': 'heatmap_exec','waterfall': 'waterfall_exec','slope': 'slope_exec'}
    if chart_type in mapping:
        return mapping[chart_type]
    raise ValueError('No executive template available for this spec')


def render_exec(spec: Dict[str, Any], out_path: str, template_dir: str):
    spec = validate_or_raise(spec)
    rows = load_data(spec)
    template_name = infer_template_name(spec, rows)
    template = load_json(os.path.join(template_dir, f'{template_name}.json'))
    apply_base_style(template)
    fig_cfg = template['figure']
    fig, ax = plt.subplots(figsize=(fig_cfg['width'], fig_cfg['height']), dpi=fig_cfg['dpi'])
    add_titles(fig, spec, template)
    style_axes(ax, spec, template)

    if template_name == 'single_bar_exec':
        render_single_bar_exec(ax, spec, template, rows)
    elif template_name == 'ranking_bar_exec':
        render_ranking_bar_exec(ax, spec, template, rows)
    elif template_name == 'line_exec_short':
        render_line_exec(ax, spec, template, rows)
    elif template_name == 'scatter_exec_few':
        render_scatter_exec(ax, spec, template, rows)
    elif template_name == 'grouped_bar_exec':
        render_grouped_bar_exec(ax, spec, template, rows)
    elif template_name == 'stacked_bar_exec':
        render_stacked_bar_exec(ax, spec, template, rows)
    elif template_name == 'histogram_exec':
        render_histogram_exec(ax, spec, template, rows)
    elif template_name == 'heatmap_exec':
        render_heatmap_exec(ax, spec, template)
    elif template_name == 'waterfall_exec':
        render_waterfall_exec(ax, spec, template, rows)
    elif template_name == 'slope_exec':
        render_slope_exec(ax, spec, template, rows)
    else:
        raise ValueError(f'Unsupported exec template: {template_name}')

    plot = template['plot']
    fig.subplots_adjust(left=plot['left'], right=plot['right'], top=plot['top'], bottom=plot['bottom'])
    fig.savefig(out_path)
    plt.close(fig)
