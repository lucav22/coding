'''

import copy
lst1 = [1,2,3,4]
lst2 = copy.copy(lst1)

shallow copy or regular copy creates a new copy of the lst with the same content as they share the same values

lst1 = [1,2,3,4]
lst2 = copy.deepcopy(lst1)

deep copy also creates another lst object but instead the content is copied as well instead of being shared

import copy
lst1 = [1,2,3,4]
lst2 = copy.copy(lst1)
lst2[0] = 10

lst1

the original list will still remain the same but lst2 will be different since index 0 will now hold a 10



lst1 = [1,[2,3],4]
lst2 = copy.copy(lst1)

since its a shallow copy lst2 will be referencing all of the objects and data mentioned in lst1

lst1 = [1,[2,3],4]
ls2 = copy.deepcopy(ls1)

makes an all new copy of the original lst1

lst1 = [1,[2,3],4]
lst2 = copy.copy(lst1)
lst2[1][0] = 20

both lst will now have a 20 instead of a 2 since it was changed for both

lst1 = [1,[2,3],4]
lst2 = deepcopy.copy(lst1)
lst2[1][0] = 20

now ony lst2 will contain 20 as it is the new copy of the lst

lst1  = [1,2]
lst2 = [3,4]
lst3 = lst1 + lst2

lst 3 shares both data from lst 1 and lst 2 so it is a shallow implementation (most implementation will be shallow)
but it did make a new list object


lst1 = [1,2,3]
lst2 = lst 1 * 4

again a shallow implementation and will only increase the total amount of cache will is a max of 12

class Counter:
    def __init__(self):
        self.val = 0
    def inc(self):
        self.val += 1
    def __repr__(self): **Special method** representation/expects a text representation of the object
        return str(self.val)

the same can be done with str(c1)

lst1 = [Counter() for i in range(3)]

evaluated will create 3 counter() since range starts from 0 and goes to 3

lst2 = [Counter()] *3

evaluated gets 3 counters

for c in lst1:
    c.inc()
    print(c)

for c in lst 2:
    c.inc()
    print(c)

there are not going to be the same


'''