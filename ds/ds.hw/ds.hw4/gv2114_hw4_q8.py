def flat_list(nested_lst, low, high):
    flattened = []

    if low == high:  # this is the base case of whenever the index reaches the lowest level
        if isinstance(nested_lst[low], list):  # checks if the lowest lvl of the current lst is a lst or not
            flattened.extend(flat_list(nested_lst[low], 0, len(nested_lst[low]) - 1)) # recursively call to ensure
            # the only current value is not a list and the value itself is the only thing left
        else:
            flattened.append(nested_lst[low]) # if the lowest item in the range is not a lst, then the actual value
            # of gets added to flattened

    else:
        for i in range(low, high + 1):  # this is the main iteration over the recursive function
            if isinstance(nested_lst[i], list): # now we iterate through the entire lst using this for loop if the lst
                # is not empty
                flattened.extend(flat_list(nested_lst[i], 0, len(nested_lst[i]) - 1)) # recursively calls again
                # to ensure that this is the only possible value
            else:
                flattened.append(nested_lst[i]) # if the value is not a lst, then just add the current index itself

    return flattened
