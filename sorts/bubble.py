"""Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares
adjacent elements and swaps them if they are in the wrong order. The pass through the list is
repeated until the list is sorted."""

import random

import pytest


def bubble_sort(array):
    """
    Sorts given array using bubble sort algorithm. O(n^2)

    :param array: Array to sort.
    """
    iterate_to = len(array) - 1
    is_swapped = True  # Indicates whether inner loop has any swaps, if not - the array is sorted

    while iterate_to > 0 and is_swapped:
        is_swapped = False
        for i in range(iterate_to):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_swapped = True
        iterate_to -= 1


# Testing:


@pytest.fixture(
    scope="module", params=[[], [1], [1, 2, 3], [random.randint(1, 10) for _ in range(100)]],
)
def arr(request):
    return request.param


@pytest.mark.parametrize("func", [bubble_sort])
def test_bubble_sort(func, arr):
    sorted_with_builtin = sorted(arr)
    func(arr)
    assert arr == sorted_with_builtin, (
        f"{func.__name__} with {arr} as input after sorting array looks: {arr}, "
        f"but {sorted_with_builtin} expected"
    )
