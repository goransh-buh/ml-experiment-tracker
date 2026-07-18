"""
Utilities for comparing multiple experiment runs.
"""

import json
from pathlib import Path
from typing import Dict, List


def load_run_summary(run_dir: Path) -> Dict:
    """Load the summary.json for a completed run."""
    summary_path = run_dir / "summary.json"
    if not summary_path.exists():
        return {}
    with open(summary_path) as f:
        return json.load(f)


def compare_runs(log_dir: str = "./runs") -> List[Dict]:
    """Return summaries for all runs in log_dir, sorted by start time."""
    base = Path(log_dir)
    if not base.exists():
        return []

    summaries = []
    for run_dir in sorted(base.iterdir()):
        if run_dir.is_dir():
            summary = load_run_summary(run_dir)
            if summary:
                summaries.append(summary)
    return summaries


def best_run(log_dir: str, metric: str, mode: str = "max") -> Dict:
    """Find the best run according to a given metric."""
    runs = compare_runs(log_dir)
    valid_runs = [r for r in runs if r.get("final_metrics", {}).get(metric) is not None]
    if not valid_runs:
        return {}

    key_fn = lambda r: r["final_metrics"][metric]
    return max(valid_runs, key=key_fn) if mode == "max" else min(valid_runs, key=key_fn)
