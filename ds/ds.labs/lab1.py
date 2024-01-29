import random


def can_construct(word, letters):
    letterbank = [0] * 26
    offset = ord("a")  # offset made with the ord value of a in order ensure if the value is in the code

    # dealing with letters first
    for i in letters:
        letterbank[ord(i) - offset] += 1  # for the specific index of the word, we add a 1 to come back to and test

    for i in word:
        if letterbank[ord(i) - offset] < 1:  # can no longer continue since the value at the spcific index is not 1
            return False
        letterbank[ord(i) - offset] -= 1  # removing the 1 at the specific index since it is present/since we can
        # we can only use it once as stated in the instructions

    return True  # finalized since it was able to get a correct value


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)  # we are returning a new COMPLEX object so

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)  # same here

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.b)  # foil method

    def __repr__(self):
        sign = "+" if self.b >= 0 else '-'
        return f"{self.a} {sign} {abs(self.b)}i"  # abs returns the absolute value since b is already getting changd
        # by i

    def __iadd__(self, other):
        self = self + other  # actually changing self so need to return self itself
        return self


def create_permutation(n):
    random_list = []
    counter = 0
    while counter <= n:
        counter += 1
        random_list += random.randint(0, n - 1)
    return random_list


def scramble_word(word):
    total_index = len(word)
    scramble_lst = create_permutation(total_index)
    for i in range(len(scramble_lst)):
        scramble_lst[i] = word[scramble_lst[i]]
    return ''.join(scramble_lst)


def game(word):
    guessing_word = scramble_word(word)
    print("Scramble the word:" + guessing_word)
    tries = 3
    correct_try = False

    while tries and not correct_try:
        guess_user = input("Try" + str(4 - tries) + ":")
        if guess_user == word:
            correct_try = True
        else:
            print("Try again!")
            tries -= 1

    if tries:  # if tries is still active but the while loop got cancelled that means that tris were still available
        # however if out of tries, then appropiate message follows
        print('Yay, you got it!')
    else:
        print('Out of tries ')
