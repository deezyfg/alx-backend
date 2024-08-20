#!/usr/bin/env python3
"""
Module implementing a basic caching system.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Cache class that inherits from BaseCaching
    """

    def put(self, key, item):
        """
        Store the item in the cache with the specified key.

        Args:
            key: The key under which the item is stored.
            item: The item to be stored in the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve the item from the cache associated with the specified key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the given key,
            or None if the key is not found.
        """
        return self.cache_data.get(key, None)
