# [(thing to be stored ) for (element) in (iterable collection) if (condition)]
# [x for x in range(5)]
# a
print([10 ** i for i in range(6)])  # since its multiples of 10, you iterate
# the power over the range of 5 and that will only print out the values needed

# b
print([(i + 1) * i for i in range(10)])  # multiplies the current value step with an
# offset index position of the current value so 2 would come from the index being 1 +1 * the range
# value being 1

# c
print([chr(i) for i in range(97, 123)]) # goes through the ASCII values of each letter
# and returns the responding chr due to the purpose of the function chr()
