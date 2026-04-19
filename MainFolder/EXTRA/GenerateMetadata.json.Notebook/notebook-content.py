# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1ce326c4-6d5b-472f-a7f9-a1b7e526c9d4",
# META       "default_lakehouse_name": "Reliancemart_Bronze",
# META       "default_lakehouse_workspace_id": "2a6c58fc-e653-4533-9bf0-26a8472d537a",
# META       "known_lakehouses": [
# META         {
# META           "id": "1ce326c4-6d5b-472f-a7f9-a1b7e526c9d4"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
import requests
import json

repo = "Reliancemart_FabricMedallion"
folder = "Structured_data"
user = "Akshithraj"
api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{folder}"

response = requests.get(api_url)
files = response.json()

metadata = []
for f in files:
    if f['name'].endswith('.csv'):
        metadata.append({
            "source_url": f['path'],  # relative path
            "sink_folder": f"RelianceMart_Bronze_{f['name'].split('.')[0]}",
            "sink_file": f"RelianceMart_{f['name']}"
        })

df = spark.createDataFrame(metadata)

df.write.mode("overwrite").json(
    "Files/ReliancemartBronze/metadata"
)

metadata

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.option("multiline", "true").json("Files/ReliancemartBronze/metadata/part-00000-416669eb-66fb-47a3-8224-5921b36041df-c000.json")
# df now is a Spark DataFrame containing JSON data from "Files/ReliancemartBronze/metadata/part-00000-416669eb-66fb-47a3-8224-5921b36041df-c000.json".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
