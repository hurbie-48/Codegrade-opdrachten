import sqlite3


def execute_query(query: str):
    sqliteConnection = sqlite3.connect("trades.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result_of_query = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    return result_of_query


class Trade:

    def __init__(self, id=None, trade_type=None, year=None, from_country_id=None, to_country_id=None, quantity=None,
                 value=None):
        self.id = id
        self.trade_type = trade_type
        self.year = year
        self.from_country_id = from_country_id
        self.to_country_id = to_country_id
        self.quantity = quantity
        self.value = value

    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    def get_product(self):
        from product import Product

        query = f"SELECT id, title FROM products WHERE id = {self.trade_type} LIMIT 1;"
        res = execute_query(query)

        if res:
            current_product = Product("")
            current_product.id = int(res[0][0])
            current_product.title = res[0][1]
            if "name" in current_product.__dict__:
                del current_product.__dict__["name"]
            return current_product
        return None

    def get_country_from(self):
        from country import Country
        query = f"SELECT id, name, short_code FROM countries WHERE id = '{self.from_country_id}';"
        res = execute_query(query)
        if res:
            return Country(id=int(res[0][0]), name=res[0][1], short_code=res[0][2])
        return None

    def get_country_to(self):
        from country import Country
        query = f"SELECT id, name, short_code FROM countries WHERE id = '{self.to_country_id}';"
        res = execute_query(query)
        if res:
            return Country(id=int(res[0][0]), name=res[0][1], short_code=res[0][2])
        return None

    def mass_in(self, unit: str) -> float:
        qty = float(self.quantity) if self.quantity is not None else 0.0
        unit_lower = unit.lower().strip()
        if unit_lower == "skip" or unit_lower == "kg":
            return qty
        elif unit_lower == "g":
            return qty * 1000.0
        elif unit_lower == "mt":
            return qty / 1000.0
        elif unit_lower == "lb":
            return round(qty * 2.20462, 2)
        elif unit_lower == "oz":
            return round(qty * 35.274, 2)
        elif unit_lower == "st":
            return round(qty * 0.157473, 3)
        return qty