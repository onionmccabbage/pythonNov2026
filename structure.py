# we may structure code using indentation
x = True

# we indent any code block
# a code block comes after a colon :
if x:
    print('true')
    print('the code block ends when we stop indenting code')
else:
    print('false')

# this is useful for validation (checking data is the write type)
value = input('please enter a positive integer: ')
# we need to validate i is an int and it is positive
# WARNING: inut is ALWAYS a string
print(type(value))
# we can check if the input string looks like an integer
print(value.isnumeric())

if value.isnumeric(): # isnumeric allows digits only.
    num = int(value) # cast the sting to an int
    if num >0:
        print(f'Thank you for typing {num}') # f'' lets us format the string
else:
    print(f'{value} is not a positive number')

# the code block ends when there is no more 
# we may write a loop like this
l = [2,4,6,8,10]
for i in l:
    if i == num:
        print(f'{i} matches {num}')
    else:
        print(f'{i} does not match {num}')








