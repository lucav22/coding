'''


def positive_integers_list(n):
    if (n==1)
        return [1]
    else:
        res_lst = positive_integers_list(n-1) recursive call to continue the call
        res_lst.append(n) adds the missing value itself to the end so that the lst is complete
        return res_lst returning the actual lst instead of the append line

        even though the multiple calls to append for each recursive call, the total runtime will still be theta n
        added with the constant time as well

def power(a, n):
    if (n==1):
        return a
    else:
        res_power = power(a,n-1) since the sequence of the exponent is a ^n-1 which gives the appropiate sequence
        we just need to find multiplication of the entire sequence by a
        return res_power * a

def fast_power(a, n):
    if (n==1):
        return a
    else:
        part1 = power(a, n//2)
        part2 = power(a, n//2) floor division since they will be whole numbers
        if (n % 2 == 0 ):
            return part1 * part2 if this is even
        else:
            return part1 * part 2 * a if its odd then u multiply by another a

        the runtime is 2^log*n as each level the amount of calls increases exponentially which is equal to n and the
        total cost of 2n - 1, geometric sum which is the same as theta of n


    instead here we need to consider the even and odd instances

def real_fast_power(a , n):
   if (n==1):
        return a
    else:
        part = real_fast_power(a, n//2)
        if (n % 2 == 0 ):
            return part * part if this is even
        else:
            return part * part * a if its odd then u multiply by another a

    we get a singular branch instead of multiple branches that slow down the growth of the function


selection sort consists of finding the smallest possible value and put it first

'''