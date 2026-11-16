# this may be ou main application
from util import showtoday

def doStuff():
    return f'Today is {showtoday()}'

if __name__ == '__main__':
    t = doStuff()
    print( t )

    print( __name__ )