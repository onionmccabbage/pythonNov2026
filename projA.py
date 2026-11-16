# here we will use random numbers, imports and range
import random # there are many libraries that come with Python
# we may also import our own modules
import using_functions # this imports the entire module

r = random.random()
s = random.randint(0,10)
print(r, s)

# we may use our imported code
r = using_functions.checkNumeric(r)
print(r) # 1


# the 'range' object
w = range(0,11,2) # (start, stop-before, step=1)
print(type(w))
for i in w:
    print(i) # 0, 2, 4, 6, 8, 10