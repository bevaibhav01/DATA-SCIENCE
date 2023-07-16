# Q4. What are getter and setter in python? Create a class and create a getter and a setter method in this
# class.

#getter setter is used get or set a value of private variables

class vehicle:
    def __init__(self,name,speed):
        self.name=name
        self.__speed=speed

    def get_speed(self):
        return self.__speed

    def set_speed(self,speed):
        self.__speed=speed


car=vehicle("harrier",120)

print(car.get_speed())
car.set_speed(200)
print(car.get_speed())