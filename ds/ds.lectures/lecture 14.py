'''

we need to consider how to separate strings from the functions
and then make sure that each have the functions that is related to them
the string works as an array and each take a step for the following values
each item will be a single token instead of worrying about spaces


from stacks import
def eval_postfix_exp(exp_str):
    operators = '+-*/'
    exp_lst = exp_str.split() # the integers are made into strings by this function by the spaces
    arguments_stack = ArrayStack()

    for token in exp_lst:
        if (token not in operators):
            arguments_stack.push(int(token)) # adds the number into the stack as an int
        else:
            arg2 = arguments_stack.pop() #removes the value at the top and removes it
            arg1 = arguments_stack.pop() #same here
            if (token == "+"):
                res = arg1 + arg2
            elif(token == '-'):
                res = arg1 - arg2
            elif(token == '*'):
                res = ar1 * arg2
            else:
                if (arg2 == 0):
                    raise ZeroDivisionError("")
                res = arg1 / arg2
            arguments_stack.push(res) # adds result to the top of the stack
    return arguments_stack.pop() #the last thing found in the stack, will be removed as it has gone through
    the entire lst


    Queue ADT
    First in First out!






'''