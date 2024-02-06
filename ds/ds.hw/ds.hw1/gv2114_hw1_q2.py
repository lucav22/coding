def shift(lst, k, shift = 'left'):
    for i in range(k):
        if shift == 'left':
            lst.append(lst[0])  # index 0 since value being appended is always
            # what is at the front
            lst.pop(0)  # same here for pop always the first index being removed
        else:
            lst.insert(0, lst[-1])  # since we want to insert at the front, we do insert
            # instead of append
            lst.pop(-1)  # and then remove the last items now
    return lst


