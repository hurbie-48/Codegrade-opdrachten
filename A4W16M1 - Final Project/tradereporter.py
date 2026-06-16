from country import Country
from product import Product
import sqlite3


def execute_query(query: str):
    sqliteConnection = sqlite3.connect("trades.db")
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    sqliteConnection.close()
    return result

class Reporter:
    # 1 how many different products are there? -> int
    def total_amount_of_products(self) -> int:
        query = f"""
        SELECT COUNT(*) AS total_products FROM products;
        """
        result = execute_query(query)
        return result[0][0]

    # 2 which country has the most trade records? -> Country
    def country_with_most_trade_records(self) -> Country:
        raise NotImplementedError()

    # 3 which product has the highest total trade value? -> Product
    def product_with_highest_trade_value(self) -> Product:
        raise NotImplementedError()

    # 4 which country has the highest export trade value? -> Country
    def country_with_highest_export_value(self) -> Country:
        raise NotImplementedError()

    # 5 which country has the highest import trade value? -> Country
    def country_with_highest_import_value(self) -> Country:
        raise NotImplementedError()

    # 6 which country has the net highest trade value (export - import)? -> Country
    def country_with_highest_net_trade_value(self) -> Country:
        raise NotImplementedError()

    # 7 What is the average export export trade value per product for a given country? -> dict[str, float]
    def average_export_trade_value_per_product_for_country(
        self, country_id: str, report: bool = False
    ) -> dict[str, float]:
        raise NotImplementedError()

    # 9 Sort descending product by average value of export per MT -> list[tuple[Product, float]]
    def products_sorted_by_average_export_value_per_mt(
        self,
    ) -> list[tuple[Product, float]]:
        raise NotImplementedError()

    # 10 Report per country the total export, import value, export quantity, import quantity, and net trade value (export - import) -> list[tuple[Country, float, float, int, int, float]]
    # 11 when to_csv is True, also export the report to a csv file with the name "Trade report per country.csv" and the following columns: country_id, country_name, country_short_code, total_export_value, total_import_value, total_export_quantity, total_import_quantity, net_trade_value
    def trade_report_per_country(
        self, to_csv: bool = False
    ) -> list[tuple[Country, float, float, int, int, float]]:
        raise NotImplementedError()

    # 12 Get all countries that export more N MT per year on average -> list[Country]
    def countries_exporting_more_than_n_mt_per_year(self, n: float) -> list[Country]:
        raise NotImplementedError()
