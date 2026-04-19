# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e7d72935-a9b9-42b7-9079-92e47def4beb",
# META       "default_lakehouse_name": "Reliancemart_Gold",
# META       "default_lakehouse_workspace_id": "2a6c58fc-e653-4533-9bf0-26a8472d537a",
# META       "known_lakehouses": [
# META         {
# META           "id": "e7d72935-a9b9-42b7-9079-92e47def4beb"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# # Gold Transformation

# CELL ********************


from pyspark.sql.functions import *

Orders_df = spark.read.parquet("Files/RelianceMart_Silver_Orders/ShoppingMart_customers_orderdata")

reviews_df = spark.read.parquet("Files/RelianceMart_Silver_Reviews/RelianceMart_review")
social_df = spark.read.parquet("Files/RelianceMart_Silver_Social_Media/RelianceMart_social_media")
weblogs_df = spark.read.parquet("Files/RelianceMart_Silver_Web_Logs/RelianceMart_web_logs")
display(social_df)

# KPI1 : Aggregates web log data to measure engagement per user on each page and action.
# weblogs_df = spark.read.parquet("Files/ShoppingMart_Silver_Web_Logs/ShoppingMart_web_logs")
weblogs_df = weblogs_df.groupBy("user_id", "page", "action").count()
weblogs_df.write.mode("overwrite").parquet("Files/RelianceMart_Gold_Web_Logs/RelianceMart_web_logs")
#display(weblogs_df)

# KPI2 : Aggregates unstructured social media data to track sentiment trends across different platforms.
#social_df = spark.read.parquet("Files/ShoppingMart_Silver_Social_Media/ShoppingMart_social_media")
social_df= social_df.groupBy("platform","sentiment" ).count()
social_df.write.mode("overwrite").parquet("Files/RelianceMart_Gold_Social_Media/SRelianceMart_social_media")
# display(social_df)

#KPI3: Aggregates product reviews to calculate the average rating per product.
#reviews_df = spark.read.parquet("Files/ShoppingMart_Silver_Reviews/ShoppingMart_review")
reviews_df = reviews_df.groupBy("product_id").agg(avg("rating").alias("AvgRating"))
reviews_df.write.mode("overwrite").parquet("Files/RelianceMart_Gold_Reviews/RelianceMart_review")
#display(reviews_df)


Orders_df.write.mode("overwrite").parquet("Files/RelianceMart_Gold_Orders/RelianceMart_customers_orderdata")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
