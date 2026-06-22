from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalesDataFrameProject") \
    .getOrCreate()

# Read CSV File
df = spark.read.csv(
    "sales.csv",
    header=True,
    inferSchema=True
)

print("\nOriginal Data")
df.show()

# Sort by Sales Descending
print("\nProducts Sorted By Sales")
sorted_df = df.orderBy(col("sales").desc())
sorted_df.show()

# Top 3 Products
print("\nTop 3 Products")
top3_df = sorted_df.limit(3)
top3_df.show()

# Sales Greater Than 80000
print("\nProducts With Sales > 80000")
high_sales_df = df.filter(col("sales") > 80000)
high_sales_df.show()

# Save Output
high_sales_df.coalesce(1).write \
    .mode("overwrite") \
    .option("header", "true") \
    .csv("output/high_sales_products")

spark.stop()