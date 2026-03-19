#!/usr/bin/env python3
import argparse
import os
from render_core import load_json, render_exec


def main():
    parser = argparse.ArgumentParser(description='Compatibility wrapper: render executive charts through the single render core.')
    parser.add_argument('--spec', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--template-dir', default=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates'))
    args = parser.parse_args()

    spec = load_json(args.spec)
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    render_exec(spec, args.output, args.template_dir)


if __name__ == '__main__':
    main()
