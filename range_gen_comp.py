# NB whenever we name something, there are some basics rules
# we may use letters, numbers and the underscore
# don't begin a name with a digit
# there are also some common conventions
# 'snake_case' is common for most things
# 'camelCase' where subsequent words have initial cap
# 'PascalCase' where each word takes initial cap

# range
r = range(0, 10) # only the range object exists in memory (rather than all the values using up memory)
# range can be like this
s = range(10**6, 0, -1)
for _ in s:
    print(_)
    if _ < (10**6)-8:
        break

# generators
# a bit like a range, but with added calculations
g = (i**2 for i in r) # NB we use () to make a generator
print( type(g) )
for _ in g:
    print(_)

# a useful function
def useful(n):
    '''some complex calcs we may need'''
    result = ((n/2)**3)**0.5
    return result

# another generator
f = (useful(i) for i in r)
for _ in f:
    print(_)

# comprehensions
# a comprehension will comprehensively deal with every member of a collection
j = [i**2 for i in r] # this is a list comprehension []
print(j, type(j))