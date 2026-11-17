# we may work with text files ot write data as and when we choose

def fileWriter(s):
    '''Commit the contents of 's' to a persistent text file'''
    try:
        # 'x' is exclusive access (fails if the file already exists)
        # 'w' means (over)write any existing content
        with open('log.txt', 'a') as fout: # text is the default
            fout.write(s)
            fout.write('\n') # also \t
            # fout.close() # not needed, since 'with' tidies up anyway
            # when the 'with' block ends, the fout resource will be released automatically
    except Exception as err:
        print(err)



if __name__ == '__main__':
    # the following code will only be executed if this module is run directly
    # if this module is imported elsewhere, the following lines do not execute
    s = ['apples', 'pears', 'oranges', 'durian', 'kiwi']
    for item in s:
        fileWriter(item)