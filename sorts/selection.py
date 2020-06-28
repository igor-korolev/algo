"""Selection sort is an in-place comparison sorting algorithm.The algorithm divides the input
list into two parts: a sorted sublist of items which is built up from left to right at the front
(left) of the list and a sublist of the remaining unsorted items that occupy the rest of the
list. O(n^2)."""

import random

import pytest


def selection_sort(array):
    """
    Sorts given array using selection sort algorithm. O(n^2)

    :param array: Array to sort.
    """
    for x in range(len(array)):
        smallest_i = x
        for y in range(x + 1, len(array)):
            if array[y] < array[smallest_i]:
                smallest_i = y
        array[x], array[smallest_i] = array[smallest_i], array[x]


# Testing:


@pytest.fixture(
    scope="module", params=[[], [1], [1, 2, 3], [random.randint(1, 100) for _ in range(100)]]
)
def arr(request):
    return request.param


@pytest.mark.parametrize("func", [selection_sort])
def test_selection_sort(func, arr):
    sorted_with_builtin = sorted(arr)
    func(arr)
    assert arr == sorted_with_builtin, (
        f"{func.__name__} with {arr} as input after sorting array looks: {arr}, "
        f"but {sorted_with_builtin} expected"
    )
