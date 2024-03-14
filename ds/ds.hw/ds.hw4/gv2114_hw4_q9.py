def permutations(lst, low, high):
    if low == high:
        return [[lst[low]]] # if the range of the permutation has been reduced to only one value
    # then it will take into consideration this case and ensure that it keeps the same format for the rest of
    # the other permutations

    all_permutations = [] # empty lst to return all the resulting permutations

    for i in range(low, high + 1): # iterates through the given range to see how many permutation will occur
        lst[low], lst[i] = lst[i], lst[low] # flips all the values to be not in the same place
        inner_permutations = permutations(lst, low + 1, high) # if there are other values then we go through
        # each smaller permutations through the lst and gradually decrease the amount of items in each
        # permutation
        for permutation in inner_permutations: # how many times we get a different result from the previous
            # recursive function
            all_permutations.append([lst[low]] + permutation) # actually adding the result to the main lst
        lst[low], lst[i] = lst[i], lst[low] # again switching the values so we can get the original state of the lst
        # and not lose this permutation as well

    return all_permutations

lst = [1,2,3]
print(permutations(lst, 0, 2))