#!/usr/bin/env python3
'''Web'''
import requests
from redis import Redis


r = Redis()


def get_page(url: str) -> str:
    '''Get Page and return its content while caching its value for 10 seconds'''
    r.incr(f"count:{url}")
    cache = r.get(f"count:{url}") 
    if cache:
        return cache.decode("utf-8")
    resp = requests.get(url)
    r.setex(f"count:{url}", 10, resp.text)
    return resp.text
