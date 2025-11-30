class Vehicle:
    company = "Hero Honda Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        print("Init of vehicle..")
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provides mileage of {self.mileage}"

class Car(Vehicle):
    model = "ABC123"
    def __init__(self, car_type, drive_type):
        print("Init of Car..")
        self.car_type = car_type # Type of car - Sedan, Hatchback, SUV
        self.drive_type = drive_type # Manual/Automatic

        # Done after line 38.
        Vehicle.__init__(self,4,4,15)
        # Another way
        # super().__init__(4,6,18) # Used to refer the parent class.

# c1 = Car() - ERROR.. Because n_wheels, n_seats, mileage are needed which were inherited from vehicle.
# If car doesn't have __init__
# c1 = Car(4,5,20)
# print(c1.mileage) # 20
# print(c1.company) # Hero Honda Motors
# print(c1.get_details()) # This vehicle has 4 wheels and 5 seats and provides mileage of 20

c1 = Car("SUV", "Manual")
print(c1)
# Init of Car..
# <__main__.Car object at 0x000002BAC33B0590>

# No error from running upper code.
print(c1.model, c1.company) # ABC123 Hero Honda Motors
# print(c1.mileage) # ERROR.. we didn't initialize init of parent.
# Now we initialized it (Look at function)
print(c1.mileage) # 15
print(c1.get_details()) # This vehicle has 4 wheels and 4 seats and provides mileage of 15
print(c1.__dict__) # {'car_type': 'SUV', 'drive_type': 'Manual', 'n_wheels': 4, 'n_seats': 4, 'mileage': 15}

