from databasemanager import DatabaseManager

# Beheert het toevoegen, aanpassen, ophalen en verwijderen van databasegegevens.
class SalesManager:
    def __init__(self, databasemanager: DatabaseManager) -> None:
        self.db = databasemanager

    # Haalt een specifieke verkoop op via het ID.
    def get_sale(self, sale_id: int) -> tuple:
        return self.db.fetchone("SELECT * FROM sales WHERE id = ?", (sale_id,))

    # Voegt een nieuwe verkoop toe en geeft het ID terug.
    def add_sale(self, date: str, product_id: int, customer_id: int, quantity: int, price: float) -> int:
        return self.db.insert(
            "INSERT INTO sales (date, product_id, customer_id, quantity, price) VALUES (?, ?, ?, ?, ?)",
            (date, product_id, customer_id, quantity, round(price, 2))
        )

    # Werkt een bestaande verkoop bij in de database.
    def update_sale(self, sale_id: int, date: str, product_id: int, customer_id: int, quantity: int, price: float) -> bool:
        return self.db.update(
            "UPDATE sales SET date = ?, product_id = ?, customer_id = ?, quantity = ?, price = ? WHERE id = ?",
            (date, product_id, customer_id, quantity, round(price, 2), sale_id)
        )

    # Verwijdert een verkoop uit de database via het ID.
    def delete_sale(self, sale_id: int) -> bool:
        return self.db.delete("DELETE FROM sales WHERE id = ?", (sale_id,))

    # Haalt een specifieke klant op via het ID.
    def get_customer(self, customer_id: int) -> tuple:
        return self.db.fetchone("SELECT * FROM customers WHERE id = ?", (customer_id,))

    # Voegt een nieuwe klant toe en geeft het ID terug.
    def add_customer(self, name: str, email: str) -> int:
        return self.db.insert(
            "INSERT INTO customers (name, email) VALUES (?, ?)",
            (name, email)
        )

    # Werkt de gegevens van een bestaande klant bij.
    def update_customer(self, customer_id: int, name: str, email: str) -> bool:
        return self.db.update(
            "UPDATE customers SET name = ?, email = ? WHERE id = ?",
            (name, email, customer_id)
        )

    # Verwijdert een klant uit de database via het ID.
    def delete_customer(self, customer_id: int) -> bool:
        return self.db.delete("DELETE FROM customers WHERE id = ?", (customer_id,))

    # Haalt een specifiek product op via het ID.
    def get_product(self, product_id: int) -> tuple:
        return self.db.fetchone("SELECT * FROM products WHERE id = ?", (product_id,))

    # Voegt een nieuw product toe en geeft het ID terug.
    def add_product(self, name: str, category: str) -> int:
        return self.db.insert(
            "INSERT INTO products (name, category) VALUES (?, ?)",
            (name, category)
        )

    # Werkt de gegevens van een bestaand product bij.
    def update_product(self, product_id: int, name: str, category: str) -> bool:
        return self.db.update(
            "UPDATE products SET name = ?, category = ? WHERE id = ?",
            (name, category, product_id)
        )

    # Verwijdert een product uit de database via het ID.
    def delete_product(self, product_id: int) -> bool:
        return self.db.delete("DELETE FROM products WHERE id = ?", (product_id,))