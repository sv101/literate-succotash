# Method overriding

class Pet:
    def __init__(self, name):
        self.name = name
        self.is_alive=True
    def eat(self):
        return f'{self.name} is eating.'
    def talk(self):
        return f'{self.name}'

class Dog(Pet):
    number_of_legs = 4
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
#    def talk(self):
#        return f'{self.name} says Woof!'
        