from pyspark.sql import SparkSession

# create spark session
spark = SparkSession.builder \
.appName("partitiondemo") \
.getOrCreate()

#create dataframe with 5 million records
df = spark.range(5000000)

#display initial partitions
print("\n Initial Number of Partions: ")
print(df.rdd.getNumPartitions())

# repartition to 12 partitions
df_repartition = df.repartition(12)

print("\nPartitions after repartitioning(12):")
print(df_repartition.rdd.getNumPartitions())

# coalesce to 3 partitons
df_coalesced = df_repartition.coalesce(3)

print("\nPartitions after Coalesce(3):")
print(df_coalesced.rdd.getNumPartitions())

# display sample records
print("\nSample records:")
df_coalesced.show(10)

spark.stop()