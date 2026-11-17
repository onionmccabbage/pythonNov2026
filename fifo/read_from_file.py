# we may work with text files ot write data as and when we choose

def fileReader():
    '''Retrieve the contents of a persistent text file'''
    try:
        with open('log.txt', 'r') as fin: # text is the default
            # i = fin.read() # read() retrievs the entire contents as one continous string
            # i = fin.readlines() # readlines() retrieves the entire contents into a list of strings
            mylines = [] # in this case we DO need to initiate the empty list
            for k in range(0,20):
                mylines.append (fin.readline()) # readline() will read the next line (until \n or EOF)
            return mylines
    except Exception as err:
        print(err)

if __name__ == '__main__':
    y = fileReader()
    print(y)