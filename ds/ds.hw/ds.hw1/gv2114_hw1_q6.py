class Vector:
    def __init__(self, d):
        if isinstance(d, int):
            self.coords = [0] * d
        elif isinstance(d, list):
            self.coords = d.copy()  # makes a copy of the original passed through
            # since its really a lst

        # generates an empty list with the amount of
        # passed characters in a dimensional space

    def __len__(self):
        return len(self.coords)  # return the amount of items in the vector

    def __getitem__(self, j):
        return self.coords[j]  # get the specific item in the created vector

    def __setitem__(self, j, val):
        self.coords[j] = val  # with the given vector, specify the number given
        # and change with the provided index

    def __add__(self, other):
        if len(self) != len(other):  # dimensions must agree given vector characteristics
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # makes a new vector object with the length of the self object
        # since they need to have the same dimensions
        for j in range(len(self)):  # for the amount of items in the length in range of self
            result[j] = self[j] + other[j]  # takes the index of self and other adds it to the index
            # of the new vector object and there is no error since there all the same size
        return result

    def __eq__(self, other):
        return self.coords == other.coords  # check if the lst has the same items

    def __ne__(self, other):
        return not (self == other)  # check if the vectors are not equal

    def __str__(self):
        return '<' + str(self.coords)[1:-1] + '>'  # a typical slice that removes the first and last items
        # so that means for the vector, it only takes the value inside the lst

    def __repr__(self):
        return str  # the function provided in the previous statement

    def __sub__(self, other):  # similar implementation to add
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __neg__(self): #same here to add
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -(self[j])
        return result

    def __mul__(self, other): #relies on rmul to handle the other instances
        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        elif isinstance(other, Vector):
            final_sum = 0
            for i in range(len(self)):
                final_sum += self[i] * other[i]
            return final_sum

    def __rmul__(self, other):
        return self.__mul__(other)
