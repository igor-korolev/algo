# In mathematics, the Euclidean algorithm, or Euclid's algorithm, is an efficient method
# for computing the greatest common divisor (GCD) of two integers (numbers), the largest number
# that divides them both without a remainder.


def gcd_by_subtracting(m, n):
    """
    Computes the greatest common divisor of two numbers by continuously subtracting the smaller
    number from the bigger one till they became equal.

    :param int m: First number.
    :param int n: Second number.

    :returns: GCD as a number.
    """
    while m != n:
        if m > n:
            m -= n
        else:
            n -= m
    return m


assert gcd_by_subtracting(112, 12345678) == 2


def gcd_recursive_by_divrem(m, n):
    """
    Computes the greatest common divisor of two numbers by recursively getting remainder from
    division.

    :param int m: First number.
    :param int n: Second number.

    :returns: GCD as a number.
    """
    if n == 0:
        return m
    return gcd_recursive_by_divrem(n, m % n)


assert gcd_by_subtracting(112, 12345678) == 2


def gcd_looping_with_divrem(m, n):
    """
    Computes the greatest common divisor of two numbers by getting remainder from division in a
    loop.

    :param int m: First number.
    :param int n: Second number.

    :returns: GCD as a number.
    """
    while n != 0:
        m, n = n, m % n
    return m


assert gcd_by_subtracting(112, 12345678) == 2
