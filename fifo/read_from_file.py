# we may work with text files ot write data as and when we choose

def fileReader():
    '''Retrieve the contents of a persistent text file'''
    try:
        with open('log.txt', 'r') as fout: # text is the default
            i = fout.read()
            return i
    except Exception as err:
        print(err)

if __name__ == '__main__':
    y = fileReader()
    print(y)