from abc import ABC, abstractmethod


class Vehicle(ABC):
    @staticmethod
    @abstractmethod
    def drive(distance):
        pass

    @staticmethod
    @abstractmethod
    def refuel(fuel):
        pass


class Car(Vehicle):
    AC = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Car.AC)
        if self.fuel_quantity - needed_fuel >= 0:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):
    AC = 1.6
    FUEL = 0.95

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = distance * (self.fuel_consumption + Truck.AC)
        if self.fuel_quantity - needed_fuel >= 0:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += (fuel * self.FUEL)
        return self.fuel_quantity


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

