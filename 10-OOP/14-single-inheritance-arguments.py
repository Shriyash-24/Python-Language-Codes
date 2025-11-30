# Single Inheritance Arguments
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
    def __init__(self, car_type, drive_type, n_wheels, n_seats, mileage):
        self.car_type = car_type
        self.drive_type = drive_type
        super().__init__(n_wheels, n_seats, mileage)

c1 = Car("SUV", "Manual", 4, 7, 20)
