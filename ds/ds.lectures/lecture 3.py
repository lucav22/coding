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




;





'''