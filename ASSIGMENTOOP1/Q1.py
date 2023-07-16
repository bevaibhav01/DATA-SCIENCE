# Q1, Create a vehicle class with an init method having instance variables as name_of_vehicle, max_speed
# and average_of_vehicle.

class vehicle:
    def __init__(self, name, max_speed, avg):
        self.name = name
        self.speed = max_speed
        self.avg = avg

    def details(self):
        return self.name, self.speed, self.avg


car = vehicle("fortuner", 180, 20)

print(car.details())
