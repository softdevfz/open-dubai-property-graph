#!/usr/bin/env python3
"""Download the latest Open Dubai Property Graph from fairsqft.com/data/.

Usage: python3 download.py [--format parquet|csv|jsonl] [--out DIR]
Standard library only. The full files live on fairsqft.com; this repository only holds a 100-row sample.
"""
import argparse, json, pathlib, urllib.request

BASE = 'https://fairsqft.com/data/open/'
UA = {'User-Agent': 'open-dubai-property-graph-download'}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--format', default='parquet', choices=['parquet', 'csv', 'jsonl'])
    ap.add_argument('--out', default='data')
    a = ap.parse_args()
    latest = json.loads(get(BASE + 'latest.json'))
    as_of = latest['as_of']
    out = pathlib.Path(a.out) / as_of
    out.mkdir(parents=True, exist_ok=True)
    for name in ('archetypes.' + a.format, 'crosswalk.' + a.format, 'datapackage.json'):
        (out / name).write_bytes(get(f'{BASE}{as_of}/{name}'))
        print('saved', out / name)


if __name__ == '__main__':
    main()
