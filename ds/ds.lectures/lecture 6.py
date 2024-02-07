'''

the asymptotic notation of O is that g is an upper bound of f<g


if f is under a multiple of with g with a constant and it starts at any point, it can be claiimed then that f is bounded
by upper bound g


the asymptotic notation of omega is that g is a lower bound of f>g

meaning that f has to be greater than g by any constant of c

the asymptotic notation of theta is that g is an upper bound of f = g

meaning that f has to be in between two multiples of g that keep it inside of the range of being
equal to each other

3n^2 + 6n - 15 = theta(n^2)

the proof is finding the three constants

we start by doing comparisons 3n^2 + 6n - 15 < 3^2 + 6n < 3n^2 + 6n^2 = 9n^2 since they are all greater than the original
function provided

so c 1 which is < c1n becomes 9

      3n^2 < 3n^2 + 6n - 15

we get n0 from seeing where 6n-15 is positive which would be n>2.5 which the becomes n0 = 3 and c2 = 3

which makes the range 3n^2 to 9n^2



def print_square(n)
    for i in range(1,n+1):
    line = '*' * n
    print(line)

    what would be the runtime of this function? T(n) =

forms a square with starts

equal is one runtime, but when multiplication is used in the context of duplication such as ( * n )

the asymptotic costs turns out to be theta of n since the duplication and print cost depends on the size of n

the total cost n*n which is n^2 since you the entire function depends on n times to run the total amount of times


 def print_triangle(n):
    for i in range(1,n+1):
    line = '*' * i
    print(line)

prints out a triangle instead of a square meaning the runtime is different


def f(n):
    for i in
        for j in
            for k in

the time cost inside would be theta(i) since it relies oni for the duplications

the total cost would be n^2, similar to the cost of the first function since if you add the entire cost it comes up to n^2

'''