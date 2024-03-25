'''

Stacks consist of LIFO which means they come from LAST in FIRST out order

s = Stack() creates an empty stack
len(s)

s.push(item) adds item to the top of the stick (INSERT)
s.pop() removes the item from the top of the stack (s) and returns it as a string
s.top() returns the item at the top of the stack ()

infix notation: just regular notation like traditional equations
prefix (polish) notation: similar but the functions go before they are done
!!!! TIP TO DO THIS IS START RIGHT TO LEFT UNTIL THE FIRST FUNCTION AND CONTINUE WORKING
/*+52-834 (this means that from the subtraction sign to 8 and 3 are done) then
+52 are done since its done next and then * form the results of the previous functions
and then / with the 4 ( also closest to each function not the farthest away
postfix notation: similar to prefix notation but in the sense that it goes
from left to right and u choose the first function that comes in line dosent matter where
but the first one

class ArrayStack:
     def __init__(self):
         self.data = ArrayList()
     def __len__(self):
         return len(self.data)
     def is_empty(self):
         return len(self) == 0
     def push(self, val):
         self.data.append(val) #since the last item in the stack, it gets appended
     def top(self):
         if (self.is_empty()):
             raise Exception("Stack is empty")
         return self.data[-1] #last item in the list gets removed
     def pop(self):
         if (self.is_empty()):
             raise Exception("Stack is empty")
         return self.data.pop() #the popped items gets removed



Queue ADT is a collection of items, FIRST in FIRST OUT
q = Queue()
q.enqueue(item) adds item into the queue (at end) insert
q.dequeue() removes and returns the first item in the queue(q) first to be added
q.first() returns the top item in the queue(q)

DYNAMIC Queue accommodates for the no size limitation, dynamically configures more data

STATIC Queue has a size limitation with a fixed sized

q = Queue(max_cap)
q.isfull() Return True if q is empty
q.enqueue(item) adds item into the queue unless its full!

say for example [2,4,6,8] is the queue and the first element is 2 since it stays in
front of the queue and any new item gets added to the back of the queue

CIRCULAR array will add the new items to the front of the queue if it gets full



'''