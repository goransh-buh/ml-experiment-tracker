"""Unit tests for tracker.compare"""

import shutil
import tempfile
import unittest

from tracker.run import Run
from tracker.compare import compare_runs, best_run


class TestCompare(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir, ignore_errors=True)

    def test_compare_empty(self):
        self.assertEqual(compare_runs(self.tmp_dir), [])

    def test_compare_with_runs(self):
        run1 = Run("exp1", log_dir=self.tmp_dir)
        run1.log_metric("accuracy", 0.8)
        run1.finish()

        run2 = Run("exp2", log_dir=self.tmp_dir)
        run2.log_metric("accuracy", 0.9)
        run2.finish()

        runs = compare_runs(self.tmp_dir)
        self.assertEqual(len(runs), 2)

    def test_best_run(self):
        run1 = Run("exp1", log_dir=self.tmp_dir)
        run1.log_metric("accuracy", 0.8)
        run1.finish()

        run2 = Run("exp2", log_dir=self.tmp_dir)
        run2.log_metric("accuracy", 0.95)
        run2.finish()

        best = best_run(self.tmp_dir, "accuracy", mode="max")
        self.assertEqual(best["name"], "exp2")


if __name__ == "__main__":
    unittest.main()
