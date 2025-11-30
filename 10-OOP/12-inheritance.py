# Inheritance - Property or behaviour that is derived from a parent or ancestors.

# Vehicle - Fuel Capacity, Mileage.
# Car is type of vehicle and motorcycle is type of vehicle.
# Car also has mileage, motorcycle also has mileage.
# Car is a vehicle, Motorcycle is a vehicle. They have is-a relationship.
# So fuel capacity, and mileage are properties of vehicle class that can be inherited by car and motorcycle.
# Vehicle is base class, and the class that inherits is called as derived class/child class.
# Vehicle can move, a car can move by inheriting property of vehicle.
# Car class can have it's own properties such as sunroof, it's specific to car.

# Person is a class used to define humans, it can have name, age, eats()..
# Teacher, Doctor, Student are child class, Person will be it's parent.
# Teacher can have specific properties, such as teach().
# Student can have specific properties, such as study() and so on.


class Vehicle:
    company = "Hero Honda Motors"

    def __init__(self, n_wheels, n_seats, mileage):
        self.n_wheels = n_wheels
        self.n_seats = n_seats
        self.mileage = mileage

    def get_details(self):
        return f"This vehicle has {self.n_wheels} wheels and {self.n_seats} seats and provides mileage of {self.mileage}"

class Car(Vehicle):
    pass

# Car class inherits the vehicle class.
# Car class is called Child class or derived class.
# Vehicle class is called Parent class or base class.
# This is called single inheritance.

