import sqlite3


def execute_query(query: str):
    sqliteConnection = sqlite3.connect("trades.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result_of_query = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    return result_of_query


class Country:

    def __init__(self, id=None, name=None, short_code=None):
        self.id = id
        self.name = name
        self.short_code = short_code

    def __repr__(self) -> str:
        sorted_items = sorted(self.__dict__.items(), key=lambda item: item[0])
        return "{}({})".format(
            type(self).__name__,
            ", ".join([f"{key}={value!s}" for key, value in sorted_items]),
        )

    def get_all_trades(self):
        query = f"""
            SELECT * FROM trades
            WHERE CAST(from_country_id AS TEXT) = '{self.id}'
               OR CAST(to_country_id AS TEXT) = '{self.id}'
               OR UPPER(TRIM(to_country_id)) = '{str(self.short_code).upper()}'
        """
        return execute_query(query)

    def get_from_trades(self):
        query = f"""
            SELECT * FROM trades
            WHERE CAST(from_country_id AS TEXT) = '{self.id}'
        """
        return execute_query(query)

    def get_to_trades(self):
        query = f"""
            SELECT * FROM trades
            WHERE CAST(to_country_id AS TEXT) = '{self.id}'
               OR UPPER(TRIM(to_country_id)) = '{str(self.short_code).upper()}'
        """
        return execute_query(query)
