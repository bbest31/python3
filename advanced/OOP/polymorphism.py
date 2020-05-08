# Polymorphism
# Method Overriding is when the same class method is implemented in different ways in different classes.

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method.")

class Dog(Animal):
    def __init__(self,name):
        super.__init__(name)

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self,name):
        super.__init__(name)

    def speak(self):
        print("Woof!")