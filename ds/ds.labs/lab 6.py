'''
# QUESTION 1
# Write a recursive function that returns the sum of all numbers from 0 to n. (5 minutes)
def sum_to(n):
    # base case
    if n < 0:
        return 0

    # recursive case
    return n + sum_to(n-1)


# QUESTION 2
# Write a recursive function that returns the product
    # of all even numbers from 1 to n.
def product_evens(n):
    # base case
    if n <= 1:
        return 1

    # recursive case
    if n % 2 == 0: # is even
        return n * product_evens(n-1) # or you can just do product_evens(n-2) because,
                                        # even - 2 is always even so you'll never get odd
    else:
        return product_evens(n-1)


# QUESTION 3
# Write a recursive function to find the maximum element in a non-empty, non-sorted list of numbers.
def find_max(lst, low, high):
    # base case
    # 1 element list, by definition it must be the max
    if low == high:
        return lst[low]  # or lst[high] since they are the same

    # recursive case
    curr_max = find_max(lst, low + 1, high)  # the idea is to get the curr max from the next recursive call

    # update the curr_max appropriately
    if lst[low] > curr_max:
        curr_max = lst[low]
    return curr_max

# [13, 9, 16, 3, 4, 2], curr_max = find_max([9, 16, 3, 4, 2])

# QUESTION 4
# Write a recursive function to determine if a string is a palindrome.
def is_palindrome(str, low, high):
    # base case
    # 0 length or 1 length string, by definition must be a palindrome
    if low >= high:
        return True

    # recursive case
    elif str[low] != str[high]:  # check current letters at the ends
        return False  # not a palindrome, return False
    return is_palindrome(str, low+1, high-1)  # otherwise, check the inside string
    # alternatively
    # return str[low] == str[high] and is_palindrome(str, low+1, high-1)


# QUESTION 5
# Give a recursive implementation for the binary search algorithm.
Given the binary search with while loop
while low <= high: # exit if low > high
    mid = (low + high)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return None


def binary_search(nums, target, low, high):
    # base case
    # index out of bounds, exit
    if low > high:
        return None

    # recursive case
    mid = (low + high)//2  # calculate midpoint
    if nums[mid] == target:  # found the target, return mid
        return mid

    # update low and high
    elif nums[mid] < target:
        return binary_search(nums, target, mid+1, high) # low = mid + 1
    else: # nums[mid] > target
        return binary_search(nums, target, low, mid-1) # high = mid - 1


# QUESTION 6
# Given a string of letters representing a word(s), write a recursive function that returns
# a tuple of 2 integers: the number of vowels, and the number of consonants in the word.
def vc_count(word, low, high):
    # base case
    # 0 length word, no vowels or consonants
    if low > high:
        return (0,0)

    # recursive case
    # get the number of vowels and consonants from the string after the current letter
    vowels, consonants = vc_count(word, low+1, high)

    # update the number of vowels and consonants
    if word[low] in "aeiouAEIOU":  # is a vowel
        vowels += 1
    else: # not a vowel
        consonants += 1
    return (vowels, consonants)


# QUESTION 7
# Given a list of integers, write a function to print the sum triangle of the array.
def list_sum_triangle(lst):
    if len(lst) >= 1:
        temp = lst.copy() # make a copy for printing the current list
        # for i in range(len(lst)-1): # same thing as the sum_row
        # lst[i] += lst[i+1]
        sum_row(lst, 0, len(lst)-1) # modify the list
        lst.pop() # get rid of the last element
        list_sum_triangle(lst)
        print(temp)
def sum_row(lst, low, high):
    if low < high:
        lst[low] += lst[low + 1]
        sum_row(lst, low+1, high)

'''


def sum_to(n):
    if n < 0:  # to account for negative numbers
        return 0
    else:
        return n + sum_to(n - 1)  # add the value of n so it is not lost before the recursive call is called


def product_evens(n):
    if n < 1:  # to account for anything after 1 since that is where we start
        return 1

    if n % 2 == 0:
        return n * product_evens(
            n - 1)  # u wanna make sure that the recursive call is not the one that calls the division
    # of the numbers and instead its a separate if statement
    else:
        return product_evens(
            n - 1)  # as a result, if the number is even then u wanna include it as a apart of the product
    # if its not, then its going to the else statement to jump to the next number


'''
def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    prev = find_max(lst[1:]) # slicing will slow down the implementation on each run, and as a result cause a quadratic
    # runtime
    if prev > lst[0]:
        return prev
    return lst[0]
'''


def find_max(lst, low, high):
    if low == high:
        return lst[low]

    curr_max = find_max(lst, low + 1, high)  # recursive function to slice the lst and take the first element
    # of each new lst

    if lst[low] > curr_max:  # check the current low index and see if its greater than the next index found in the
        # curr_max call, if it is, then curr_max will be set to the current lst_low value, if it is not then curr_max
        # will remain unchanged
        curr_max = lst[low]
    return curr_max


def is_palindrome(str, low, high):
    if low >= high:
        return True  # if the low value matches is greater than the high value, that means the current size of the string
    # is either 0 or 1 since that is the lowest possible value for a base case which means that it is a palindrome

    elif str[low] != str[high]:  # if the ends of the str at the current moment are not equal then clearly it is not a
        # palindrome ex racecar
        return False
    return is_palindrome(str, low + 1, high - 1)  # we call for the recursion steps to keep occuring


'''
while low <= high: # exit if low > high
    mid = (low + high)//2
    if lst[mid] == target:
        return mid
    elif lst[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
return None
'''


def binary_search(lst, low, high, val):
    if low > high:
        return None

    mid = (low + high) // 2
    if lst[mid] == val:
        return mid
    elif lst[mid] < val:
        binary_search(lst, mid + 1, high, val)
    else:
        binary_search(lst, low, mid - 1, val)
    # the code is basically the same thing as binary search as it will just recurse over the same funciton over and
    # shrinking the viewing window until it finds the appropiate value


def vc_count(word, low, high):
    if low > high:
        return (0, 0)  # there are no vowels or constanants present since low and high are the ranges of the word

    vowels, consonants = vc_count(word, low + 1, high) # we take the total amount of vowels and consonants at each
    # iteration as a tuple, not updating a previous one since they are immutable but instead getting a new tuple at each
    # run

    if word[low] in "aeiouAEIOU":
        vowels += 1
    else:
        consonants += 1
    return (vowels, consonants)
