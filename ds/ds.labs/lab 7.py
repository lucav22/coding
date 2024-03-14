

def intersectionOfLst(lst1, lst2):
    res = []

    ptr1 = 0
    ptr2 = 0
    while ptr1 < len(lst1) and ptr2 < len(lst2):
        if lst1[ptr1] == lst2[ptr2]:
            res.append(lst1[ptr1])



def isPowerOfTwo(n):
    if n == 1:
        return True
    elif n < 1:
        return False
    return isPowerOfTwo(n/2) # log time is always dividing by two


def split_parity(lst, low, high): #exam 1 question
    if low <= high:
        if lst[low] % 2 != 0 and lst[high] % 2 == 0:
            lst[low],lst[high] = lst[high] , lst[low]
        if lst[low] % 2 == 0:
            low += 1
        if lst[low] %2 != 0:
            high -= 1
        split_parity(lst,low,high)

def SortList(lst):
    count = [0] * (max(lst) + 1)

    for i in lst:
        count[i] += 1

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            lst[index] = i
            index += 1
            count[i] -= 1



def nested_sum(lst):
    if isinstance(lst,int):
        return lst
    else:
        total = 0
        for i in lst:
            total += nested_sum(i)
        return total

def nested_depth_level(lst):
    if isinstance(lst,int):
        return 1 + max(nested_depth_level(elem) for elem in lst)
    else:
        return 0

def nested_depth_level2(lst):
    return 1 + max(nested_depth_level2(elem) if isinstance(elem,list) else 0 for elem in lst)


def deep_reverse(lst, low, high):
    if low > high:
        return 