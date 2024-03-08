def find_duplicates(lst):
    duplicates = []
    for number in lst:
        if lst[abs(number) - 1] < 0:
            # If the number is already marked, this is a duplicate and we ignore it
            if abs(number) not in duplicates:
                duplicates.append(abs(number))
        else:
            lst[abs(number) - 1] *= -1
    for i in range(len(lst)):
        lst[i] = abs(lst[i])
    return duplicates






