def two_sum(srt_lst, target):
    left = 0
    right = len(srt_lst) - 1
    ind = None
    found = False

    while left < right and found == False:
        if target == (srt_lst[left] + srt_lst[right]):
            ind = (left, right)
            found = True
        elif target < (srt_lst[left] + srt_lst[right]):
            right -= 1
        else:
            left += 1
    return ind


srt_lst = [-2, 7, 11, 15, 20, 21]
print(two_sum(srt_lst, 22))
