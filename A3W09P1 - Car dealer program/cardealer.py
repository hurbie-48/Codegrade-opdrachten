class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")


class Car:
    def __init__(self, brand, model, color, price, sold_to=None):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.customer = None
        self.sold_to = None

        if sold_to is not None:
            self.sell(sold_to)

    def sell(self, sold_to=None):
        self.sold = True
        if sold_to is not None:
            self.customer = sold_to
            self.sold_to = sold_to

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        if not self.sold:
            print("Not sold yet")
        else:
            if self.sold_to is not None:
                print(f"Sold to {self.sold_to.name}")
            else:
                print("Sold")


class Motorcycle:
    def __init__(self, brand, model, color, price, sold_to=None):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.customer = None
        self.sold_to = None

        if sold_to is not None:
            self.sell(sold_to)

    def sell(self, sold_to=None):
        self.sold = True
        if sold_to is not None:
            self.customer = sold_to
            self.sold_to = sold_to

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        if not self.sold:
            print("Not sold yet")
        else:
            if self.sold_to is not None:
                print(f"Sold to {self.sold_to.name}")
            else:
                print("Sold")


if __name__ == "__main__":

    first_car = Car("BMW", "X5", "Black", 34.899)

    first_car.print()

    second_car = Car("BMW", "X5", "Black", 34.899, "John Doe")

    second_car.print()
    second_car.customer.print()