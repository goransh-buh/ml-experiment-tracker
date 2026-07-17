"""
Core Run class — represents a single experiment run.
"""

import json
import time
import uuid
from pathlib import Path
from typing import Any, Dict, Optional


class Run:
    """A single experiment run that logs metrics and parameters to disk."""

    def __init__(self, name: str, log_dir: str = "./runs"):
        self.name = name
        self.run_id = str(uuid.uuid4())[:8]
        self.log_dir = Path(log_dir) / f"{name}_{self.run_id}"
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.metrics: Dict[str, list] = {}
        self.params: Dict[str, Any] = {}
        self.start_time = time.time()

    def log_param(self, key: str, value: Any) -> None:
        """Log a hyperparameter for this run."""
        self.params[key] = value
        self._flush_params()

    def log_metric(self, key: str, value: float, step: Optional[int] = None) -> None:
        """Log a metric value, optionally at a specific step."""
        if key not in self.metrics:
            self.metrics[key] = []
        entry = {"value": value, "step": step, "timestamp": time.time()}
        self.metrics[key].append(entry)
        self._flush_metrics()

    def _flush_params(self) -> None:
        with open(self.log_dir / "params.json", "w") as f:
            json.dump(self.params, f, indent=2)

    def _flush_metrics(self) -> None:
        with open(self.log_dir / "metrics.json", "w") as f:
            json.dump(self.metrics, f, indent=2)

    def finish(self) -> None:
        """Mark the run as complete and write summary."""
        duration = time.time() - self.start_time
        summary = {
            "run_id": self.run_id,
            "name": self.name,
            "duration_seconds": duration,
            "params": self.params,
            "final_metrics": {k: v[-1]["value"] if v else None for k, v in self.metrics.items()},
        }
        with open(self.log_dir / "summary.json", "w") as f:
            json.dump(summary, f, indent=2)
