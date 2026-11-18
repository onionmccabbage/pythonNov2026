# here we will create our own class

class Person(): # the () are optional
    '''This class will encapsulate data related to person
    name (non-empty string) and age (positive integer)'''
    # a class has 'properties' (things that belong to the class)
    # the __init__ will run once, when we create an instance
    def __init__(self, name, age): # any class function MUST take 'self' as an argument
        self.name = name
        self.age = age



if __name__ == '__main__':
    # exercise the code within this module
    # we can make instances of our class
    p1 = Person() # this will make the __init__ method run once

    # we can make instances of any class
    l1 = list() # short cut is l1 = []
    t1 = tuple()
    d1 = dict()