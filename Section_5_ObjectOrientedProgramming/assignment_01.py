# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""


# Your Code Below:


class Animal:
    def __init__(self):
        print("Animal constructed.")

    def eat(self):
        print("Animal is eating..")

    def move(self):
        print("Animal is moving..")


class Dog(Animal):
    def __init__(self, dog_name, dog_age):
        Animal.__init__(self)
        self.name = dog_name
        self.age = dog_age

    def move(self):
        print("Dog is running..")


class Fish(Animal):
    def __init__(self, fish_name, fish_age):
        Animal.__init__(self)
        self.name = fish_name
        self.age = fish_age

    def move(self):
        print("Fish is swimming..")


class Bird(Animal):
    def __init__(self, bird_name, bird_age):
        Animal.__init__(self)
        self.name = bird_name
        self.age = bird_age

    def move(self):
        print("Bird is flying..")


my_dog = Dog("lady", 7)
my_dog.move()
my_dog.eat()

my_fish = Fish("sally", 1)
my_fish.move()
my_fish.eat()

my_bird = Bird("free", 4)
my_bird.move()
my_bird.eat()