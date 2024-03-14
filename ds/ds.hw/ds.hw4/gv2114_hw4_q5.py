def count_lowercase(s, low, high):  # need to return a value
    if low == high:
        return int(s[low].islower())  # acts as a boolean function that will return a 1 or 0 if its true or false
    else:
        mid = (low + high) // 2
        low_count = count_lowercase(s, low, mid)  # similar method of using boolean search with mid
        high_count = count_lowercase(s, mid + 1, high) # add one to mid since we dont wanna lose a value
        return low_count + high_count  # adds the counts of going through the low and high counts


def is_number_of_lowercase_even(s, low, high):
    count = count_lowercase(s, low, high)  # we did the function already just redo it again and just check if its even
    return count % 2 == 0
