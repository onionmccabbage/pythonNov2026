

class Swapi():
    '''a top-level class to encapsulate swpai data'''
    __slots__ = ['__name', '__immut']
    def __init__(self, n):
        self.name = n # all swpai data includes a name property
        # suppose we wanted an immutable property
        self.__immut = 'cannot be changed'
    # we need get/set methods for 'name'
    @property
    def name(self):
        return self.__name # mangled!!!
    @name.setter
    def name(self, new_name):
        if type(new_name) == str and len(new_name)>0:
            self.__name = new_name
        else:
            # self.__name = 'default' # we may choose to set a sensible default
            raise TypeError('Name mus be a non empty string')