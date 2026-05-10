#!/usr/bin/env python3
'''List all documents in collection'''
from pymongo import MongoClient


client = MongoClient()
logs = client.logs
collection = logs.nginx

all = collection.count_documents({})
print(f"{all} logs")
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for method in methods:
    count = collection.count_documents({'method': method})
    print(f"\tmethod {method}: {count}")
status = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f"{status} status check")




