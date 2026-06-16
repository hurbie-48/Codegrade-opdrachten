class Product:
    # Init functie om een nieuwe instantie te maken
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        # Prijs ophalen en teruggeven
        if quantity < 10:
            return self.price * quantity
        elif 10 <= quantity < 100:
            return self.price * quantity * 0.9
        else:
            return self.price * quantity * 0.8

    def make_purchase(self, quantity):
        # Checken of het product op voorraad is.
        if quantity > self.amount:
            print("Nothing on stock!")
        self.amount -= quantity


if __name__ == "__main__":
    first_product = Product("Test", 100, 10.0)
    print(first_product.get_price(3))
    print(first_product.get_price(17))
    print(first_product.get_price(157))
    first_product.make_purchase(1)
    print(first_product.amount)
    first_product.make_purchase(13)
    print(first_product.amount)
    first_product.make_purchase(166)