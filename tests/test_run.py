"""Unit tests for tracker.run.Run"""

import shutil
import tempfile
import unittest
from pathlib import Path

from tracker.run import Run


class TestRun(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_log_param(self):
        run = Run("test_experiment", log_dir=self.tmp_dir)
        run.log_param("learning_rate", 0.01)
        self.assertEqual(run.params["learning_rate"], 0.01)

    def test_log_metric(self):
        run = Run("test_experiment", log_dir=self.tmp_dir)
        run.log_metric("accuracy", 0.95, step=1)
        self.assertEqual(len(run.metrics["accuracy"]), 1)
        self.assertEqual(run.metrics["accuracy"][0]["value"], 0.95)

    def test_finish_writes_summary(self):
        run = Run("test_experiment", log_dir=self.tmp_dir)
        run.log_metric("loss", 0.1)
        run.finish()
        summary_path = run.log_dir / "summary.json"
        self.assertTrue(summary_path.exists())


if __name__ == "__main__":
    unittest.main()
