#!/usr/bin/env python3
'''Web'''
import requests
from redis import Redis


r = Redis()


def get_page(url: str) -> str:
    '''Get Page'''
    r.incr(f"count:{url}")
    cache = r.get(url)
    if cache:
        return cache.decode("utf-8")
    resp = requests.get(url)
    r.setex(url, 10, resp.text)
    return resp.text
