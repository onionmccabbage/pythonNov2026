# we know about numbers
x = 55 # int
y = 44.2 # float

# we know about strings (str)
hello = 'greet'
# we have met list and tuple
k = [x, y, hello, 46, 'oobiedoobie']
j = (1,) # this is a one-member tuple
# all the above collections are ordinal

# we have two non-ordinal collections
# a dictionary is a collection of key-value pairs
# dict is NOT ordinal
# we may choose to write a dict over several lines
g = {
    'fn':'Floella',
    'ln':'Benjamin',
    'award':'Dame'
    }

# dict are always mutable
g['age'] = 72
print( g, type(g) )
# we may access members of the dict by their key
print( g['award'] )

# we may iterate over the members of a dict
for (k,v) in g.items():
    print(f'{k} contains {v}')

# we also have a 'set' data type
# a set is not ordinal and may contain most simple data types
# a set will ensure its members are unique (each member may only occur once)
data = {3, 2, 7, -2, 'a', True} # a set contains only values
data.add(99)
data.remove(True)
print( data, type(data) )