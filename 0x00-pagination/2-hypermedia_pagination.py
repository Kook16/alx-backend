#!/usr/bin/env python3
'''Simple helper function'''
from typing import Tuple, List, Dict
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    ''' return a tuple of size two containing
    a start index and an end index '''
    return (
        (page - 1) * page_size,
        page * page_size,
    )


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

        Returns:
        List[List]: List of rows corresponding to the page
        """
        assert isinstance(page, int) and page > 0, "Page must be\
            an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must\
            be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination details.

        Args:
        page (int): Page number (1-indexed)
        page_size (int): Number of items per page

        Returns:
        Dict: Dictionary with pagination details
        """
        assert isinstance(page, int) and page > 0, "Page must be\
            an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "Page size must\
            be an integer greater than 0"

        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)

        data = dataset[start_index:end_index]

        total_pages = (len(dataset) + page_size - 1) // page_size

        return {
            "page_size": page_size if page <= total_pages else 0,
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
