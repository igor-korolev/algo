# In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers
# up to any given limit. It does so by iteratively marking as composite (i.e., not prime) the
# multiples of each prime, starting with the first prime number, 2. The multiples of a given
# prime are generated as a sequence of numbers starting from that prime, with constant difference
# between them that is equal to that prime.


def sieve_of_eratosthene(num):
    """
    Computes prime numbers using sieve of Eratosthenes.

    :param num: The number to which you need to find prime numbers.

    :returns: List of prime numbers.
    """
    sieve = list(range(num))
    sieve[1] = 0  # All non-prime nums we'll replace by zeros.

    for checked_num in sieve[2:]:
        if checked_num != 0:
            multiplier = checked_num * 2
            while multiplier < num:
                sieve[multiplier] = 0
                multiplier += checked_num
    return [n for n in sieve if n != 0]


assert sieve_of_eratosthene(50) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
