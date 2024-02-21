def factors(num):
    for index in range(1, int(num ** 0.5) + 1):  # halfway point is the square root instead
        if index == 1:
            yield 1
        elif num % index == 0:  # if the remainder is 0 meaning that the division
            # is set correctly
            yield index  #here the index is yielded since it was checked if the remainder
            # is 0
    for index in range(int(num ** 0.5) - 1, 0, -1):  # splitting it in half for the other end
        # that way the total cost is less
        if num % index == 0:
            yield num // index # here the result of the division is the value yielded
            # since we found all the index values and now we want the second half which is now the result
            # of the value with the index

for curr_factors in factors(100):
    print(curr_factors)
