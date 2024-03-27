'''

import ctypes
def make_array(n):...


class StaticArrayQueue:
    def __init__(self, max_cap):
        self.data = make_array(max_cap)
        self.n = 0
        self.capacity = max_cap
        self.first_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def enqueue(self, item):
        if (self.is_full()):
            raise Exception('Queue is full')
        if (self.is_empty()): # making a new queue so that there is no error
            self.data[0] = item
            self.first_ind = 0
            self.n += 1
        else:
            back_ind  = (self.first_ind + self.n) % self.capacity # find out the current placement with mod
            self.data[back_ind] = item
            self.n += 1

    def first(self):
        if (self.is_empty()):
            raise Exception('Queue is empty')
        return self.data[self.first_ind] #returning the first item from the queue

    def dequeue(self):
        if (self.is_empty()):
            raise Exception('Queue is empty')
        res = self.data[self.first_ind]
        self.first_ind = (self.first_ind + 1) % self.capacity # since this is a queue, once the item is taken out, then the following item
        # becomes the queued item and making sure that the circular implementation is kept
        self.n -= 1
        if (self.n == 0):
            self.first_ind = None # this is in case its the end of the queue
        return res
** Modulus gives the REMAINDER!! so something like 6 % 8 would give you 6 since there is no divisor and just
** returns the number by itself

class StaticArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data = make_array(Array.Queue.INITIAL_CAPACITY)
        self.n = 0
        self.capacity = Array.Queue.INITIAL_CAPACITY
        self.first_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def is_full(self):
        return (len(self) == self.capacity)

    def enqueue(self, item):
        if (len(self) == self.capacity):
            self.resize(
        if (self.is_empty()): # making a new queue so that there is no error
            self.data[0] = item
            self.first_ind = 0
            self.n += 1
        else:
            back_ind  = (self.first_ind + self.n) % self.capacity # find out the current placement with mod
            self.data[back_ind] = item
            self.n += 1

    def first(self):
        if (self.is_empty()):
            raise Exception('Queue is empty')
        return self.data[self.first_ind] #returning the first item from the queue

    def dequeue(self):
        if (self.is_empty()):
            raise Exception('Queue is empty')
        res = self.data[self.first_ind]
        self.first_ind = (self.first_ind + 1) % self.capacity # since this is a queue, once the item is taken out, then the following item
        # becomes the queued item and making sure that the circular implementation is kept
        self.n -= 1
        if (self.n == 0):
            self.first_ind = None # this is in case its the end of the queue
        if (len(self) < (self.capacity // 4)):
            self.resize(self.capacity // 2)
        return res

    def resize(self, new_size):
        new_data = make_array(new_size) # make new array
        old_in = self.first_ind # the old start index of the queue
        for new_ind in range(self.n): # updating the new queue with taking each data from the previous queue
            new_data[new_ind] = self.data[old_ind]
            old_in = (old_in + 1) % self.capacity # circularly

'''