

class Swapi():
    '''a top-level class to encapsulate swpai data'''
    __slots__ = ['__name', '__immut', '__films']
    def __init__(self, n, f):
        self.name = n # all swpai data includes a name property
        # suppose we wanted an immutable property
        self.films = f
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
            raise TypeError('Name must be a non empty string')
    @property
    def films(self):
        return self.__films
    @films.setter
    def films(self, film_list):
        '''validate we have a list of items (more than zero)'''
        if type(film_list)==list and len(film_list)>0:
            self.__films = film_list
        else:
            raise TypeError('Films must be a non-empty list')

# we would usually write each class in separate module
class Species(Swapi):
    __slots__ = ['__name', '__language', '__films'] # NB slots are not inherited
    def __init__(self, n, language, films):
        super().__init__(n, films)
        self.language = language # this calls the setter method
    @property
    def language(self):
        return self.__language
    @language.setter
    def language(self, l):
        if type(l)==str and len(l)>0:
            self.__language = l
        else:
            raise TypeError('Language must be a non-empty string')

class Planet(Swapi):
    __slots__ = ['__name', '__climate', '__films']
    def __init__(self, n, climate, films):
        super().__init__(n, films)
        self.climate = climate
    @property
    def climate(self):
        return self.__climate
    @climate.setter
    def climate(self, c):
        if type(c)==str and len(c)>0:
            self.__climate = c
        else:
            raise TypeError('Climate must be a non-empty string')

