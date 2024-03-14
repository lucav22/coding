def print_triangle(n):
    if n == 1:
        print('*')
    else:
        print_triangle(n - 1)  # will recurse until the smallest value which will be 1 and that will print out
        line = n * '*'  # the value of n will be multiplied by the amount of stars present
        print(line)  # print out the current line present


def print_opposite_triangles(n):
    if n == 1:
        print('*')
        print('*')
    else:
        line = n * '*'
        print(line)
        print_opposite_triangles(n - 1)  # needs to add another start to initiate the second recursive call
        print(line)


def print_ruler(n): # similar approach to other recursions calls
    if n == 1:
        print('-')
        return

    print_ruler(n - 1) # ensures that the first half is done accordingly

    print('-' * n) # multiplies the dashes by the current amount of n

    print_ruler(n - 1) # once that half is dones, the bottom half is done, and the middle point is
    # the starting point for this bottom half



