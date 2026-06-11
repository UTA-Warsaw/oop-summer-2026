class FoodOrder:
    def __init__(self, customer):
        self.customer = customer

    def prepare(self):
        print(f"Preparing order for {self.customer}")


class PizzaOrder(FoodOrder):
    def prepare(self):
        print(f"Preparing pizza for {self.customer}")


order = PizzaOrder("Samet")
order.prepare()