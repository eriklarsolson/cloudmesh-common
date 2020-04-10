###############################################################
# pytest -v --capture=no tests/test_stopwatch.py
# pytest -v --capture=no tests/test_stopwatch..py::Test_stopwatch.test_001
# pytest -v  tests/test_stopwatch.py
###############################################################

import time

import pytest
from cloudmesh.common.Benchmark import Benchmark

from cloudmesh.common.util import HEADING


@pytest.mark.incremental
class Test_Printer:

    def test_benchmark_stopwatch_1(self):
        HEADING()
        Benchmark.Start()
        time.sleep(0.1)
        Benchmark.Stop()
        assert True

    def test_benchmark_stopwatch_2(self):
        HEADING()
        Benchmark.Start()
        time.sleep(0.1)
        Benchmark.Stop()

        Benchmark.print(sysinfo=True, csv=True)
        assert True
