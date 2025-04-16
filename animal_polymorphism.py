class Animal:
    def move(self):
        print("This animal moves in its own way.")

class Dog(Animal):
    def move(self):
        print("The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("The bird flies through the sky.")

class Cat(Animal):
    def move(self):
        print("The cat moves silently with elegance.")

animals = [Dog(), Bird(), Cat()]

for animal in animals:
    animal.move()
