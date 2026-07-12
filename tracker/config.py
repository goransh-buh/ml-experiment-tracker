"""
Configuration defaults for the tracker.
"""

from dataclasses import dataclass


@dataclass
class TrackerConfig:
    log_dir: str = "./runs"
    auto_flush: bool = True
    max_runs_kept: int = 100  # oldest runs pruned beyond this

    @classmethod
    def default(cls) -> "TrackerConfig":
        return cls()
