# Databricks notebook source

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp

spark = SparkSession.builder.getOrCreate()

mount_point = dbutils.widgets.get("mount_point")
file_name = dbutils.widgets.get("file_name")

# Sample data to add
data = [("Mark", 25), ("Sameh", 30), ("Norhan", 35), ("Ahmed", 25)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Add a timestamp to the new records
df = df.withColumn("Timestamp", current_timestamp())

file_path = f"{mount_point}/{file_name}"

# Read existing data if it exists
if dbutils.fs.ls(file_path):
    existing_df = spark.read.csv(file_path, header=True, inferSchema=True)
    
    # Optionally filter out records that already exist (based on unique columns like Name, Age)
    # In this case, assuming "Name" and "Age" are unique and Timestamp is for new data
    existing_names = [row["Name"] for row in existing_df.select("Name").distinct().collect()]
    df = df.filter(~df.Name.isin(existing_names))

# Write the new, non-duplicate data
df.write.csv(file_path, header=True, mode="append")

print(f"File written/updated at: {file_path}")
