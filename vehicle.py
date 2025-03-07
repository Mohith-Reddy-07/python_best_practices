from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Car(Vehicle):
    def fuel_type(self):
        print("Car uses petrol or diesel")

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol")


car = Car()
bike = Bike()

car.fuel_type()
bike.fuel_type()
