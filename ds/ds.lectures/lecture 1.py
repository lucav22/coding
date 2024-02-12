'''
java
int x
x = 10

python
x = 10

python type is associated with the object with the given value and x is pointing to the int value
if another value is assigned to x, then x now points to the new value


x=10
x=15
the original pointer of x to 10 would remain but a new pointer would go to 15 as both are now active

lst = [1,2,3]
for elem in lst:
    elem = elem +10
lst

lst is the reference data by python and it creates a lst object
the lst object has a pointer to three blocks that each reference three int items
each container would reference each content

three iteration are to be expected

elem becomes apart of the dataset as well and it references to the specific data

once the code goes to elem = elem + 10  , it makes a new reference to int 11 but since the original lst object
still points to int 1 int 2 and int 3, then the lst returns the original values

**immutable meaning no change**


lst = [1,2,3]
for i in range(len(lst)):
    lst[i] = lst[i] + 10
lst

reference to i in data of python points to int 0 but since it references to lst[i] + 10


lst1 = [1,2,3]
lst2 = lst1
lst3 = [1,2,3]
lst1.append(6)
lst2.append(5)
lst3.append(6)
***append adds new item to the end of a lst function***

each assigned lst has a value to them in the data and are pointing to a lst object and now pointing to 1,2,3 int objects

lst2 will point to the same lst1 object
lst3 will be pointing to a new lst object

the appended value of 4 as an integer object is not true


s1 = 'abc'
s1.upper()
s1

s1 is assigned to str object "abc" and the str object points to three spaces with each individual letter
s1 is ***immutable*** so it cannot be changed
s1.upper starts a new str object but it is not used
instead s1 = s1.upper() the original reference will no reassign itself to the new data

def main():
    lst = [1,2,3]
    s = 'abc'
    func(lst,s)
    print(lst,s)
def func(lst,s):
    lst.append(4)
    s = s.upper
    print(lst, s)
main()


when running main, func is then ran, first print statement, and then the second print statement


'''
