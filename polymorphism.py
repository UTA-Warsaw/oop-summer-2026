
class Car:
    def show_information(self):
        print("This is a car.")


class Plane:
    def show_information(self):
        print("This is a plane.")


class Ship:
    def show_information(self):
        print("This is a ship.")


vehicles = [Car(), Plane(), Ship()]

for vehicle in vehicles:
    vehicle.show_information()
    