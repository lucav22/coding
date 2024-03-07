def find_duplicates(lst):
    duplicates = []
    for number in lst:
        # Since the elements are from 1 to n-1, we adjust by subtracting 1 to use 0-indexed Python lists
        if lst[abs(number) - 1] < 0:
            # If the number is already marked, this is a duplicate
            if abs(number) not in duplicates:
                duplicates.append(abs(number))
        else:
            # Mark the number seen by negating the value at its index
            lst[abs(number) - 1] *= -1
    # Restore the list to its original state (optional)
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    return duplicates






