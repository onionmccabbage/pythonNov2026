# here we will use random numbers, imports and range
from random import random # there are many libraries that come with Python
from random import randint
# we may also import our own modules
from using_functions import checkNumeric # this imports the entire module
# CAREFUL: whenever we import stuff, any executable code WILL run

r = random() # we imported this specifically, so no need for random.random()
s = randint(0,10)
print(r, s)

# we may use our imported code
r = checkNumeric(r) # or using_functions.checkNumeric(r)
print(r) # the same random floating point number


# the 'range' object
w = range(0,11,2) # (start, stop-before, step=1)
print(type(w))
for i in w:
    print(i) # 0, 2, 4, 6, 8, 10

# a range can handle calculations
for i in w:
    # is it an even number
    if i/2 == i//2:
        print(f'{i} is even')
    # is it an odd number
    if i/2 != i//2:
        print(f'{i} is odd')
    # is is a square number