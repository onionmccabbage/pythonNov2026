import datetime

def showtoday():
    '''return a nicely formatted date representing today'''
    now =datetime.date( datetime.datetime.today() )
    return now

# exercise this module
n = showtoday()
print( n )