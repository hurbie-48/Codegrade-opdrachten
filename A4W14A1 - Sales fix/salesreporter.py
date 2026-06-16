from databasemanager import DatabaseManager

# Genereert verkooprapportages en overzichten in tabelvorm.
class SalesReporter:
    def __init__(self, databasemanager: DatabaseManager) -> None:
        self.db = databasemanager

    # Telt het totale aantal verkooptransacties.
    def sales_amount(self) -> int:
        result = self.db.fetchone("SELECT COUNT(*) FROM sales")
        return int(result[0])

    # Berekent de totale omzet van alle verkopen samen.
    def total_sales(self) -> float:
        result = self.db.fetchone("SELECT SUM(price * quantity) FROM sales")
        return round(float(result[0] or 0.0), 2)

    # Maakt een overzichtstabel van de verkoopcijfers per product.
    def sales_by_product(self) -> str:
        rows = self.db.fetchall("""
            SELECT p.name, SUM(s.quantity), ROUND(SUM(s.price * s.quantity), 2)
            FROM sales s
            JOIN products p ON s.product_id = p.id
            GROUP BY p.id
            ORDER BY p.id
        """)
        return self.display_table(["Product", "Quantity", "Sales"], rows)

    # Maakt een overzichtstabel van de verkoopcijfers per klant.
    def sales_by_customer(self) -> str:
        rows = self.db.fetchall("""
            SELECT c.name, SUM(s.quantity), ROUND(SUM(s.price * s.quantity), 2)
            FROM sales s
            JOIN customers c ON s.customer_id = c.id
            GROUP BY c.id
            ORDER BY c.id
        """)
        return self.display_table(["Customer", "Quantity", "Sales"], rows)

    # Maakt een overzichtstabel van de omzet per datum.
    def sales_over_time(self) -> str:
        rows = self.db.fetchall("""
            SELECT date, ROUND(SUM(price * quantity), 2)
            FROM sales
            GROUP BY date
            ORDER BY date
        """)
        return self.display_table(["Date", "Sales"], rows)

    # Toont een tabel met de meest verkochte producten.
    def top_selling_products(self, amount: int = 5) -> str:
        rows = self.db.fetchall("""
            SELECT p.name, SUM(s.quantity)
            FROM sales s
            JOIN products p ON s.product_id = p.id
            GROUP BY p.id
            ORDER BY SUM(s.quantity) DESC, p.id ASC
            LIMIT ?
        """, (amount,))
        return self.display_table(["Product", "Quantity"], rows)

    # Toont een tabel met de klanten die het meeste geld hebben uitgegeven.
    def top_customers(self, amount: int = 5) -> str:
        rows = self.db.fetchall("""
            SELECT c.name, ROUND(SUM(s.price * s.quantity), 2)
            FROM sales s
            JOIN customers c ON s.customer_id = c.id
            GROUP BY c.id
            ORDER BY SUM(s.price * s.quantity) DESC, c.id ASC
            LIMIT ?
        """, (amount,))
        return self.display_table(["Customer", "Sales"], rows)

    # Vormt gegevens om tot een netjes uitgelijnde teksttabel.
    def display_table(self, headers: list, rows: list) -> str:
        column_widths: list = [max(len(str(item)) for item in column) for column in zip(*([headers] + list(rows)))]
        row_format: str = " | ".join(["{{:<{}}}".format(width) for width in column_widths])
        table: list = list()

        table.append(row_format.format(*headers))
        table.append("-+-".join(['-' * width for width in column_widths]))

        for row in rows:
            table.append(row_format.format(*row))

        return "\n".join(table)