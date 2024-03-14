def permutations(lst, low, high):
    if lst == high:
        return [[lst[low]]]

    