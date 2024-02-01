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



prime is divisors are 1 and num
complimentary is d * k equal or divisors of 100




def is_prime(num):
    count_divs=0

    for curr in range (1,num+1):
        if (num%curr == 0):
            count_divs += 1
    if (count_divs==2)
        return True
    else:
        return False

takes the range of the value from 1 to the ending of the number (accounting for range being exclusive)
runs an if statement for a mod for each number and if there eis no remainder, then the count is increased since that means
a number is divided evenly, if the count reaches 2 that means there are two numbers thats divide evenly

we are trying to prove that there is no factor in the other half of the number

so we take k and only the second half of the range so we do k> num/2

then we take k's complementary divisor which would be d which is another d = num/k

which then equals to d < 2, meaning that the only number left is d = 1  so k = num and that the only divisor in the
second half is the number itself




'''