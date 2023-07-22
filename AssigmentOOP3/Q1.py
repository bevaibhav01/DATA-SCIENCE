# Q1. What is Abstraction in OOps? Explain with an example.

# Abstraction is a fundamental concept in Object-Oriented Programming (OOP) that
# focuses on hiding the implementation details of an object and exposing only the
# relevant characteristics or behaviors to the outside world. It allows you to
# create a simplified representation of an object, emphasizing what an object does
# rather than how it does it.

import abc


class human:
    @abc.abstractmethod
    def show(self):
        pass
class vaibhav:
    def show(self):
        print('Iam a real human')

obj=vaibhav()
obj.show()

