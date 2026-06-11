# Abstraction = hiding complex implementation details and showing only essentials

from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Car is moving")


car = Car()
car.move()