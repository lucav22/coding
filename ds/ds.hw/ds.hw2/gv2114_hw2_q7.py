def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    ind = None
    found = False
    while left <= right and found == False: # keeps running until either fails
        mid = (left + right) // 2
        if mid > 0 and lst01[mid] == 1 and lst01[mid - 1] == 0: #the logic here is that the midpoint has to have a
            #greater index than 0 since the first value has to be a 0 and the following 1 for the smallest value of
            #index 1. This is also because if the index is 0 then checking the left side would give an index error but
            # also to make sure the 1 is actually the first appearance
            found = True
            ind = mid
        elif lst01[mid] == 0: #if the mid value is 0, then the value has to be to the right of 0 to make the left pointer
            # move all the way to the nearest possible value it could be
            left = mid + 1
        else: #if neither is true, then we are too far into the values of 1 and need to go back to the left making right
            #as closes to the first appearance of 1
            right = mid - 1
    return ind


lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
print(findChange(lst01))
