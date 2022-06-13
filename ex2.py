# Subclasses

class Pet:
    def __init__(self, name):
        self.name = name
        self.is_alive=True
    def eat(self):
        return f'{self.name} is eating.'
    def talk(self):
        return f'{self.name}'

# Since all pets have similar features, we can reduce typing out repetative code by creating 
# a parent class and use the parent classes as a blue print to derive sub classes

# In our example we have defined a pet class and used inheritence to create the Dog class

class Dog(Pet):
    number_of_legs = 4
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
#    def talk(self):
#        return f'{self.name} says Woof!'
        