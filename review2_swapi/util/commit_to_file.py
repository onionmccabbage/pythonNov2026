def persistText(t):
    '''persist the contents of 't' to a text file'''
    try:
        with open('swapi.txt', 'at') as fout:
            fout.write(t)
            fout.write('\n')
    except Exception as err:
        print(err)