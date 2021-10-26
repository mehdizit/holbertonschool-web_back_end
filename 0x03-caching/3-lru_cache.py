#!/usr/bin/python3
""" LRU Caching """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Class that inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()
        self.lru_order = []
    
    def put(self, key, item):
        """ Assign to the dictionary """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.lru_order.remove(key)
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    del self.cache_data[self.lru_order[0]]
                    print("DISCARD:", self.lru_order[0])
                    self.lru_order.pop(0)
                self.cache_data[key] = item
            self.lru_order.append(key)
    
    def get(self, key):
        """
        return the value of key in self.cache_data
        """
        if key in self.cache_data:
            self.lru_order.remove(key)
            self.lru_order.append(key)
            return self.cache_data[key]
        return None
    