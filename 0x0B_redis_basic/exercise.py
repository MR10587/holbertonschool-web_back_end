#!/usr/bin/env python3
'''Redis Start'''
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Count calls'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, *kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    '''Input and output history'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__

        self._redis.rpush(key + ":inputs", str(args))

        output = method(self, *args, **kwargs)
        self._redis.rpush(key + ":outputs", output)
        return output
    return wrapper

class Cache:
    '''Cache'''
    def __init__(self):
        '''Init'''
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Store'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        '''Get type'''
        value = self._redis.get(key)

        if value is None:
           return value

        if fn:
            return fn(value)
        return value

    def get_str(self, key):
        '''String'''
        return self.get(key, fn = lambda d: d.decode("utf-8"))

    def get_int(self, key):
        '''Integer'''
        return self.get(key, int)
