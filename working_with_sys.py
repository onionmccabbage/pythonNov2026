# sys refers to the system upon which Python is operation
import sys
# we may choose to add a location for Python to look for imports etc
sys.path.append('data')

print(sys.path)

# sys also includes argv which is a list of arguments
# sys.argv[0] is always the name of the currently running module
# we may choose to inject further system argument variables
# tis is useful, since 'input' is rarely going to have a user to respond!!!!
for _ in sys.argv:
    print(_)

# we often concatenate all the sys.argv beyond member zero
result = ', '.join( sys.argv[1:] ) # start at member 1
print(result)