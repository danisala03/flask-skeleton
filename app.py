from flask import Flask
import json
import os
import sys
import uuid

from azure.core.exceptions import AzureError
from azure.cosmos import CosmosClient, PartitionKey

ENDPOINT = os.environ["COSMOS_ENDPOINT"]
KEY = os.environ["COSMOS_KEY"]
DATABASE_ID = "dbtest"

client = CosmosClient(url=ENDPOINT, credential=KEY)

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        database = client.create_database_if_not_exists(id=DATABASE_ID)
        return f"Database created or returned: {database.id}"

    except:
        return "Request to the Azure Cosmos database service failed."

if __name__ == '__main__':
    app.run(debug=True)
