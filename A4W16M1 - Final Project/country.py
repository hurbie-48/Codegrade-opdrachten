import sqlite3


def execute_query(query:str):
    sqliteConnection = sqlite3.connect("trades.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    return result

class Country:

    # Representation method
    # This will format the output in the correct order
    # Format is @dataclass-style: Classname(attr=value, attr2=value2, ...)
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    def get_all_trades(self):
        query = f"""
            SELECT trades.* FROM trades
            INNER JOIN countries ON trades.from_country_id = countries.id
            WHERE countries.name = '{self.name}'
        """
        return execute_query(query)

    def get_from_trades(self):
        query = f"""
            SELECT trades.from_country_id FROM trades
            INNER JOIN countries ON trades.from_country_id = countries.id
            WHERE countries.name = '{self.name}'
        """
        return execute_query(query)

    def get_to_trades(self):
        query = f"""
               SELECT trades.to_country_id FROM trades
               INNER JOIN countries ON trades.from_country_id = countries.id
               WHERE countries.name = '{self.name}'
           """
        return execute_query(query)