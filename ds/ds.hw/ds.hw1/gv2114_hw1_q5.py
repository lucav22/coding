def fibs(n):
    a, b = 1, 1  # starting point is 1,1 as stated in the hw instructions
    for i in range(n):
        yield a
        a, b = b, a + b  # this switches the place of b with as it moves up and
        # the new spot of b is taken up by the addition of the current numbers


