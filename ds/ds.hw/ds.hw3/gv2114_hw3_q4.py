def remove_all(lst, value):
    pointer = 0
    for i in range(len(lst)):
        if lst[i] != value: # we are checking if the value needs to be replaced or not
            lst[pointer] = lst[i] # if the current index value is not equal to the value
            # the current pointer value is replaced with written over
            # if the value matches the index then the index is left alone since it will be replaced
            # and the other indexes are left untouched
            pointer += 1 # everytime the index is not the value, the pointer is increased to set the new lst index
            # since the value we want to remove is not going to be present we do not need to keep up the price
    return lst[:pointer] # the lst is sliced to the new value and no value is cut of since its
    # already replaced