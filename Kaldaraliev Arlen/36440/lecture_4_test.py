
current_student_github_progress = "almost done"


MAX_CARS_COUNT = 10


class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


car1 = Car("Toyota", "Camry", "Red")


print(car1.brand, car1.model, car1.color)