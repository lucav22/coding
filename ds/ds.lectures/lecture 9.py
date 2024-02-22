"""

important sums

1+2+3+4.....n = theta(n^2)
1+2+3+4.....log(n) = theta(log(n))
1+2+4+8 .... 2^n+1 = theta(2^n)
1+2+4+8 ..... n = 2n - 1 =  theta(n)

Amortized analysis, finding the total cost of a series of operation considering the cost and define the amortized cost
total cost of the entire series / n

import ctypes
def make_array(n):



class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.n = 0
        self.capacity = 1


    def __len__(self):
        return self.n

    def append(self,val):
        if(self.n == self.capacity): reaches the full capacity of data
            self.resize(2* self.capacity)
        self.data_arr[self.n] = val self.n goes into the next available slot
        self.n += 1 increases the logical size of the array

    def resize(self, new_size):
        make_array(new_size)
        for i in range(self.n):
            new_arr[i] = self.data_arr[i]
        self.data_arr = new_arr
        self.capacity = new_size


"""