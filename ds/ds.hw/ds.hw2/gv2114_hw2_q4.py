def e_approx(n):
    factorial = 1
    for index in range(1, n + 1):
        if index == 1:
            return 1
        else:
            factorial = 1/(factorial * index)
    return factorial


def main():
    for n in range(15):
        curr_approx = e_approx(n)
        approx_str = "{:.15f}".format(curr_approx)
        print("n=", n, 'Approximation:', approx_str)
