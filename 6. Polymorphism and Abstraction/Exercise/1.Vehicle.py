from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    ADDITIONAL_CAR_FUEL_CONSUMPTION = 0.9

    def drive(self, distance ):
        consumption = distance * (self.fuel_consumption + Car.ADDITIONAL_CAR_FUEL_CONSUMPTION)

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    ADDITIONAL_CAR_FUEL_CONSUMPTION = 1.6
    TRUCK_TANK_CAPACITY = 0.95

    def drive(self, distance ):
        consumption = distance * (self.fuel_consumption + Truck.ADDITIONAL_CAR_FUEL_CONSUMPTION)

        if consumption <= self.fuel_quantity:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += Truck.TRUCK_TANK_CAPACITY * fuel


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)









