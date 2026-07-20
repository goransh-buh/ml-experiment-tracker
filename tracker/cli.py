"""
Command-line interface for browsing experiment runs.

Usage:
    python -m tracker.cli list
    python -m tracker.cli best --metric accuracy
"""

import argparse
from tracker.compare import compare_runs, best_run


def main():
    parser = argparse.ArgumentParser(description="Browse ML experiment runs")
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List all runs")
    list_parser.add_argument("--log-dir", default="./runs")

    best_parser = subparsers.add_parser("best", help="Show the best run by metric")
    best_parser.add_argument("--metric", required=True)
    best_parser.add_argument("--mode", default="max", choices=["max", "min"])
    best_parser.add_argument("--log-dir", default="./runs")

    args = parser.parse_args()

    if args.command == "list":
        runs = compare_runs(args.log_dir)
        for r in runs:
            print(f"{r['run_id']}: {r['name']} — {r.get('final_metrics', {})}")
    elif args.command == "best":
        run = best_run(args.log_dir, args.metric, args.mode)
        print(run if run else "No runs found.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
