"""
Export run comparisons to CSV for external analysis (Excel, pandas, etc).
"""

import csv
from pathlib import Path
from typing import List

from tracker.compare import compare_runs


def export_to_csv(log_dir: str = "./runs", output_path: str = "runs_export.csv") -> None:
    """Export all run summaries to a flat CSV file."""
    runs = compare_runs(log_dir)
    if not runs:
        print("No runs found to export.")
        return

    # Collect all unique metric names across runs
    all_metrics = set()
    for r in runs:
        all_metrics.update(r.get("final_metrics", {}).keys())

    fieldnames = ["run_id", "name", "duration_seconds"] + sorted(all_metrics)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in runs:
            row = {
                "run_id": r["run_id"],
                "name": r["name"],
                "duration_seconds": round(r.get("duration_seconds", 0), 2),
            }
            row.update(r.get("final_metrics", {}))
            writer.writerow(row)

    print(f"Exported {len(runs)} runs to {output_path}")
