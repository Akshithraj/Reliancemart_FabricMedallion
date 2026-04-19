# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d5974284-79bc-4307-a95e-3531df15822a",
# META       "default_lakehouse_name": "Reliancemart_Silver",
# META       "default_lakehouse_workspace_id": "2a6c58fc-e653-4533-9bf0-26a8472d537a",
# META       "known_lakehouses": [
# META         {
# META           "id": "1ce326c4-6d5b-472f-a7f9-a1b7e526c9d4"
# META         },
# META         {
# META           "id": "d5974284-79bc-4307-a95e-3531df15822a"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ## Silver Transformation
# # 

# CELL ********************

# LOAD DATA FROM BRONZE LAYER

from pyspark.sql.functions import *

df_customers = spark.read.format("csv").option("header","true").load("Files/RelianceMart_Bronze_Customers/RelianceMart_customers.csv")
df_orders = spark.read.format("csv").option("header","true").load("Files/RelianceMart_Bronze_Orders/RelianceMart_orders.csv")
df_products = spark.read.format("csv").option("header","true").load("Files/RelianceMart_Bronze_Products/RelianceMart_products.csv")
df_reviews = spark.read.json("Files/RelianceMart_Bronze_Reviews/RelianceMart_review.json")
df_social = spark.read.json("Files/RelianceMart_Bronze_Social_Media/RelianceMart_social_media.json")
df_weblogs = spark.read.json("Files/RelianceMart_Bronze_Web_Logs/RelianceMart_web_logs.json")

# DATA CLEANING AND ENRICHING	
df_orders = df_orders.dropna(subset = ["OrderID", "CustomerID", "ProductID", "OrderDate", "TotalAmount"])
df_orders = df_orders.withColumn("OrderDate", to_date(col("OrderDate")))
# display(df_orders)

# JOIN WITH PRODUCTS & CUSTOMERS
df_orders = df_orders \
    .join (df_customers, on = 'CustomerID', how = "inner") \
    .join (df_products, on = 'ProductID', how = "inner")

# WRITE DATA TO SILVER LAYER	
df_orders.write.mode("overwrite").parquet("Files/RelianceMart_Silver_Orders/ShoppingMart_customers_orderdata")

df_reviews.write.mode("overwrite").parquet("Files/RelianceMart_Silver_Reviews/RelianceMart_review")
df_social.write.mode("overwrite").parquet("Files/RelianceMart_Silver_Social_Media/RelianceMart_social_media")
df_weblogs.write.mode("overwrite").parquet("Files/RelianceMart_Silver_Web_Logs/RelianceMart_web_logs")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
