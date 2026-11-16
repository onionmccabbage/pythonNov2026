# there are a few kinds of loop in Python

def game(): # we are not obliged to provide function arguments
    '''Here we will ask the user to enter a value
    If they enter 'quit' then the program ends
    if a positive integer is entered, convert and show the value
    for all other entries, explain that a number is needed'''
    running = True
    while running: # this is often called a 'run loop'
        # ask the user to enter a value
        val = input('Please enter a value: ') # remember: input is ALWAYS a string
        if val == 'quit':
            print('Goodbye')
            break # this will stop the while loop
        elif val.isnumeric():
            num = int(val) # convert it to an integer
            running=False # once we have an integer we can stop asking for user entry
            return num 
        else:
            print('We need a number, try again')

# we must remember to actully call our function!!
game()
