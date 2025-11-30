# Class A and Class B ==> Class C can inherit from both of them.
# Multilevel inheritance is Class A is inherited by B and B is inherited by Class C. Class C inherits from both of them indirectly.

class Vehicle:
    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This Vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provide mileage of {self.mileage}"

class Car(Vehicle):
    model = "ABC123"
    def __init__(self, car_type, drive_type, n_wheels, n_seats, mileage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(n_wheels, n_seats, mileage)

    def display_info(self):
        print(f"Car Type: {self.car_type}, Drive Type: {self.drive_type}")

class ElectricCar(Car):
    def __init__(self, car_type, drive_type, n_wheels, n_seats, mileage, battery_capacity, distance_range):
        self.battery_capacity = battery_capacity
        self.distance_range = distance_range
        super().__init__(car_type, drive_type, n_wheels, n_seats, mileage)

    def charge(self):
        print(f"Charging the battery to {self.battery_capacity}%")

ec1 = ElectricCar("Sedan", "Manual", 4, 4, 25, 100, 400)
print(ec1.__dict__) # {'battery_capacity': 100, 'distance_range': 400, 'car_type': 'Sedan', 'drive_type': 'Manual', 'n_wheels': 4, 'n_seats': 4, 'mileage': 25}
