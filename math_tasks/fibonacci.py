# In mathematics, the Fibonacci numbers, commonly denoted Fn, form a sequence, called the
# Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0
# and 1.
from collections import namedtuple

import pytest


def fib_recursive(num):
    """
    Finds the N-th fibonacci number recursively.

    :param int num: The N-th fibonacci number (index).
    :return: Computed number.
    """
    if num < 2:
        return num
    return fib_recursive(num - 1) + fib_recursive(num - 2)


def fib_dict(num):
    """
    Finds the N-th fibonacci number recursively(but uses dict for memoization).

    :param int num: The N-th fibonacci number (index).
    :return: Computed number.
    """
    cache = {0: 0, 1: 1}

    def fib_recurs(n):
        if n in cache:
            return cache[n]
        cache[n] = fib_recurs(n - 1) + fib_recurs(n - 2)
        return cache[n]

    return fib_recurs(num)


def fib_loop(num):
    """
    Finds the N-th fibonacci number using ordinary for-loop.

    :param int num: The N-th fibonacci number (index).
    :return: Computed number.
    """
    if num < 2:
        return num

    first, second = 0, 1
    for i in range(2, num + 1):
        first, second = second, first + second
    return second


# Testing
Number = namedtuple("Number", ["value", "expected"])


@pytest.fixture(
    scope="module",
    params=[Number(1, 1), Number(2, 1), Number(3, 2), Number(10, 55)],
    ids=lambda s: f"Input: {s.value}, Expected: {s.expected}",
)
def number(request):
    return request.param


@pytest.mark.parametrize("func", [fib_recursive, fib_dict, fib_loop])
def test_fibonacci(func, number):
    result = func(number.value)
    assert result is number.expected, (
        f"{func.__name__} with '{number.value}' as input returned {result}, "
        f"but {number.expected} expected"
    )
