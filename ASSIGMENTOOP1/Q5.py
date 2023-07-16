# Q5.What is method overriding in python? Write a python code to demonstrate method overriding.

# Method overriding is an ability of any object-oriented programming language that
# allows a subclass or child class to provide a specific implementation of a method
# that is already provided by one of its super-classes or parent classes

class animal:
    def __init__(self):
        self.value = "PARENT"

    def show(self):
        print(self.value)


class dog(animal):
    def __init__(self):
        self.value = "child"

    def show(self):
        print(self.value)


obj1=dog()

obj1.show()
