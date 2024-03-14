def split_by_sign(lst, low, high): #extremely similar approach to split_by_parity (same as exam and lab question)
    # sadly not enough time on the exam though :D
    if low <= high: # set the correct constraints so we stay within the range of the lst
        if lst[low] > 0 and lst[high] < 0: # if the index results in a positive value and the high index is positive
            # then switch their places
            lst[low], lst[high] = lst[high], lst[low]
        if lst[low] < 0: # if the index of low results in a negative value, ignore it in place and increase the count
            low += 1
        if lst[high] > 0: # if the value is positive on the high side, then ignore that value as well
            high -= 1
        split_by_sign(lst, low, high) # recursive function

lst = [-5, -4, 4, 2,-2, 9, 11, -59]

print(split_by_sign(lst,0, 7))
print(lst)