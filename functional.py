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