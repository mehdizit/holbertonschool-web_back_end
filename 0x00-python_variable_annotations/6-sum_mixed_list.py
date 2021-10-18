#!/usr/bin/env python3
"""Mixed lists"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        Args:
            mxd_lst: float-int numbers
        Return:
            Float base in int or float numbers
    """
    sum1: float = 0

    for x in mxd_lst:
        sum1 += x

    return sum1
