#!/usr/bin/env python3
import argparse
import csv
import json
import os
from typing import Dict, List

from chart_schema import fill_defaults, SUPPORTED_TYPES


def read_headers(csv_path: str) -> List[str]:
    with open(csv_path, 'r', encoding='utf-8-sig', newline='') as f:
        reader = csv.reader(f)
        return next(reader)


def build_spec(chart_type: str, headers: List[str]) -> Dict:
    first = headers[0] if headers else 'x'
    second = headers[1] if len(headers) > 1 else 'y'
    third = headers[2] if len(headers) > 2 else 'z'

    if chart_type == 'bar':
        spec = {
            'chart_type': 'bar',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': second,
            'x': first,
            'y': second,
            'sort_by': second,
        }
    elif chart_type == 'grouped_bar':
        spec = {
            'chart_type': 'grouped_bar',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': 'Value',
            'x': first,
            'series': headers[1:] if len(headers) > 1 else [second],
        }
    elif chart_type == 'stacked_bar':
        spec = {
            'chart_type': 'stacked_bar',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': 'Value',
            'x': first,
            'series': headers[1:] if len(headers) > 1 else [second],
            'normalize': False,
        }
    elif chart_type == 'line':
        spec = {
            'chart_type': 'line',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': second,
            'x': first,
            'y': second,
        }
    elif chart_type == 'scatter':
        spec = {
            'chart_type': 'scatter',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': second,
            'x': first,
            'y': second,
            'label_key': '',
        }
    elif chart_type == 'histogram':
        spec = {
            'chart_type': 'histogram',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': 'Frequency',
            'x': first,
        }
    elif chart_type == 'waterfall':
        spec = {
            'chart_type': 'waterfall',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': first,
            'y_label': second,
            'x': first,
            'y': second,
            'measure_types': ['relative'] * max(0, len(headers)),
        }
    elif chart_type == 'slope':
        spec = {
            'chart_type': 'slope',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'label_key': first,
            'start_key': second,
            'end_key': third,
            'left_label': second,
            'right_label': third,
        }
    elif chart_type == 'heatmap':
        spec = {
            'chart_type': 'heatmap',
            'title': 'Replace with takeaway title',
            'subtitle': '',
            'x_label': 'Columns',
            'y_label': 'Rows',
            'x_labels': ['Col 1', 'Col 2'],
            'y_labels': ['Row 1', 'Row 2'],
            'matrix': [[0, 1], [1, 0]],
        }
    else:
        raise ValueError(f'unsupported chart_type: {chart_type}')

    return fill_defaults(spec)


def main():
    parser = argparse.ArgumentParser(description='Generate a validated chart spec template from CSV headers.')
    parser.add_argument('--csv', help='Input CSV path (optional for heatmap templates)')
    parser.add_argument('--chart-type', choices=sorted(SUPPORTED_TYPES), required=True)
    parser.add_argument('--output', required=True, help='Output JSON spec path')
    args = parser.parse_args()

    headers: List[str] = []
    if args.csv:
        headers = read_headers(args.csv)
    spec = build_spec(args.chart_type, headers)
    if args.csv and args.chart_type != 'heatmap':
        spec['data_path'] = args.csv

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(spec, f, ensure_ascii=False, indent=2)
        f.write('\n')


if __name__ == '__main__':
    main()
