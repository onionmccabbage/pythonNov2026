# we may choose to format the precision of numeric values
a = 3
b = 7.6

# NB we would only round out a value when presenting it (not during calculations)
print(f'{(b/a):0.4f}')

# oh and by the way...
s = 'The value {1} divided by {0} is {3}'.format(b, a, b/a, a/b)
print(s)