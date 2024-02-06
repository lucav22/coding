# a
def square_sum(n):
    final = 0
    for i in range(n):
        final += i ** 2
    return final


# b
# [(thing to be stored ) for (element) in (iterable collection) if (condition)]
def square_sum_v2(n):
    return sum(i ** 2 for i in range(n))


# c
def square_sum_odd(n):  # just an additional statement for the odd values only!
    final = 0
    for i in range(n):
        if i % 2 == 1:
            final += i ** 2
        else:
            pass
    return final


# d
def square_sum_odd_v2(n):
    return sum(i ** 2 for i in range(n) if i % 2 == 1)


print(square_sum(10))
print(square_sum_v2(10))
print(square_sum_odd(10))
print(square_sum_odd_v2(10))
