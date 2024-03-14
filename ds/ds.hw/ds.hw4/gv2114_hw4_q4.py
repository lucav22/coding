def list_min(lst, low, high):
    if low == high:
        return lst[low]  # does not matter if the low or high index since it will be the same length
    else:
        mid = (low + high) // 2  # basically binary search on finding the middle point of entry
        low_search = list_min(lst, low, mid)  # searching each value in the lower section of the lst
        high_search = list_min(lst, mid + 1, high)  # searching each value in the higher section of the lst
        # also add one since we do not wanna lose a value
    return min(low_search, high_search)  # searching through the parameters for the low and high value
