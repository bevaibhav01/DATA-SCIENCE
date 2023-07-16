# Q2. Create a child class car from the vehicle class created in Que 1, which will inherit the vehicle class.
# Create a method named seating_capacity which takes capacity as an argument and returns the name of
# the vehicle and its seating capacity.

class vehicle:
    def __init__(self, name, max_speed, avg):
        self.name = name
        self.speed = max_speed
        self.avg = avg

    def details(self):
        return self.name, self.speed, self.avg


class car(vehicle):

    def __init__(self, name, speed, avg):
        self.capacity = 0
        vehicle.__init__(self,name, speed, avg)

    def seating_capacity(self, capacity):
        self.capacity = capacity
        return self.capacity, self.name


object = car("fortuner", 180, 20)

print(object.seating_capacity(7))
