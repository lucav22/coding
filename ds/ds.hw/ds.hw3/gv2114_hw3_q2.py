import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data_arr[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data_arr[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'


    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times

    def insert(self, index, val):
        if not (-self.n <= index <= self.n):  # similar implementation to set item
            # to take account of positive and negative index
            raise IndexError("Invalid index")
        if index < 0:
            index = self.n + index  # in case of negative index being set to the right position
        if self.n == self.capacity:  # if the amount of digital items are the same as physical items
            # then we call the resize function to increase the size
            self.resize(2 * self.capacity)
        for i in range(self.n, index, -1):  # shifting the elements to make room for the value
            # and the shifting starts from the end to the index where the insert is going to happen
            # ex. [10,20,30,40,50] index 2 , [10,20,30,40,50,50,_,_,_,_] since the array was doubled
            # so then [10,20,30,40,40,50] etc.....
            self.data_arr[i] = self.data_arr[i - 1]

        self.data_arr[index] = val  # there is a "space" created for the value and no value will be lost
        self.n += 1

    def pop(self, index=None): #exam 1 question
        if index is None:
            index = self.n - 1  # since we are going to pop the last value
        if not (-self.n <= index < self.n):
            raise IndexError("Invalid index")
        if index < 0:
            index = self.n + index

        element = self.data_arr[index]
        # either the element we are going to pop is to be the last value
        # or the specific that was provided

        for i in range(index, self.n - 1):  # same as length
            self.data_arr[i] = self.data_arr[i + 1]  # same approach as insert since we need to shrink down lst

        self.data_arr[self.n - 1] = None  # no matter what, the final value will be deleted
        self.n -= 1  # shrink down the amount of data

        if self.n < self.capacity // 4: #as mentioned in the problem, if the amount of items
            # is less than the capacity is a quarter of it, then we resize it by half
            self.resize(self.capacity // 2)

        return element
