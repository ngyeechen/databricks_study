from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import seaborn as sns

spark = SparkSession.builder.getOrCreate()

sns.set_theme(style="whitegrid")

##avg sale price by year
df = spark.table("gold_sales_by_year").toPandas()

plt.figure(figsize=(10,5))

sns.lineplot(
    data=df,
    x="year",
    y="avg_sale_price",
    marker="o"
)

plt.title("Average Sale Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Sale Price")

plt.tight_layout()
plt.show()


##sale by property type
df = spark.table("gold_sales_by_year").toPandas()

plt.figure(figsize=(10,5))

sns.lineplot(
    data=df,
    x="year",
    y="avg_sale_price",
    marker="o"
)

plt.title("Average Sale Price by Year")
plt.xlabel("Year")
plt.ylabel("Average Sale Price")

plt.tight_layout()
plt.show()


##avg sale price by number of rooms
df = spark.table("gold_price_by_rooms").toPandas()

plt.figure(figsize=(8,5))

sns.lineplot(
    data=df,
    x="num_rooms",
    y="avg_sale_price",
    marker="o"
)

plt.title("Average Sale Price by Number of Rooms")

plt.tight_layout()
plt.show()


##top 10 localities
df = (
    spark.table("gold_sales_by_locality")
    .orderBy("total_sales", ascending=False)
    .limit(10)
    .toPandas()
)

plt.figure(figsize=(10,6))

sns.barplot(
    data=df,
    x="total_sales",
    y="Locality"
)

plt.title("Top 10 Localities by Number of Sales")

plt.tight_layout()
plt.show()