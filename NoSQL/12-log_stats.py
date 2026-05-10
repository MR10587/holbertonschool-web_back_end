#!/usr/bin/env python3
'''Provides some stats about Nginx logs stored in MongoDB'''
from pymongo import MongoClient


client = MongoClient('mongodb://127.0.0.1:27017')
collection = client.logs.nginx

print(f"{collection.count_documents({})} logs")
print("Methods:")
for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
    count = collection.count_documents({'method': method})
    print(f"    method {method}: {count}")
status = collection.count_documents({'method': 'GET', 'path': '/status'})
print(f"{status} status check")