'''


insertion sort

the loop invariant will start at each iteration, the subarray consists of the sorted order

worst case quadratic runtime
best case quadratic runtime

selection sort

the start of each iteration smalles items in a sorted order

worst case quadratic runtime
best case quadratic runtime


the worst and best runetime is the same since it depends on the number of items and the type of sort


merge sort

** there is not sorting runtime that is under quadratic except maybe log runtime **

sort recursively the first half, and sort recursively the second half, and then merge the two halves together into one
sequence

runs through both lsts and sees which value is smaller or bigger than the other and adds them to the lst in order

def merge_sort(lst):
    if (len(lst) == 0):
        return
     elif (len(lst) == 1):
        return
 else:
     mid = len(lst) // 2
     left_lst = lst[ : mid]
     right_lst = lst[mid : ]
     merge_sort(left_lst)
     merge_sort(right_lst)
     merged = merge(left_lst, right_lst)
     for i in range(len(merged)):
        lst[i] = merged[i]


def merge(srt_lst1, srt_lst2):
    n1 = len(srt_lst1)
    n2 = len(srt_lst2)
    min1 = 0
    min2 = 0
    merged_lst = []

     while (i1 < len(srt_lst1)) and (i2 < len(srt_lst2)):
         if srt_lst1[i1] < srt_lst2[i2]:
             merged_list.append(srt_lst1[i1])
             i1 += 1
     else:
         merged_list.append(srt_lst2[i2])
         i2 += 1
     while i1 < len(srt_lst1):
         merged_list.append(srt_lst1[i1])
         i1 += 1
     while i2 < len(srt_lst2):
         merged_list.append(srt_lst2[i2])
         i2 += 1
     return merged_list










'''