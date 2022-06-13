class Dog:
    number_of_legs = 4
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_alive=True
    def eat(self):
        return f'{self.name} is eating.'
    def talk(self):
        return f'{self.name} says Woof!'


class Cat:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.is_alive=True
    def eat(self):
        return f'{self.name} is eating.'
    def talk(self):
        return f'{self.name} says Meow!'