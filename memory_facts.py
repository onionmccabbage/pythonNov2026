# some devices are restricted in their capabilities
# it is always a good idea to have memory efficiency in mind
# NB Python is not restricted in any practical way: it will make use of as much resource as we give it
def checkEquality(a, b):
    if a==b:
        return 'the same value (in the same memory location)'
    else:
        return 'different values (in different memory locations)'

x = 10
y = 10
print( checkEquality(x, y) )

# tuples are much less memory hungry than lists
# tuple (immutable) list (mutable)