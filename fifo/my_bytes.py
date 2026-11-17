# as well as text files we may need to operate with byte files
# Bytes are a way to represent data more efficiently
# we byte-encode our data

def makeBytes(f):
    '''convert the incoming values in 'f' to a bytestring'''
    b = b'{f}' # this converts a string to a byte-encoded string
    return b

if __name__ == '__main__':
    w = 'hello'
    x = makeBytes(w)
    print(w, type(w))