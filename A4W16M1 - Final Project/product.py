import sqlite3


def execute_query(query: str):
    sqliteConnection = sqlite3.connect("trades.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result_of_query = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    return result_of_query


def get_all_products() -> list[tuple[str]]:
    query = """
    SELECT UPPER(title) FROM products;
    """
    return execute_query(query)


class Product:
    def __init__(self, id=None, title=None):
        self.id = id
        self.title = title
        self.name = title

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    def get_trades(self):
        query = f"""SELECT trades.* FROM trades
        INNER JOIN products ON trades.product_id = products.id
        WHERE products.title = '{str(self.title).upper()}'"""
        return execute_query(query)
