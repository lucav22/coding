'''

generators

def f():
x=1
yield x
x+=1
yield x
x+=1
yield x

g = f()

g

prints out the generator object instead of the actual value

a generator is an iterator which can be called by next() and exposes multiple values

next(g)
1
next(g)
2
next(g)
3
next(g)
Stop Iteration


the essential use of generator is that you start with a variable of x = 1 and yield stores the value in a row and then you can add values
to it such as x+=1 that increases the value and when yield is called again then the value is kept as well


def elem in range(3,10,0.5)
    print(elem)

def my_range(start,stop,step):
    curr = start
    while(curr < stop):
        yield(curr)
        curr+=step

instead of printing the value, you instead yield them since it will store all of them and the user can then call the whichever value
they require and want to show

when the function is called no code will be executed, only a generator will be created for the moment



the holding execution and exposing the element when its needed, so the entire set is not required to expose the sequence

does not require a data structure to hold all of the memory at once


def integers():
    curr = 1
    while(True):
        yield(curr)
        curr+=1

simple change of instead of making a printing function, make it a generator by making it yield



Correctness and the Performance of Algorithms

Correctness: The provided output

Performance: Measure the resources that is used
-Time
-Space
-disk use
-disk-memory communication
-number of processors
-amount of communication





'''