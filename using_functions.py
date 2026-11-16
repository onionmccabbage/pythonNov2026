# we may gather together opertions onto  single function

def addNumbers(a, b): # here we choose to pass in arguments to the function
    '''A docstring lets us explain the purpose of a function
    Here we will check we have numeric values then add them 
    Triple quotes let us write several lines within a string'''
    # we can check that a and b are numbers
    # double-equals checks a value
    if type(a)== int and type(b)== int: # and or
        # we have integers
        result = a+b
        return result
    else:
        print('not integer')

# exercise this module
r = addNumbers(5, '4')
print(r)


