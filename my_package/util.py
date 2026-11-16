from datetime import datetime

def showtoday():
    '''return a nicely formatted date representing today'''
    now = datetime.now() # .now gives date and time
    # we may choose to make this look pretty
    prettyDate = datetime.strftime(now, '%d-%m-%Y %H:%M:%S') # provide a 'picture' for the date
    return prettyDate

if __name__ == '__main__':
    # exercise this module
    n = showtoday()
    print( n )

    # what does python call this module?
    # every module we run directly is called '__main__'
    print( f'This module is currently known as {__name__}' )