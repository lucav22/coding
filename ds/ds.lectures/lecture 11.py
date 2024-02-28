'''


def count_down(start, end):
    if (start == end):
        print(end)
    else:
        print(end)
        count_down(start, end-1)

we make sure to print(end) to get the current end value and then shrinking the range to start counting down until


def count_up_and_down(start, end):
    if (start == end):
        print(end)
    else:
        print(start)
        count_up_and_down(start+1, end)
        print(start)

def factorial(n):
    if(n==1):
        return 1
    else:
        rest_fact = factorial(n-1)
        return rest_fact * n

equation for a factorial (n-1) * n


utilize a recursion tree to see the total cost of the recursion call, we need to add up all the costs of calling the
recursive function to see the total cost of the function

def count_appearances1(lst,val):
    if (len(lst) == 0):
        return 0
    else:
        rest_count =  count_appearances1(lst[1:] , val)
        if (lst[0] == val):
            return rest_count + 1
        else:
            return rest_count


def count_appearances2(lst, low, high, val):
    if (low == high):
        if (lst[low] == val):
            return 1
        else:
            return 0
    else:
       rest_count =  count_appearances2(lst, low + 1, high, val)
        if (lst[low] == val):
            return rest_count + 1
        else:
            return rest_count


it will will slice the lst into a smaller sub lst that will check for the values




'''