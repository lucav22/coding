def split_parity(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] % 2 == 0 and lst[right] % 2 != 0: #check that the value is even but also that the value being exchanged
            # and ensuring the value being changed with is odd, since if its even, it needs to stay
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        if lst[left] % 2 != 0: #checking if its odd
            left += 1
        if lst[right] % 2 == 0: #checking if its even
            right -= 1
    return lst


lst1 = [1, 2, 3, 4]
print(split_parity(lst1))
