import ctypes  # provides low-level arrays


def make_array(n):
    return (n * ctypes.py_object)()


class ArrayList:
    def __init__(self, iterable_collection=None):
        self.data_arr = make_array(1)
        self.capacity = 1  # actual size of array
        self.n = 0  # digital size

        if iterable_collection is not None:  # if the iterable collection is passed, run this part of the code
            for elem in iterable_collection:  # for each element found in the iterable collection, append each of those
                # elements to the array
                self.append(elem)  # again, we are setting the values here NOT returning anything!

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

    def __getitem__(self, ind):
        if not (- self.n <= ind <= self.n - 1):  # negative indices become -5 to -1 instead of 0 to 4
            raise IndexError('invalid index')
        if ind < 0:
            ind = self.n + ind  # for instance, if self.n is 5 and the index we use is -1
            # we then get ind 4 which if the index is from 0 to 4, this would give the last value in the lst
        return self.data_arr[ind]

    def __setitem__(self, ind, val):
        if not (-self.n <= ind <= self.n - 1):
            raise IndexError('invalid index')
        if ind < 0:
            ind = self.n + ind  # same implementation since the only thing changing is the index position
        self.data_arr[ind] = val

    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  # could also yield self[i]

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)

    def __repr__(self):
        pass

    def __add__(self, other):
        lst = ArrayList()  # make an empty lst to hold the new values since arrays are fixed sizes and we need more space
        lst += self  # adding the new elements into the empty lst
        lst += other  # adding the other elements into the empty lst

    def __iadd__(self, other):
        self.extend(other)  # since we want add more elements to the original lst, we use extend to help us
        return self

    def __mul__(self, scalar):  # this method would allow the duplication of the lst over and over to a new lst
        lst = ArrayList()
        for i in range(scalar):  # this is how many times the lst will be duplicated since it depends on the scalar
            lst.extend(self)  # each time the range happens, lst.extend will occur with the data found in self
        return lst  # when completed, return the entire lst

    def __rmul__(self, scalar):
        return self * scalar

    def remove(self, val):
        i = 0

        while i < self.n and self[i] != val:
            i += 1

        while i < self.n - 1: # negative indices
            self[i] = self[i+1]
            i += 1
        if i < self.n: #i should be in the last index (len - 1). The condition is if i is still within range/ list is not empty.
            self[i] = None
            self.n -= 1

    #we've actually done this before with move_zeroes in Lab 3
    def removeAll(self, val):

        #first move all instances of val to the back
        last_val = 0                   #keep track of the last zero
        for i in range(len(self)):      #use i to traverse through the list,
            if self[i] != val:            #if lst[i] != 0, swap, then move the last zero reference up
                self[i], self[last_val] = self[last_val], self[i]
                last_val += 1

        while self[i] == val:
           self[i] = None
           i -= 1
           self.n -= 1 #don't forget to decrement the size