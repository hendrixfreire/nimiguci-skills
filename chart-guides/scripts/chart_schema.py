#!/usr/bin/env python3
from __future__ import annotations

from typing import Any, Dict, List, Set

SUPPORTED_TYPES: Set[str] = {
    'bar', 'grouped_bar', 'stacked_bar', 'line', 'scatter', 'histogram', 'heatmap', 'waterfall', 'slope'
}

BASE_REQUIRED = {'chart_type', 'title'}
SUPPORTED_PRESENTATION_TEMPLATES: Set[str] = {
    'single_bar_exec', 'ranking_bar_exec', 'line_exec_short', 'scatter_exec_few',
    'grouped_bar_exec', 'stacked_bar_exec', 'histogram_exec', 'heatmap_exec',
    'waterfall_exec', 'slope_exec'
}
STYLE_DEFAULTS = {
    'width': 13.33,
    'height': 7.5,
    'dpi': 150,
    'font_family': 'DejaVu Sans',
    'title_size': 14,
    'axis_size': 10,
    'tick_size': 8,
    'grid': False,
}

TYPE_DEFAULTS: Dict[str, Dict[str, Any]] = {
    'bar': {
        'orientation': 'vertical',
        'show_values': True,
        'highlight_index': 0,
        'sort_order': 'desc',
        'value_format': 'number',
        'value_decimals': 0,
        'x_tick_rotation': 0,
        'y_min': 0,
    },
    'grouped_bar': {
        'orientation': 'vertical',
        'show_values': False,
        'highlight_index': 0,
        'value_format': 'number',
        'value_decimals': 0,
        'x_tick_rotation': 0,
        'y_min': 0,
        'show_legend': True,
        'legend_loc': 'upper right',
    },
    'stacked_bar': {
        'orientation': 'vertical',
        'show_values': False,
        'value_format': 'number',
        'value_decimals': 0,
        'x_tick_rotation': 0,
        'y_min': 0,
        'show_legend': True,
        'legend_loc': 'upper right',
        'normalize': False,
    },
    'line': {
        'show_values': False,
        'show_legend': False,
        'label_mode': 'final',
        'highlight_index': 0,
        'value_format': 'number',
        'value_decimals': 0,
    },
    'scatter': {
        'label_key': '',
        'marker_size': 50,
        'alpha': 0.85,
        'value_format': 'number',
        'value_decimals': 0,
    },
    'histogram': {
        'bins': 10,
        'show_values': False,
        'value_format': 'number',
        'value_decimals': 0,
    },
    'heatmap': {
        'show_values': False,
        'cmap': 'Purples',
        'value_format': 'number',
        'value_decimals': 0,
    },
    'waterfall': {
        'show_values': True,
        'value_format': 'number',
        'value_decimals': 0,
        'y_min': 0,
    },
    'slope': {
        'show_values': True,
        'highlight_index': 0,
        'value_format': 'number',
        'value_decimals': 0,
        'left_label': 'Before',
        'right_label': 'After',
    },
}

TYPE_REQUIRED: Dict[str, Set[str]] = {
    'bar': {'x', 'y'},
    'grouped_bar': {'x', 'series'},
    'stacked_bar': {'x', 'series'},
    'line': {'x', 'y'},
    'scatter': {'x', 'y'},
    'histogram': {'x'},
    'heatmap': {'matrix'},
    'waterfall': {'x', 'y'},
    'slope': {'label_key', 'start_key', 'end_key'},
}


def fill_defaults(spec: Dict[str, Any]) -> Dict[str, Any]:
    normalized = dict(spec)
    style = dict(STYLE_DEFAULTS)
    style.update(normalized.get('style', {}))
    normalized['style'] = style
    chart_type = normalized.get('chart_type')
    if chart_type in TYPE_DEFAULTS:
        merged = dict(TYPE_DEFAULTS[chart_type])
        merged.update(normalized)
        merged['style'] = style
        normalized = merged
    return normalized


def validate_spec(spec: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    chart_type = spec.get('chart_type')

    for field in BASE_REQUIRED:
        if field not in spec or spec.get(field) in (None, ''):
            errors.append(f'missing required field: {field}')

    if chart_type not in SUPPORTED_TYPES:
        errors.append(f'unsupported chart_type: {chart_type}')
        return errors

    required = TYPE_REQUIRED[chart_type]
    for field in required:
        if field not in spec or spec.get(field) in (None, '', []):
            errors.append(f'missing required field for {chart_type}: {field}')

    if 'data_path' not in spec and 'data' not in spec and chart_type != 'heatmap':
        errors.append('spec must contain either data_path or data for non-heatmap charts')

    if chart_type == 'bar':
        _validate_bar(spec, errors)
    elif chart_type in {'grouped_bar', 'stacked_bar'}:
        _validate_series_chart(spec, errors)
    elif chart_type == 'line':
        _validate_line(spec, errors)
    elif chart_type == 'scatter':
        _validate_scatter(spec, errors)
    elif chart_type == 'histogram':
        _validate_histogram(spec, errors)
    elif chart_type == 'heatmap':
        _validate_heatmap(spec, errors)
    elif chart_type == 'waterfall':
        _validate_waterfall(spec, errors)
    elif chart_type == 'slope':
        _validate_slope(spec, errors)

    tmpl = spec.get('presentation_template')
    if tmpl is not None and tmpl not in SUPPORTED_PRESENTATION_TEMPLATES:
        errors.append(f'unsupported presentation_template: {tmpl}')

    return errors


def _validate_bar(spec: Dict[str, Any], errors: List[str]) -> None:
    if spec.get('orientation') not in {'vertical', 'horizontal'}:
        errors.append('bar orientation must be vertical or horizontal')


def _validate_series_chart(spec: Dict[str, Any], errors: List[str]) -> None:
    if spec.get('orientation') not in {'vertical', 'horizontal'}:
        errors.append(f"{spec['chart_type']} orientation must be vertical or horizontal")
    series = spec.get('series')
    if not isinstance(series, list) or len(series) == 0:
        errors.append(f"{spec['chart_type']} requires non-empty series list")
    if spec['chart_type'] == 'stacked_bar' and spec.get('normalize') not in {True, False}:
        errors.append('stacked_bar normalize must be boolean')


def _validate_line(spec: Dict[str, Any], errors: List[str]) -> None:
    y = spec.get('y')
    if not isinstance(y, (str, list)):
        errors.append('line y must be string or list of strings')


def _validate_scatter(spec: Dict[str, Any], errors: List[str]) -> None:
    alpha = spec.get('alpha')
    if alpha is not None and not (0 < float(alpha) <= 1):
        errors.append('scatter alpha must be between 0 and 1')


def _validate_histogram(spec: Dict[str, Any], errors: List[str]) -> None:
    bins = spec.get('bins')
    if not isinstance(bins, int) or bins <= 0:
        errors.append('histogram bins must be a positive integer')


def _validate_heatmap(spec: Dict[str, Any], errors: List[str]) -> None:
    matrix = spec.get('matrix')
    if not isinstance(matrix, list) or len(matrix) == 0:
        errors.append('heatmap matrix must be a non-empty 2D list')
        return
    row_lengths = {len(row) for row in matrix if isinstance(row, list)}
    if len(row_lengths) != 1:
        errors.append('heatmap matrix rows must all have the same length')
    if 'x_labels' in spec and len(spec['x_labels']) != len(matrix[0]):
        errors.append('heatmap x_labels length must match matrix column count')
    if 'y_labels' in spec and len(spec['y_labels']) != len(matrix):
        errors.append('heatmap y_labels length must match matrix row count')


def _validate_waterfall(spec: Dict[str, Any], errors: List[str]) -> None:
    types = spec.get('measure_types')
    if types is not None and len(types) != 0:
        if 'data' in spec and len(types) != len(spec['data']):
            errors.append('waterfall measure_types length must match inline data length')


def _validate_slope(spec: Dict[str, Any], errors: List[str]) -> None:
    if spec.get('left_label') in (None, '') or spec.get('right_label') in (None, ''):
        errors.append('slope left_label and right_label are required')


def validate_or_raise(spec: Dict[str, Any]) -> Dict[str, Any]:
    normalized = fill_defaults(spec)
    errors = validate_spec(normalized)
    if errors:
        raise ValueError('invalid chart spec:\n- ' + '\n- '.join(errors))
    return normalized
