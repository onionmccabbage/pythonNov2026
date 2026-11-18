# coding styles broadly fall into class-based and functional
# higher-order functions are functions which take other functions as arguments

fruits = ['apple', 'pears', 'kiwi', 'banana']

# map lets us apply any function to every member of any collection
# NB we do not actually invoke the function, we just specify it
title_fruits = tuple( map( str.capitalize, fruits ) )

def tidyUp(n):
    '''make sure the incoming string 'n' has no whitespace'''
    if type(n)==str:
        result = n.strip() 
    else:
        result = 'default'
    return result

values_l = ['   Python  ', '    tab', 'Done      ']
tidy = list( map(tidyUp, values_l)  )
print(tidy)
print( type(title_fruits) , title_fruits)


# as well as map we may use filter. This lets us apply a filter function across every member of a collection
def longWord(w):
    '''only return the word if it is more than 5 letter
    Otherwise return 'default' '''
    if len(w)<5:
        return False # NB any filter function must evaluate to True or False
    else:
        return True # this drives whether to include or excluse members of the collection

words = ('Python', 'wibblywoo', 'BBC')

long_words = tuple( filter(longWord, words) )

print( type(long_words), long_words )
