# Wikipedia: Karp–Rabin algorithm is a string-searching algorithm created by Richard M. Karp and
# Michael O.Rabin (1987) that uses hashing to find an exact match of a pattern string in a text.

import hashlib


def find_substr(full_string, substring):
    """
    Finds starting index of the substring.

    :param full_string: The whole string where to search.
    :param substring: Substring to find.

    :returns: Index of the found substring or -1.
    """
    subs_len = len(substring)
    s_len = len(full_string)
    assert s_len > 0 and subs_len > 0, "String and substring cannot be empty"
    assert subs_len < s_len, "Substring is shorter than the full string"

    subs_hash = hashlib.sha1(substring.encode("utf-8")).hexdigest()

    for i in range(s_len - subs_len + 1):
        checked_substr = s[i : i + subs_len]
        if subs_hash == hashlib.sha1(checked_substr.encode("utf-8")).hexdigest():
            if checked_substr == substring:  # Additional check in case of collision
                return i
    return -1


# Testing
s = "Just a simple string for test"  # Index of word 'simple' is 7
subs = "simple"
found_substring_index = find_substr(s, subs)
assert (
    found_substring_index == 7
), f"Found substring index is wrong: {found_substring_index}"
