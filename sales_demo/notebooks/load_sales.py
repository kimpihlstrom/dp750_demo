# Databricks notebook source
# Second task of sales_job: runs only after the unit tests passed.
# catalog and schema arrive as widgets, from base_parameters in resources/sales_job.yml.
import os
import sys

sys.path.append(os.path.abspath(".."))   # the bundle root, so that src/ can be imported
from src.sales import add_gross, remove_cancelled

dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")
schema = f"`{dbutils.widgets.get('catalog')}`.`{dbutils.widgets.get('schema')}`"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {schema}")
sales = spark.createDataFrame(
    [(1, 100.0, "PAID"), (2, 250.0, "paid"), (3, 80.0, " Cancelled ")],
    "sale_id INT, net DOUBLE, status STRING",
)
add_gross(remove_cancelled(sales)).write.mode("overwrite").saveAsTable(f"{schema}.sales_gross")
print(f"Wrote {schema}.sales_gross")
