

#1
# True
# True
# False # not the same thing


#2
# lst1 = [10,[2,30],[4,5],6]
# lst2 = [10,[2,30],[4,5],6]
# lst3 = [1,[2,30],[4,5],6] [:] will shallow copy the outside components BUT the nested lsts will be shared!
# lst4 = [1,[2,3], [4,5], 6]

#3
# def positive_prefix_sum(lst):
   # return [x for i in range(len(lst)) if sum(lst[:i+1]) > 0]
   # rmr how to do prefix sum as stated above and the specific parameter is only for the positive components
   # also formate for lst comprehension
   # i for i in (iterable collection) if (condition)

#4
def reverse1(lst):
    rev_lst = []
    i = 0
    while i < len(lst):
        rev_lst.insert(0,lst[i]) #this will continuously increase as it reaches n
        # my guess is n^2
    return rev_lst

# pattern
# growth or formula
# runtime

def reverse2(lst):
    rev_lst = []
    i = len(lst) - 1
    while i >= 0: # seems to be linear time as it will append one item at a time n
        # and each call is dependent on the size of n so it will either be really fast or slow
        rev_lst.append(lst[i])
        i -= 1
    return rev_lst

#5

'''each call will result in the lst getting cut in half at the midpoint
as a result, each call will be in linear time, as a result the runtime will be log n
since the summation will look something like 1 + 2 + 4 + 8 + 16 + 32 + n = 2n-1 and n'''

#6
def remove_all_evens(lst):
    pointer = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0: #if it is not even then keep since we are going to copy its index
            # if it is odd (which is what we want) we can then add it to the position in front of us or same place
            lst[pointer] = lst[i]
            pointer += 1
    del lst[pointer:] # since they want us to keep the same lst

lst  = [2,3,5,2,16,13]
print(remove_all_evens(lst))

#7
def is_sorted(lst, low, high):
    if low > high:
        return True
    if lst[low] > lst[low + 1]: #as the condition is stated, if this happens then its false
        return False
    else:
        return is_sorted(lst, low+1, high) # only increase low since we want to make sure all of the values
        # in high are kept

lst1 = [1,3,6,8,12,15,31]
print(is_sorted(lst1, 0, 6))



