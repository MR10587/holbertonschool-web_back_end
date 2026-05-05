#!/usr/bin/env python3
'''Web'''
import requests
from redis import Redis


r = Redis()
count = 0


def get_page(url: str) -> str:
    count += 1
    r.set(f"count:{url}", count, ex=10)
    resp = requests.get(url)
    return resp

print(get_page("https://httpbin.org/delay/3"))