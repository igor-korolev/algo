# From the wikipedia(https://en.wikipedia.org/wiki/Ackermann_function)
# In computability theory, the Ackermann function, named after Wilhelm Ackermann, is one of the
# simplest and earliest-discovered examples of a total computable function that is not primitive
# recursive. All primitive recursive functions are total and computable, but the Ackermann function
# illustrates that not all total computable functions are primitive recursive.
import sys
sys.setrecursionlimit(3000)


def acker(m, n):
    """
    Computes the value of the Ackermann function for the input integers m and n.

    :param int m: First number.
    :param int n: Second number.

    :returns: Computed value.
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return acker(m - 1, 1)
    return acker(m - 1, acker(m, n - 1))


assert acker(3, 8) == 2045
