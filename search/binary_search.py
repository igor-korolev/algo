# TODO: add docs and reformat


def bin_search(array, value):
    if not array:
        return None
    lenght = len(array)
    half = lenght // 2
    if array[half] == value:
        return half
    elif half == 0:
        return None

    if value > array[half]:
        return bin_search(array[half:], value)
    else:
        return bin_search(array[:half], value)


two = bin_search(list(range(10)), 2)
assert two == 2, "{} != 2".format(two)

one = bin_search([1, 5, 12, 15, 19, 23, 34, 44, 44, 90], 5)
assert one == 1, "{} != 2".format(one)

no = bin_search([34, 36, 99], 40)
assert no is None, "{} != 2".format(no)

no = bin_search([], 40)
assert no is None, "{} != 2".format(no)
