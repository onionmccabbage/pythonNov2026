# this is a comment
# Python has some data types
a = 1 # we assign the value 1 to a variable called 'a'
b = 7.3 # this is a floating point number

print( a, b ) # print is a function. It has brackets
print( type(a), type(b) )

# Python has several data types
# all text is contained in a string type
c = 'here is a long string of characters inside quotes'
print(c, type(c)) # a string is an immutable ordinal collection of characters
# ordinal means the collection is in a numeric order: 0, 1, 2, 3 etc.
print( c[10] ) # this will be 'l'
# we may use [] to 'slice' any part of a collection. All collection start at zero
print( c[0:14] ) # [start:stop-before]
# other data types
boo = True # or False - the boolean data type
# we also have lists and tuples
l = [4,3,2,5.5,-2.11, 'hello', False] # here we have an ordinal mutable collection of any data type
# mutable means we can change existing values for other values
l[4] = -99
# other list operations
l.append('new')
l.insert(3, 'also')
l.pop() # removes the very last entry from a collection
print( type(l), l, l[4:6] )