#!/usr/bin/env python3
'''List all documents in collection'''


def schools_by_topic(mongo_collection, topic):
    '''Return school by topic'''
    return mongo_collection.find({"topic": topic})
