from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    trim,
    to_date
)


def run():

    spark = SparkSession.builder.getOrCreate()

    silver_df = spark.table("property_transactions_bronze")

    silver_df = (
        silver_df
        .withColumn("Date", to_date(col("Date")))
        .withColumn("Estimated_Value", col("Estimated_Value").cast("double"))
        .withColumn("Sale_Price", col("Sale_Price").cast("double"))
        .withColumn("num_rooms", col("num_rooms").cast("double"))
        .withColumn("num_bathrooms", col("num_bathrooms").cast("double"))
        .withColumn("carpet_area", col("carpet_area").cast("double"))
        .withColumn("property_tax_rate", col("property_tax_rate").cast("double"))
        .withColumn("Locality", trim(col("Locality")))
        .withColumn("Property", trim(col("Property")))
        .withColumn("Residential", trim(col("Residential")))
        .withColumn("Face", trim(col("Face")))
    )

    silver_df.write \
        .mode("overwrite") \
        .saveAsTable("property_transactions_silver")

    print("Silver table created successfully.")


if __name__ == "__main__":
    run()