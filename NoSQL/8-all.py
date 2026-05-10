#!/usr/bin/env python3
'''List all documents in collection'''
from pymongo import MongoClient


def list_all(mongo_collection):
    documents = []
    for document in mongo_collection:
        documents.append(document)
    return documents
