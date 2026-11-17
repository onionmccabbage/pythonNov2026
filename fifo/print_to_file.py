# sometimes we simply need to commit text to a persistent file

t = 'is it coffee yet?'

# 'a' will append (or create) the file 't' means text
fout = open('log.txt', 'at') # this is a file access object

# NB print always adds a newline to the end by default
print( t, file=fout )