# ML Experiment Tracker

A lightweight, dependency-minimal library for tracking machine learning
experiments — metrics, hyperparameters, and artifacts — with zero setup
required (no external servers, just local files).

## Why this exists

Most experiment tracking tools (MLflow, Weights & Biases) require running
a server or signing up for a SaaS product. This is a minimal alternative
for quick local experimentation: log metrics with one line, compare runs
with one function call.

## Installation

```bash
git clone <this-repo>
cd ml-experiment-tracker
pip install -r requirements.txt
```

## Quick start

```python
from tracker.run import Run

run = Run("my_experiment")
run.log_param("learning_rate", 0.01)
run.log_metric("accuracy", 0.92)
run.finish()
```

## Comparing runs

```python
from tracker.compare import compare_runs, best_run

all_runs = compare_runs("./runs")
top_run = best_run("./runs", metric="accuracy", mode="max")
```

## CLI

```bash
python -m tracker.cli list
python -m tracker.cli best --metric accuracy
```

## Exporting results

```python
from tracker.export import export_to_csv
export_to_csv("./runs", "results.csv")
```

## Features

- ✅ Zero-config local experiment logging
- ✅ Hyperparameter + metric tracking
- ✅ Run comparison and best-run selection
- ✅ CSV export for external analysis
- ✅ Simple matplotlib visualization
- ✅ CLI for quick browsing

## Running tests

```bash
python -m pytest tests/
```

## License

MIT
