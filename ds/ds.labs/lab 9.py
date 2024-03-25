from ArrayStack import ArrayStack

# Q1, see vitamin q3. Want to keep elements in stack the same
def stack_sum(s):
    if len(s) == 0:
        return 0
    else:
        val = s.pop()
        curr_total = stack_sum(s)
        curr_total += val
        s.push(val)
        return curr_total

class MeanStack:
    def __init__(self):
        self.data = ArrayStack()



# Q3
'''
the idea is to use the stack to store the int values in reverse order

start from the back because stack reverses the order and it's more efficient to remove from the back than it is from the front
is the last elem a list? if so, pop it and extend it back onto the list
is the last elem an instead? if so, store it into the stack

repeat this until the list is empty
then pop all values from the stack and add them back onto the list

'''


def flatten_lst(lst):
    stack = ArrayStack()

    while len(lst) != 0:
        val = lst.pop()  # get the last value
        if isinstance(val, list):  # is it a list?
            lst.extend(val)  # extend it back # for loop of appends

        else:  # it's an int, its already flattened
            stack.push(val)

    while not stack.is_empty():
        lst.append(stack.pop())  # remove the values from the stack and place back into the list


# Q4
'''
the idea is to store to have the other stack store the values in descending order
ex stack top <-> bottom

s = [1, 5, 8, 2, 5, 9, 2]

helper = [1] 
helper = [5, 1]     5 > 1
helper = [8, 5, 1]  8 > 5
helper = [8, 5, 1]  2 > 8 is false, store 2 in temp var

put the values from helper back onto stack until temp > helper.top()
helper = [5, 1]
helper = [1] 2 > 1 so we can put the value of temp onto the helper stack now
helper = [2, 1]

repeat this process
heleper = [5, 2, 1]
helper = [8, 5, 2, 1]
... so on 

'''

def stack_sort(s):
    helper = ArrayStack()

    while not s.is_empty():
        temp = s.pop()

        while (not helper.is_empty()) and temp < helper.top():
            s.push(helper.pop())

        helper.push(temp)

    while not helper.is_empty():
        s.push(helper.pop())

