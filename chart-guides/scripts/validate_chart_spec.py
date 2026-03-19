#!/usr/bin/env python3
import argparse
import json
import sys

from chart_schema import validate_or_raise


def main():
    parser = argparse.ArgumentParser(description='Validate a chart spec JSON against the chart-guides schema.')
    parser.add_argument('--spec', required=True, help='Path to JSON spec')
    args = parser.parse_args()

    with open(args.spec, 'r', encoding='utf-8') as f:
        spec = json.load(f)

    try:
        normalized = validate_or_raise(spec)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        raise SystemExit(1)

    print(json.dumps(normalized, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
