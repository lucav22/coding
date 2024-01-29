'''

lst1 = counter() for i in range(3)]

for c in lst1:
    c.inc()
    print(c)

increasing the value for each counter object in range
the memory has a container of size 3 with the object type of lst
the first element is a counter object that is called and stated as 0
everytime a counter object is being executed making multiple objects of the same counter in the lst

;

lst2 = [Counter()]*3

for c in lst2;
    c.inc()
    print(c)

same method id being performed here except with a different lst
works differently as the there is the original lst 2 object that contains only one object with counter = 0
and then consequently another lst 2 that is sharing its value with the original lst2 (lstthat is temporary since * is a
constructor)

lst1 = [1,2,3]
lst2 = [4,5]
lst1.extend()

the second expressions does not have to be a second lst, but it can such as the result of this in order of 5 data

SEPARATE to append as append would add it as a singular data container whereas extend adds the size of the second lst

lst 1 points to a lst object with three containers
lst 2 points to 4 and 5
extend simply mutates the lst1 to contain the objects of lst2

lst1 = [1,2,3]
lst2= [4,5]
lst1 += lst2

lst1 = lst1 + lst2
NOT SIMILAR

instead it mutates the lst and its equivalent to extend as stated previously


for loops are used for iterable-collections
an object that produces an inter via the syntax inter(iterable object)

lst = [1,2,3]
lst_iter = iter(lst)

this produces an iterator since it was closed in the iter object

s = "abc"
s_iter = iter(s)

again the iterator objects is created


an iterator is an objects that contains or exposes a series of values that makes subsequent calls to next(iterator)


next(lst_iter)
1
next(lst_iter)
2

going through the values in the collection in order as being called in next

next(lst_iter)
StopIteration error that happens when the collection is empty

can use the iter function multiple times to make two different iter objects that each have their own order of nest

lst = [1,2,3]
lst_iter1 = iter(lst)
lst_iter2 = iter(lst)

s = 'abc'
for item in s:
    print(item)

restricted on using a for loop

s = 'abc'
s_iter = iter(s)
end = False
make an iter object to then use a while loop to use next

while(end == False ):
    try:
        item = next(s_iter)
        print(item)
    except StopIteration
        end == True


assign each value that is being called to item
before the loop make sure to have a boolean variable that way when the except error is raised, the variable can be changed
to stop the while loop since the value has been change to true

for elem in range(3,10,0.5)
    print(elem)

    starts from 3 to 10 in jumps of .5 to 9.5 since its exclusive

write our own version of range

def my_range (start,stop, step):
    res = []
    curr = start
    while (curr < stop):
        res.append(curr)
        curr += step
    return res

adds all values of the step into a giant lst and continues the while loop until it reaches the end

the entire runtime of the function is spend running my_range instead of running the for loop





;





'''