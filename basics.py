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