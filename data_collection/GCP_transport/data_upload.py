from google.cloud import storage
import json
import itertools
import pandas as pd
from sodapy import Socrata


## Retrieve Data From Online Portal
# Authenticate API client:
client = Socrata("data.cityofchicago.org",
                "uxnrv7ZjS2c3jlrgMaXw9cNko",
                username="abeburton@me.com",
                password="js9@5x#H9@wp2#Y")
# results is a generator
results = client.get_all("m6dm-c72p", year=)
# select all indices of the generator to make a list of dicts
result_list = list(itertools.islice(results, 299602996))


## Move Data to GCS
# Initialize a client
storage_client = storage.Client()

# Define your Google Cloud Storage bucket and file path
file_path = 'bdp-rideshare-project/rideshare/rideshare.json'

# Convert the JSON object to a JSON string
json_data = json.dumps(result_list)

# Write the JSON data to Cloud Storage
with storage_client.bucket("msca-bdp-student-gcs").blob(file_path).open("w") as file:
    file.write(json_data)

print("JSON data written to Cloud Storage")
