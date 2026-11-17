"""Unit tests: one function, invented rows, one assertion. No tables."""
import pytest

from src.sales import add_gross, remove_cancelled


@pytest.fixture
def sales(spark):
    """Three invented sales: we know the right answers, and nothing is sensitive."""
    return spark.createDataFrame(
        [(1, 100.0, "PAID"), (2, 20.0, " cancelled "), (3, 10.0, "Cancelled")],
        "sale_id INT, net DOUBLE, status STRING",
    )


def test_remove_cancelled_ignores_case_and_spaces(sales):
    assert [row.sale_id for row in remove_cancelled(sales).collect()] == [1]


def test_add_gross_adds_vat(sales):
    assert add_gross(sales).where("sale_id = 1").first().gross == 125.5


def test_add_gross_keeps_every_row(sales):
    assert add_gross(sales).count() == 3
