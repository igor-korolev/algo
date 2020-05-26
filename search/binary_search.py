"""
Binary search is a search algorithm that finds the position of a target value within a sorted
array. Binary search runs in logarithmic time O(log n)
"""
import random


def bin_search_recursive(array, what_to_find, left=0, right=None):
    """
    Finds element in a sorted array using recursion.

    :param list array: A sorted list of values.
    :param what_to_find: An item to find.

    :returns: Index of the searchable item or -1 if not found.
    """
    right = right if right is not None else len(array) - 1
    if left > right:
        return -1  # Searchable not found

    middle_pos = (left + right) // 2
    if array[middle_pos] == what_to_find:
        return middle_pos

    if what_to_find < array[middle_pos]:
        return bin_search_recursive(array, what_to_find, left=left, right=middle_pos - 1)
    return bin_search_recursive(array, what_to_find, left=middle_pos + 1, right=right)


# Testing
def test_item_should_be_found_recursive():
    array_for_test = sorted(random.randint(0, 1000) for _ in range(100))
    array_for_test.append(1001)  # Add testable item at the end of a test array
    found_pos, expected_pos = bin_search_recursive(array_for_test, 1001), 100
    assert (
        found_pos == expected_pos
    ), f"Wrong index position found: {found_pos}, expected: {expected_pos}"


def test_item_not_found_in_empty_array():
    found_pos, expected_pos = bin_search_recursive([], 1001), -1
    assert (
        found_pos == expected_pos
    ), f"Found {found_pos} in empty array, the position has to be {expected_pos}"


def test_item_should_not_be_found():
    found_pos, expected_pos = bin_search_recursive([1, 2, 3], 4), -1
    assert (
        found_pos == expected_pos
    ), f"Item 4 should not be found. Real: {found_pos}, expected: {expected_pos}"
