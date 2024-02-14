'''


def binary_search(srt_lst,val):
    left = 0
    right = len(srt_lst)-1
    ind = NONE
    found = False

    while(found == False) and (left <= right):
        mid = (left+right)//2
        if (val == srt_lst[mid]):
            ind = mid
            found = True
        elif (val < srt_lst[mid])
            right = mid - 1
        else:
            left = mid + 1
    return ind

keeps cutting the lst in half until finding the value, if the value is not found check if we need to cut to the right
or left side of the lst, it will continue running until the value is found or if the left or the right bound crosses
each other

the time of the body inside of while is constant and so is the before text, so far its constant time, the cost of the
algorithm will be the number of iterations,

the worst time would be theta of log(n) since it depends on the number of iterations and it is in better time than
time n since it is faster

lst = [10,20,30,40]

len(lst)
theta (n) would run when calling for len(lst)

we can store the size of the lst in the lst object in order to make len run in constant time

lst[3]
linear time would occur here again which is not good

Array: A fixed size sequential collection that:
All the elements are stored continuously in the memory

All the elements are of the same size

address of arr[3] = base address of arr + 3*(size of each element)

1000 + 3*4

array allow random access (constant time)

the size of the containers are the same but the container can hold any size item, it makes it easier to access any
specific index

so instead address of arr[k] = base address of arr + k*(size of each element)

lst.append(50)









'''