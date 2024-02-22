def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    ind = None
    found = False

    while left < right and found == False:  # keeps running until either condition is broken
        if target == (srt_lst[left] + srt_lst[right]):
            ind = (left, right)  # tuple value is set here
            found = True
        elif target < (srt_lst[left] + srt_lst[right]):  # if the addition of the indices overshoots the target value
            # that means that the value of the right index is too much we need to decrease the right index
            right -= 1
        else:  # if the target value is too low, then the left index is not high enough to sum with the right value and
            # thus needs to be increased to match the target
            left += 1
    return ind


srt_lst = [-2, 7, 11, 15, 20, 21]
print(two_sum(srt_lst, 22))
