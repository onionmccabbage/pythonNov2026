# we may gather together opertions onto  single function

# here is a re-useable function to validate ewe have numeric values
def checkNumeric(value):
    '''check if the incoming argument value is a number
    If it is, just return it. Otherwise, return 1 as a default'''
    if type(value) == int:
        return value # all good
    else:
        return 1 # set a sensible default

# we may choose to set default values for our function arguments
def addNumbers(a=1, b=2): # here we choose to pass in arguments to the function
    '''A docstring lets us explain the purpose of a function
    Here we will check we have numeric values then add them 
    Triple quotes let us write several lines within a string'''
    # we can check that a and b are numbers
    # double-equals checks a value
    # if type(a)== int and type(b)== int:
    #     result = a+b
    #     return result
    # else:
    #     print('not integer')
    # use our checking function
    a = checkNumeric(a)
    b = checkNumeric(b)

# ternary operator
x=2
f = True if x==1 else False 
print(f) # False

# exercise this module
s = addNumbers() # the defaults will be used
r = addNumbers(5, '4')
print(r)
