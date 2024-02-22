def findChange(lst01):
    left = 0
    right = len(lst01) - 1
    ind = None
    found = False
    while left <= right and found == False:
        mid = (left + right) // 2
        if mid > 0 and lst01[mid] == 1 and lst01[mid - 1] == 0:
            found = True
            ind = mid
        elif lst01[mid] == 0:
            left = mid + 1
        else:
            right = mid - 1
    return ind


lst01 = [0, 0, 0, 0, 0, 1, 1, 1]
print(findChange(lst01))
