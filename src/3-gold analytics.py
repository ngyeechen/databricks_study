from pyspark.sql import SparkSession


def run():

    spark = SparkSession.builder.getOrCreate()

    silver_df = spark.table("property_transactions_silver")

    silver_df.createOrReplaceTempView("silver")

    spark.sql("""
    CREATE OR REPLACE TABLE gold_sales_by_property AS
    SELECT
        Property,
        COUNT(*) AS total_sales,
        AVG(Sale_Price) AS avg_sale_price,
        AVG(carpet_area) AS avg_carpet_area
    FROM silver
    GROUP BY Property
    """)

    spark.sql("""
    CREATE OR REPLACE TABLE gold_sales_by_year AS
    SELECT
        YEAR(Date) AS year,
        COUNT(*) AS total_sales,
        AVG(Sale_Price) AS avg_sale_price
    FROM silver
    GROUP BY YEAR(Date)
    ORDER BY year
    """)

    spark.sql("""
    CREATE OR REPLACE TABLE gold_sales_by_locality AS
    SELECT
        Locality,
        COUNT(*) AS total_sales,
        AVG(Sale_Price) AS avg_sale_price,
        AVG(Estimated_Value) AS avg_estimated_value
    FROM silver
    WHERE Locality IS NOT NULL
    GROUP BY Locality
    """)

    spark.sql("""
    CREATE OR REPLACE TABLE gold_price_by_rooms AS
    SELECT
        num_rooms,
        COUNT(*) AS total_sales,
        AVG(Sale_Price) AS avg_sale_price
    FROM silver
    GROUP BY num_rooms
    ORDER BY num_rooms
    """)

    print("Gold tables created successfully.")


if __name__ == "__main__":
    run()