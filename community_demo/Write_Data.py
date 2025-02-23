# Databricks notebook source

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
mount_point = dbutils.widgets.get("mount_point")
file_name = dbutils.widgets.get("file_name")

data = [("Mark", 25), ("Sameh", 30), ("Norhan", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

file_path = f"{mount_point}/{file_name}"
df.write.csv(file_path, header=True)

print(f"File written to: {file_path}")
