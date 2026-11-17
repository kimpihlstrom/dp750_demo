"""Business logic of the sales job: plain PySpark, no tables, no widgets, so it is easy to test."""
from pyspark.sql import DataFrame, functions as F

VAT_RATE = 0.255
CANCELLED_STATUSES = ["CANCELLED", "REFUNDED", "REJECTED"]


def remove_cancelled(df: DataFrame) -> DataFrame:
    """Removes cancelled sales. Ignores case and spaces: ' Cancelled ' counts too."""
    return df.where(~F.upper(F.trim("status")).isin(CANCELLED_STATUSES))


def add_gross(df: DataFrame, rate: float = VAT_RATE) -> DataFrame:
    """Adds the column gross: net plus VAT, rounded to cents."""
    return df.withColumn("gross", F.round(F.col("net") * (1 + rate), 2))
