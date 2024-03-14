def print_triangle(n):
    if n == 1:
        print('*')
    else:
        print_triangle(n - 1)  # will recurse until the smallest value which will be 1 and that will print out
        line = n * '*'  # the value of n will be multiplied by the amount of stars present
        print(line)  # print out the current line present


def print_opposite_triangle(n):
    if n == 1:
        print('*')
    else:
        line = n * '*'
        print(line)
        print_opposite_triangle(n - 1)  # needs to add another start to initiate the second recursive call
        print(line)


def print_ruler(n):
    if n == (2 ** n - 1):
        print('-')
    else:
        line = n * ''


print_triangle(4)
print_opposite_triangle(4)
