# as well as text files we may need to operate with byte files
# Bytes are a way to represent data more efficiently
# we byte-encode our data

def makeBytes(f):
    '''convert the incoming values in 'f' to a bytestring'''
    # b = b'{f}' # this converts a string to a byte-encoded string
    # b = f.encode() # this also converts to a byte string
    b = bytes(f)

def writeBytes(b):
    '''commit the bytes in 'b' to a byte file'''
    try:
        with open('bytefile', 'ab')  as bout:
            if type(b)==str:
                b = bytes(b) # even if it is already encoded, we just make sure
            bout.write(b)
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
    w = 0x007 # 0x lets us work in hexadecimal
    x = makeBytes(w)
    print(w, type(w))
    f = 'simple plain text'
    # here we build a byteArray (a collection of byte values)
    d = bytearray()
    for i in range(0,64):
        d.append(i) 
    writeBytes(d)
    k = readBytes()
    print(k)

# '© ? ?' in 'utf-8' is 
# b'\xC2\xA9\x20\xF0\x9D\x8C\x86\x20\xE2\x98\x83'
