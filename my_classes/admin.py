from person import Person
# everything in Python is an object
# every number, bool, list, tuple, dict, set, range, generator
# also every module, every class, every exception, every function
# By default every class inherits from 'object'
class Admin(Person): # anything can be inherited from
    def __init__(self, name, age, duty):
        super().__init__(name, age)
        self.duty = duty
    def __str__(self):
        # remember, self.name will call the getter for name (returns self.__name)
        return f'The administrator {self.name} is responsible for {self.duty}'

if __name__ == '__main__':
    a1 = Admin('Ethel', 36, ['backups', 'security', 'feed cat'])
    a1.duty.append('make coffee')
    print(a1)


