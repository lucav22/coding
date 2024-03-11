def powers_of_2():
    curr = 1
    while(True):
        yield curr
        curr *= 2

powers_of_2_gen = powers_of_2()
for i in range(4):
    elem = next(powers_of_2_gen)
    print(elem, end='')
print()



lst1 = [1,2,[3,4]]
lst2 = lst1
lst3 = lst1 + lst2
lst2[0] = 10
lst2[2][0] = 30
print(lst1)
print(lst2)
print(lst3)



def func1(n):
    res_lst = []
    i = 1
    while (i <=n):
        res_lst.append(i)
        i *= 2
    return res_lst

def func2(n):
    res_lst = []
    i = 1
    while (i <=n):
        res_lst = res_lst + [i]
        i *=2
    return res_lst

def func3(n):
    res_lst = [1]
    i = 1
    while (i <=n):
        res_lst = res_lst + res_lst
        i *= 2
    return res_lst

def copy(self):
    # Create a new instance of ArrayList, initializing it with the current size to optimize the creation process.
    new_array_list = ArrayList()
    # Copy the elements. Since the __iter__ method is already defined, we can use it to iterate over the current array.
    for item in self:
        new_array_list.append(item)
    return new_array_list


def partition(lst):
    pivot = lst[0]
    res_lst = [pivot]
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            res_lst.insert(0,lst[i])
        else:
            res_lst.append(lst[i])
    return res_lst

def partition2(lst):
    pivot = lst[0]
    smaller = []
    greater = []
    for i in range(1, len(lst)):
        if lst[i] < pivot:
            smaller.append(lst[i])
        else:
            greater.append(lst[i])
    return smaller + [pivot] + greater
