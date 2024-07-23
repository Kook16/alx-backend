#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache (BaseCaching):
    """ MRUCache defines a MRU caching system """

    # def __init__(self):
    #     """ Initialize """
    #     super().__init__()
    #     self.order = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.pop(key)
            self.cache_data[key] = item
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Pop the first item (FIFO)
            most_recent_used_key = self.cache_data.popitem()[0]
            # self.cache_data.pop(least_used_key)
            print(f"DISCARD: {most_recent_used_key}")

        self.cache_data[key] = item
        # self.order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        val = self.cache_data.pop(key)
        self.cache_data[key] = val
        return self.cache_data[key]
