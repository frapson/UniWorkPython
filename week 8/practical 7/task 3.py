import random

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

ListOfRandomNumbers = random.sample(range(0, 101), 10)

for i in ListOfRandomNumbers:
    if is_even(i):
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
