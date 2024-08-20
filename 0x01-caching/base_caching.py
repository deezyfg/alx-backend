#!/usr/bin/python3
"""
Module for defining a base caching system with a dictionary storage.
"""


class BaseCaching():
    """
    BaseCaching class defines the structure for caching systems.

    Attributes:
        MAX_ITEMS (int): The maximum number of items the cache can hold.
        cache_data (dict): A dictionary to store cached data.
    """
    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize the cache data storage.
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the current state of the cache.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """
        Add an item to the cache.

        Args:
            key: The key under which the item should be stored.
            item: The item to be stored in the cache.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key: The key of the item to retrieve.

        Returns:
            The item associated with the given key,
            or None if the key is not found.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError(
            "get must be implemented in your cache class"
        )
