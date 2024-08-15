#!/usr/bin/env python3
"""
Module for deletion-resilient hypermedia pagination of a dataset.
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the Server instance with cached and indexed datasets."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: A list of lists containing the dataset rows.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Creates and returns a dataset indexed by sorting position,
        starting at 0.

        Returns:
            Dict[int, List]: A dictionary where keys are indices
                             and values are dataset rows.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieves a page of the dataset with deletion-resilient pagination.

        Args:
            index (int): The starting index of the dataset page.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing the current index,
                  data page, page size, and next index.

        Raises:
            AssertionError: If index or page_size is not a valid integer or
                            if index is out of range for the dataset.
        """
        assert type(index) == int
        assert type(page_size) == int
        csv = self.indexed_dataset()
        csv_size = len(csv)
        assert 0 <= index < csv_size
        data = []
        _next = index
        for _ in range(page_size):
            while not csv.get(_next):
                _next += 1
            data.append(csv.get(_next))
            _next += 1
        return {
            "index": index,
            "data": data,
            "page_size": page_size,
            "next_index": _next
        }
