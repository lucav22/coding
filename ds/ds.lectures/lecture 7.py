'''

def prefixaverage(lst):

res_lst = []
for i in
rest_lst.appemd()
return res_lst

mutated the new lst object and we do not wanna use append since we do not know what is being added very iteration

def prefix_average(lst):
    n = len(lst) this is theta (n)
    res_lst = [0] * n with the same size as the length of the lst theta(n)
    for i in range(n): this costs n^2 since when it gets to n it will run n (i) in the block
        curr_sum = sum(lst[:(i+1]) basically slice the lst until the i parameter that was mentioned and then sum the values
        all together until the slice AGAIN i+1 since i starts at 0
        the value of this in time is theta(i)
        curr_avg = curr_sum / (i+1) since i is starting at 0 so we add 1 to make sure its in line
        res_lst[i] = curr_avg the average value found is then indexed to the res_lst in order
        the entire block is theta(i) since its not like math and instead addition so its just adding to i
    return res_lst constant time theta(1)

def prefix_average(lst):
    n = len(lst)
    res_lst = [0] * n
    curr_sum = 0
    for i in range(n): linear time now since range will increase will be 1+1+1+1 instead of 1+2+3+n due to curr_sum
    not being ran every single time
        curr_sum += lst[i] since we dont wanna keep running a new curr_sum, we can now just add it to the pre-exisiting
        curr_sum so it dosent have issue running
        curr_avg = curr_sum / (i+1)
        rest_lst[i] = curr_avg
    return res_lst

searching problem

def linear_search(lst,val):
the function should return an index where the value appears or NONE if its not present


def linear_search(lst,val):
    for i in range(len(lst)): the inside of the for loop it is constant however the for loop is not the expected
    runtime value
        if (lst[i] == val) check the index of the lst and the value to see if its working and if it does
        then return the index of i
            return i
    return NONE

we just wanna find the value if it appears once, so that means it will iterate over and over the whole thing

the worst time would be theta n if it needs to check the entire lst, but if it only does it one time, then it will be c
constant time


def sorted_search(sort_lst , val):

tge function is given a sorted lst and the val, will return the index of the value where it is found

if we follow the approach where we check every single value, the worst case would be theta(n)

a better way to approach this problem is to find the mid point of the lst, then see if we need to go higher of lower,
cut it in the middle, then again find the mid point, cut it in the middle, and once more until you find it


def binary_search(srt_lst, val):



'''