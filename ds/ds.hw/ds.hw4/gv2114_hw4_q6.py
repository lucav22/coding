def appearances(s, low, high):
    if low == high:
        return {s[low]: 1} # initialize the dictionary since there is an appearance

    else:
        mid = (low + high) // 2 # again binary search
        left_appearances = appearances(s, low, mid) # finding the left side of the dictionary values
        right_appearances = appearances(s, mid + 1, high) # finding the right side of the dictionary values as well

    for char, count in right_appearances.items(): # returns the items in the dictionary is the form of a lst
        if char in left_appearances: # this checks if the char is found in the right_appearances and if it is found
            left_appearances[char] += count # if the value already exists then the left_appearances value is updated
        else:
            left_appearances[char] = count # if the value is not found, then the value found in right_appearances is
            # is added to the left_appearances

    return left_appearances # as a result, we only have to return one side of the appearances, which we chose left to be
    # the side we return


