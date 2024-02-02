'''class Polynomial:
    def __init__(self, lst):
        self.data = lst

    def __call__(self, val):
        """
        total = 0
        for i in range(len(self.data)):
            total += (val**i)*self.data[i]
        return total
        """
        # val = x,  x^power * coefficient
        return sum([(val**i)*self.data[i] for i in range(len(self.data))])

    def __add__(self, other):
        lst = self.data.copy()
        temp = other.data.copy()

        if len(lst) > len(temp):
            lst, temp = temp, lst # have lst be the shorter one

        while len(lst) < len(temp): # extend lst (the shorter one) with 0's
            lst.append(0)

        lst = [lst[i] + temp[i] for i in range(len(lst))]

        return Polynomial(lst)

    #OPTIONAL

    def __repr__(self):
        return " + ".join([f"{self.data[i]}x^{i}" for i in range(len(self.data)-1, -1, -1)])

    def __mul__(self, other):
        lst = [0]*(len(self.data) + len(other.data)-1)

        for i in range(len(self.data)):
            for j in range(len(other.data)):
                lst[i+j] += self.data[i] * other.data[j]

        return Polynomial(lst)

    def derive(self):
        for i in range(1, len(self.data)):
            self.data[i - 1] = self.data[i]*(i)
        self.data.pop()



#TEST CODE
poly1 = Polynomial([3, 7, 0, -9, 2]) #2x^4 -9x^3 + 7x + 3
poly2 = Polynomial([2, 0, 0, 5, 0, 0, 3]) # 3x^6 + 5x^3 + 2

poly3 = poly1 + poly2
print(poly3.data) #[5, 7, 0, -4, 2, 0, 3]

print(poly1(1)) #3
print(poly2(1)) #10
print(poly3(1)) #13 (result of 3 + 10 == poly1(1) + poly2(1))

print(poly1(2)) #-23
print(poly2(2)) #234
print(poly3(2)) #211 (result of -23 + 234 == poly1(2) + poly2(2))

print(poly1)
poly1.derive()
print(poly1)
poly1.derive()
print(poly1)

p1 = Polynomial([1, 1])
p2 = Polynomial([2, 1])
p3 = p1 * p2
print(p3)

class UnsignedBinaryInteger:
    def __init__(self, bin_num_str):
        self.data = bin_num_str

    #reused code from lab 1
    def __add__(self, other):
        result = ""
        carry = 0

        max_length = max(len(self.data), len(other.data))

        #sign extension so both will have same length
        b1 = (max_length - len(self.data))*'0' + self.data
        b2 = (max_length - len(other.data))*'0' + other.data


        for i in range(1, max_length + 1):
            #we will use the negative indices since we evaluate from right to left
            sum_bits = int(b1[-i]) + int(b2[-i]) + carry
            result = str(sum_bits % 2) + result

            #can replace this with carry = sum_bits >= 2
            if sum_bits < 2:
                carry = 0
            else:
                carry = 1 #if sum of the bits + carry >= 2, then carry = 1

        result = carry*'1' + result

        return UnsignedBinaryInteger(result)

    def decimal(self):
        value = 0
        for i in range(len(self.data)):
            value += int(self.data[i]) * 2** (len(self.data) - 1 -i)
        return value
        #one line comprehension syntax
        #return sum(int(self.data[i]) * 2** (len(self.data) - 1 -i) for i in range(len(self.data)))

    #self < other
    def __lt__(self, other):
        #more digits = greater value. longer the str = more digits
        if len(self.data) < len(other.data):
            return True

        elif len(self.data) > len(other.data):
            return False

        #same number of digits
        for i in range(len(self.data)):
            if self.data[i] != other.data[i]:
                return self.data[i] == '0' #if both not equal, that means one bin num has a 1, other has a 0
                                           #if self has a 0, that means its the smaller one

        return False #no differences in digits detected

    #self > other
    def __gt__(self, other): #self > other == other < self
        return other < self

    #self == other
    def __eq__(self, other): #only way to have equal value is to have same bin num str for data
        return self.data == other.data
        # alternatively
        # return not (self < other or self > other) #if self is not less than other and not greater than other, then they must be equal


    def is_twos_power(self):
        #recall that the only way for a bin_num to be 2's power is if only the first digit is 1 and the rest are 0's

        #skip the first digit and check the remaining digits. If any are 1, then it is not a 2's power
        for i in range(1, len(self.data)):
            if self.data[i] == '1':
                return False

        return self.data[0] == '1' #ensure 1 is the first digit


    def largest_twos_power(self):
        #this is a more intuitive solution
        if self.data[0] == '0':
            raise Exception("No twos power for 0")
        largest_sum = 1
        value = self.decimal()

        while largest_sum*2 <= value:
            largest_sum *= 2

        return largest_sum


    def __repr__(self):
        return f"0b{self.data}"



    #OPTIONAL
    #CODING PART 4
    #use 0 for sign extension
    def __and__(self, other):
        result = ""

        shorter = self.data
        longer = other.data

        if longer < shorter:
            shorter, longer = longer, shorter #swap


        10011 --> 10011
        100   --> 00100, sign extension
                    000 --> result = 0

        we only need to check as many digits as there are for the shorter one
        we can sign extend the shorter one to 0, but since 0 and with 0, 1 == 0, we don't need to bother with 10, and only compare 011 with 100

        it is also okay to just do the sign extension and attach the excess 0's as they will be removed in the while loop below


        for i in range(len(shorter)):
            #make sure to account for the difference in length

            #can replace this if/else with result += int(shorter[i] == '1' and longer[i + len(longer) - len(shorter)] == '1')
            if (shorter[i] == '1' and longer[i + len(longer) - len(shorter)] == '1'):
                result += '1'
            else:
                result += '0'

        while len(result) > 1 and result[0] != '1': #get rid of excess leading 0's
            result = result[1:]

        return UnsignedBinaryInteger(result)



    def __or__(self, other):
        result = ""
        max_length = max(len(self.data), len(other.data))
        #sign extension so both will have same length
        b1 = (max_length - len(self.data))*'0' + self.data
        b2 = (max_length - len(other.data))*'0' + other.data


        10011 --> 10011
        100   --> 00100, sign extension
                  10111 --> result = 0

        in the case of or, it is easier to use sign extension


        for i in range(max_length):

            #can replace this if/else with result += int(b1[i] == '1' or b2[i] == '1')
            if b1[i] == '1' or b2[i] == '1':
                result += '1'
            else:
                result += '0'

        while len(result) > 1 and result[0] != '1': #get rid of excess leading 0's
            result = result[1:]

        return UnsignedBinaryInteger(result)



#TEST CODE pt. 3

b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')

print("b1 is: ", b1)
print("b2 is: ", b2)

b3 = b1 + b2
print("b3 is: ", b3)


print("\nChecking decimal values:\n")
print(b1.decimal())
print(b2.decimal())
print(b3.decimal())


print("\nChecking comparisons:\n")
print(b1 < b2)
print(b2 < b1)

print(b1 > b2)
print(b2 > b1)
print(b1 + b2 == b3)


print("\nChecking is_twos_power:\n")
print(b1.is_twos_power())
print(b2.is_twos_power())
print(b3.is_twos_power())

print("\nChecking largest_twos_power:\n")
print(b1.largest_twos_power())
print(b2.largest_twos_power())
print(b3.largest_twos_power())



#TEST CODE pt. 4


b1 = UnsignedBinaryInteger('10011')
b2 = UnsignedBinaryInteger('100')
print("\nTesting b1: ", b1, "b2: ", b2)

b3 = b1 | b2
b4 = b1 & b2

print(b1, "|", b2, "=", b3)
print(b1, "&", b2, "=", b4)


b1 = UnsignedBinaryInteger('1010')
b2 = UnsignedBinaryInteger('1001')
print("\nTesting b1: ", b1, "b2: ", b2)

b3 = b1 | b2
b4 = b1 & b2

print(b1, "|", b2, "=", b3)
print(b1, "&", b2, "=", b4)'''

import copy


def powers_of_two(n):
    curr = 1
    for i in range(n + 1):  # for each value of the curr is being added to yield the power of 2
        yield pow(curr, 2)
        curr += 1


class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        original_lst = copy.deepcopy(self.coefficients)
        other_lst = copy.deepcopy(other.coefficients)

        if len(original_lst) < len(other_lst):
            while len(original_lst) < len(
                    other_lst):  # ensures that if the lsts are not the same lenght, keep running until
                # they become teh same size
                original_lst.append(0)
        elif len(other_lst) < len(original_lst):
            while len(other_lst) < len(original_lst):
                other_lst.append(0)
        else:
            pass

        # list comprehension [(thing to be stored) for (element) in (iterable collection) if (condition)

        new_lst = [original_lst[i] + other_lst[i] for i in range(len(original_lst))]  # both index of the lst are addded
        # together for the index provide in the range of the lst

        return Polynomial(new_lst)

    def __call__(self, param):
        total = 0
        for i in range(len(self.coefficients)):
            mult = self.coefficients[i]  # becomes the coefficient value found in that specific index
            total += mult * pow(param, i)  # all being multiplied by the power of the param passed by the current index
            # in the lst since its reversed so it will start at 0 and then continue
        return total


class UnsignedBinaryInteger:
    def __init__(self, num_str):
        self.num_str = num_str

    def __lt__(self, other):
        if len(self.num_str) < len(other.num_str):
            return True
        else:
            return False

    def __gt__(self, other):
        if len(self.num_str) > len(other.num_str):
            return True
        else:
            return False

    def __eq__(self, other):
        if self.num_str == other.num_str:
            return True
        else:
            return False

    def is_two_powers(self):
        if self.num_str == "0000":
            return False
        else:
            return True

    def largest_two_powers(self):
        start = 0
        base = 0
        for i in range(len(self.num_str)): #
            position = self.num_str[i]
            if position == 1:
                temp = 2 * pow(1, base)
                start += temp
                base += 1
            else:
                base += 1
                pass
        return start

    def __repr__(self):
        return f'0b{self.num_str}'
