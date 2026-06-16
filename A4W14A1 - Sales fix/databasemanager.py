import json
import os
import sqlite3
import sys

# Beheert de databaseverbinding en voert SQL-queries uit.
class DatabaseManager:
    connection = None
    cursor = None

    def __init__(self, database: str) -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # Haalt één rij op uit de database.
    def fetchone(self, query: str, parameters=()) -> tuple:
        self.cursor.execute(query, parameters)
        return self.cursor.fetchone()

    # Haalt alle rijen op uit de database.
    def fetchall(self, query: str, parameters=()) -> list:
        self.cursor.execute(query, parameters)
        return self.cursor.fetchall()

    # Voegt gegevens toe en geeft het ID van de nieuwe rij terug.
    def insert(self, query: str, parameters) -> int:
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    # Werkt bestaande gegevens bij in de database.
    def update(self, query: str, parameters=()) -> bool:
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.rowcount > 0

    # Verwijdert gegevens uit de database.
    def delete(self, query: str, parameters=()) -> bool:
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.rowcount > 0

    # Sluit de verbinding met de database.
    def close(self):
        if self.connection:
            self.connection.close()

    # Slaat de huidige databasegegevens op in een JSON-bestand.
    def backup_to_json(self, filename: str) -> None:
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        backup = dict()

        for table in self.cursor.fetchall():
            table_name = table[0]
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()

            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [(column[1], column[2], column[4], column[5]) for column in self.cursor.fetchall()]

            backup[table_name] = {"columns": columns, "rows": rows}

        with open(os.path.join(sys.path[0], filename), 'w', encoding='utf-8') as file:
            json.dump(backup, file, indent=4)

    # Herstelt de databasegegevens vanuit een JSON-bestand.
    def restore_from_json(self, filename: str) -> None:
        with open(os.path.join(sys.path[0], filename), 'r', encoding='utf-8') as file:
            backup = json.load(file)

        for table_name, table_data in backup.items():
            columns = table_data["columns"]
            rows = table_data["rows"]

            definitions = ", ".join([
                f"{column[0]} {column[1]}" +
                (f" DEFAULT {column[2]}" if column[2] is not None else "") +
                (" PRIMARY KEY" if column[3] else "") +
                (" AUTOINCREMENT" if column[3] and column[1].upper() == "INTEGER" else "")
                for column in columns])
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({definitions})")
            self.cursor.execute(f"DELETE FROM {table_name}")

            for row in rows:
                placeholders = ", ".join([f":{column[0]}" for column in columns])
                insert_query = f"INSERT INTO {table_name} ({', '.join([col[0] for col in columns])}) VALUES ({placeholders})"
                self.cursor.execute(insert_query, {column[0]: value for column, value in zip(columns, row)})

        self.connection.commit()

    # Sluit de database automatisch af wanneer het object wordt opgeruimd.
    def __del__(self):
        self.close()