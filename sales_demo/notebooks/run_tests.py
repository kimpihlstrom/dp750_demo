# Databricks notebook source
# MAGIC %pip install -q pytest

# COMMAND ----------

# First task of sales_job: the unit tests. A failing test fails this task, so load_sales never runs.
import os
import sys

import pytest

sys.dont_write_bytecode = True
retcode = pytest.main([os.path.abspath("../tests/unit"), "-v", "-p", "no:cacheprovider"])
assert retcode == 0, "Unit tests failed: nothing was loaded."
