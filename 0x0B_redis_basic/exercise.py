#!/usr/bin/env python3
'''Redis Start'''
import redis
import uuid
import typing


class Cache:
    '''Cache'''
    def __init__(self):
        '''Init'''
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        '''Store'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
