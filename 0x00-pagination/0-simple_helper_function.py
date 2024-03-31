#!/usr/bin/env python3
"""
a function return a tuple of size two containing a
start index and an end index
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start and end index.
    """
    start_index = (page - 1) * page_size
    end_index = (((page - 1) * page_size) + page_size)
    return start_index, end_index
