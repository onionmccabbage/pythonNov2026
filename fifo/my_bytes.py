# as well as text files we may need to operate with byte files
# Bytes are a way to represent data more efficiently
# we byte-encode our data

def makeBytes(f):
    '''convert the incoming values in 'f' to a bytestring'''
    # b = b'{f}' # this converts a string to a byte-encoded string
    b = f.encode() # this also converts to a byte string
    return b

def writeBytes(b):
    '''commit the bytes in 'b' to a byte file'''
    try:
        with open('bytefile', 'ab')  as bout:
            u = b.encode() # even if it is already encoded, we just make sure
            bout.write(u)
    except Exception as err:
        print(err)

def readBytes():
    '''retrieve the bytes from a byte file'''
    try:
        with open('bytefile', 'rb') as bin:
            q = bin.read()
            return q
    except Exception as err:
        print(err)

if __name__ == '__main__':
    w = str(0x007) # 0x lets us work in hexadecimal
    x = makeBytes(w)
    print(w, type(w))
    f = 'simple plain text'
    writeBytes(f)
    k = readBytes()
    print(k)