"""
Simple visualization utilities for logged metrics.
"""

from pathlib import Path
from typing import Optional

from tracker.run import Run


def plot_metric(run: Run, metric_name: str, save_path: Optional[str] = None):
    """Plot a single metric's value over logged steps."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed. Run: pip install matplotlib")
        return

    if metric_name not in run.metrics:
        print(f"No data logged for metric '{metric_name}'")
        return

    entries = run.metrics[metric_name]
    steps = [e.get("step", i) for i, e in enumerate(entries)]
    values = [e["value"] for e in entries]

    plt.figure(figsize=(8, 5))
    plt.plot(steps, values, marker="o")
    plt.xlabel("Step")
    plt.ylabel(metric_name)
    plt.title(f"{run.name} — {metric_name}")
    plt.grid(True, alpha=0.3)

    if save_path:
        plt.savefig(save_path)
        print(f"Saved plot to {save_path}")
    else:
        plt.show()
