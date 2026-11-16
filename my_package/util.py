from datetime import datetime

def showtoday():
    '''return a nicely formatted date representing today'''
    now = datetime.now() # .now gives date and time
    # we may choose to make this look pretty
    prettyDate = datetime.strftime(now, '%d-%m-%Y %H:%M:%S') # provide a 'picture' for the date
    return prettyDate

# exercise this module
n = showtoday()
print( n )