'''


from lists import ArrayList

arr_lst = ArrayList()
for i in range(5)
    arr_lst.append(i+1)

print()

it will have the values from 1 to 5 and the physical capacity will be 8 since the append will increase the physical size

def __iter__(self):
    for i in range(len(self)):
        yield(self[i]) #this will access the data inside of the array



def count_up(start,end):
    if (start == end):
        print(start)
    else:
    count_up(start, end-1)
    print(end)

when the value is not eh value we want, print out the value of start, if not then keep on calling

def count_up(start,end):
    if (start == end):
        print(start)
    else:
    print(start)
    count_up(start+1, end)

another implementation, same method of working

def count_up(start,end):
    if (start == end):
        print(start)
    else:
    mid = (start+end)//2
    count_up(start, mid)
    count_up(mid + 1, end)

another recursive call that takes the mid point of one side to the other mid side as well


'''