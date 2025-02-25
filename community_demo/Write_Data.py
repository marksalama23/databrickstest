# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, current_timestamp
import random

spark = SparkSession.builder.getOrCreate()

mount_point = dbutils.widgets.get("mount_point")
file_name = dbutils.widgets.get("file_name")

# Generate random data
random_names = ["Alice", "Bob", "Charlie"]
random_data = [(random.choice(random_names), random.randint(20, 50)) for _ in range(5)]  # 5 random records
columns = ["Name", "Age"]
df = spark.createDataFrame(random_data, columns)

# Add a timestamp column
df = df.withColumn("Timestamp", current_timestamp())

file_path = f"{mount_point}/{file_name}"

# Remove NULL timestamps before writing
df = df.filter(col("Timestamp").isNotNull())

# Overwrite the file with new random records
df.write.csv(file_path, header=True, mode="overwrite")

print(f"File overwritten at: {file_path}")
