"""Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one
item at a time. Insertion sort iterates, consuming one input element each repetition, and growing
a sorted output list. At each iteration, insertion sort removes one element from the input data,
finds the location it belongs within the sorted list, and inserts it there. It repeats until no
input elements remain. O(n^2)."""

import random

import pytest


def insertion_sort(array):
    """
    Sorts given array using insertion sort algorithm. O(n^2)

    :param list array: Array to sort.
    """
    for x in range(1, len(array)):
        current = array[x]
        for y in range(x - 1, -1, -1):  # looping backwards on sorted part of an array
            if current < array[y]:
                array[y], array[y + 1] = array[y + 1], array[y]
            else:
                break


# Testing:


@pytest.fixture(
    scope="module", params=[[], [1], [3, 1, 2], [random.randint(1, 100) for _ in range(100)]]
)
def arr(request):
    return request.param


@pytest.mark.parametrize("func", [insertion_sort])
def test_insertion_sort(func, arr):
    sorted_with_builtin = sorted(arr)
    func(arr)
    assert arr == sorted_with_builtin, (
        f"{func.__name__} with {arr} as input after sorting array looks: {arr}, "
        f"but {sorted_with_builtin} expected"
    )
