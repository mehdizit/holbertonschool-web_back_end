#!/usr/bin/python3
"""  Basic dictionary """
from base_caching import BaseCaching



class BasicCache(BaseCaching):
    """ Class that inherit from BaseCaching """
    def put (self, key, item):
        """ append the dictionary """
        if key and item:
            self.cache_data[key] = item
    
    def get(self, key):
        """ return value of cache """
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
    