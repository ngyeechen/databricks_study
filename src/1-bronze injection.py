##cant run locally, run in databricks because this needs sparks session
from pyspark.sql import SparkSession


def run():

    spark = SparkSession.builder.getOrCreate()

    csv_path = "/Volumes/workspace/github/realestatedata/Real Estate Property Transactions.csv"

    bronze_df = (
        spark.read
            .option("header", "true")
            .option("inferSchema", "true")
            .csv(csv_path)
    )

    # Replace spaces in column names
    bronze_df = bronze_df.toDF(
        *[c.replace(" ", "_") for c in bronze_df.columns]
    )

    bronze_df.write \
        .mode("overwrite") \
        .saveAsTable("property_transactions_bronze")

    print("Bronze table created successfully.")


if __name__ == "__main__":
    run()