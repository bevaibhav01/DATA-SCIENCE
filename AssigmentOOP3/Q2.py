# Q2. Differentiate between Abstraction and Encapsulation. Explain with an example.

# Abstraction is the process of representing complex real-world objects as
# simplified models in a program. It focuses on showing only the relevant
# characteristics and behaviors of an object while hiding the unnecessary
# details.

# Encapsulation is the process of bundling data (attributes) and the methods that
# operate on that data within a single unit called a class. It aims to restrict
# direct access to the internal data and allow access only through well-defined
# methods, known as getters and setters. Encapsulation helps protect the data
# from unauthorized access and modification, promoting data integrity and code
# maintainability.

import abc


# ABTRACTION
class human:
    @abc.abstractmethod
    def show(self):
        pass


class vaibhav:
    def show(self):
        print('Iam a real human')


obj = vaibhav()
obj.show()


class human1:
    def __init__(self, name):
        self.__name = name

    def getname(self):
        return self.__name


obj1 = human1("vaibhav")
print(obj1.getname())
# obj.name  we cant acces in directly now we
# have to use getter setter methos
