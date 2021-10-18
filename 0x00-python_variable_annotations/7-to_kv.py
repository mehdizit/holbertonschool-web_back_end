#!/usr/bin/env python3
"""
    Mixed Tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        Args:
            k: a String
            v: Union: int or float
        Return:
            Tuple with string as first item and int or float as second item
    """

    result = (k, v**2)

    return result
