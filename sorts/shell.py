"""Shellsort is an in-place comparison sort. The method starts by sorting pairs of elements far
apart from each other, then progressively reducing the gap between elements to be compared. By
starting with far apart elements, it can move some out-of-place elements into position faster
than a simple nearest neighbor exchange. Designed Donald Shell. O(n^2)."""

import random

import pytest


def get_ciur_gaps(array_len):
    """
    The empirical sequence of Marcin Ciur is one of the best known for sorting an array with a
    lenghth of about 4000 elements. Here we decide which gaps are suitable for the provided array.

    :param array_len: Lenght of an array.
    :return: Yields gaps.
    """
    gaps = (1, 4, 10, 23, 57, 132, 301, 701, 1750)
    for gap in gaps[::-1]:
        if gap >= array_len:
            continue
        yield gap


def shell_sort(array):
    """
    Sorts in-place given array using shell sort algorithm. This algorithm uses gaps to compare
    elements. This implementation uses Ciur sequence. O(n^2).

    :param list array: Array to sort.
    """
    for gap in get_ciur_gaps(len(array)):
        for to_compare in range(gap, len(array)):  # Positions of elements to compare
            # Find out all positions of elements that will be used for comparison with items above
            for compare in range(to_compare - gap, -1, -gap):  # Loop backwards as in the algorithm
                if array[to_compare] < array[compare]:
                    array[to_compare], array[compare] = array[compare], array[to_compare]
                to_compare -= gap  # Decrement element index if between gap more than one element


# Testing:


@pytest.fixture(
    scope="module", params=[[], [1], [3, 1, 2], [random.randint(1, 100) for _ in range(100)]]
)
def arr(request):
    return request.param


@pytest.mark.parametrize("func", [shell_sort])
def test_shell_sort(func, arr):
    sorted_with_builtin = sorted(arr)
    func(arr)
    assert arr == sorted_with_builtin, (
        f"{func.__name__} with {arr} as input after sorting array looks: {arr}, "
        f"but {sorted_with_builtin} expected"
    )
