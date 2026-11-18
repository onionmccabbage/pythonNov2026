# here we will create our own class
class Person(): # the () are optional
    '''This class will encapsulate data related to person
    name (non-empty string) and age (positive integer)'''
    # a class has 'properties' (things that belong to the class)
    # the __init__ will run once, when we create an instance
    def __init__(self, name, age): # any class function MUST take 'self' as an argument
        self.name = name
        self.age = age # this line will invoke the 'age' setter function
    # in python @property is called a 'decorator'
    @property # getter method (accessor)
    def name(self):
        # __ is called 'name mangling' we may only access it within the class
        return self.__name
    @name.setter # setter method (mutator)
    def name(self, new_name):
        if type(new_name)==str and new_name != '':
            self.__name = new_name
        else:
            raise TypeError('Name must be a non-empty string')
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if type(new_age)==int and new_age>0:
            self.__age = new_age
        else:
            raise TypeError('Age must be a positive integer')
    def __str__(self):
        '''Everything in Python has a __str__ method
         This method is called whenever we 'print' '''
        return f'{self.name} is {self.age} years old'

if __name__ == '__main__':
    # exercise the code within this module
    # we can make instances of our class
    p2 = Person('Oenid', 32)
    # can we directly access __name or __age?
    # print(p2.__name, p2.__age) #

    p2.age = 55 # all good 
    print(p2.age, p2.name)
    p1 = Person('Floella', 70) # this will make the __init__ method run once
    try:
        p1.name = True  #oops!!!
    except TypeError as te:
        print(te)
    # we use dot notation to access members of the class instance
    print( p1, p1.name, p1.age, type(p1) )
    # we can make instances of any class
    l1 = list() # short cut is l1 = []
    t1 = tuple()
    d1 = dict()