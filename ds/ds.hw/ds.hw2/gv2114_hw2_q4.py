def e_approx(n):
    factorial = 1
    total_sum = 1  # the initial sum is always 1, the rest comes from the n value
    for index in range(1, n + 1):
        factorial *= index  # the current factorial being the result of the product between the index
        # and factorial value
        total_sum += 1 / factorial
    return total_sum


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n=", n, 'Approximation:', approx_str)


main()
