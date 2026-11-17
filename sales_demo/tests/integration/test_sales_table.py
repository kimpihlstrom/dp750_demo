"""Integration test: real Spark and a real table in a dedicated test schema. Never production."""
import os

import pytest

from src.sales import add_gross, remove_cancelled


def test_pipeline_on_test_table(spark):
    table = os.environ.get("TEST_TABLE")
    if not table:
        pytest.skip("Set TEST_TABLE to a table in a test schema.")
    result = add_gross(remove_cancelled(spark.read.table(table)))
    assert result.columns == ["sale_id", "net", "status", "gross"]
    assert result.count() == 3   # 5 sample rows, 2 cancelled
