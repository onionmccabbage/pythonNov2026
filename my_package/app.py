# this may be ou main application
from util import showtoday

def doStuff():
    return f'Today is {showtoday()}'

t = doStuff()
print( t )