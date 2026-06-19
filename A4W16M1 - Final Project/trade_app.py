import json
import sqlite3


def clean_numeric(value_str):
    if not value_str:
        return 0

    cleaned = (
        str(value_str)
        .replace("$", "")
        .replace("kg", "")
        .replace("MT", "")
        .strip()
    )

    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(",", "")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", "")

    try:
        num = float(cleaned)

        if "." in cleaned:
            decimal_part = cleaned.split(".")[1]
            decimal_val = int(decimal_part) if decimal_part.isdigit() else 0

            if decimal_val > 0 and len(decimal_part) <= 2:
                num = num * 1000

        return int(num)
    except ValueError:
        return 0


def nuke_and_rebuild_database(json_path, db_path):
    with open(json_path, "r") as file:
        json_data = json.load(file)

    if isinstance(json_data, dict):
        json_data = [json_data]

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM trades;")
    cursor.execute("DELETE FROM products;")
    cursor.execute("DELETE FROM countries;")
    conn.commit()

    for item in json_data:
        from_country_id = int(item["country_code"])
        from_country_name = item["country_name"]
        from_country_iso2 = item["country_iso2"]

        cursor.execute(
            "INSERT OR IGNORE INTO countries (id, name, short_code) VALUES (?, ?, ?)",
            (from_country_id, from_country_name, from_country_iso2),
        )
        for export in item.get("exports", []):
            trade_id = int(export["id"])
            year = int(export["year"])
            to_country_id = int(export["to"])

            quantity = clean_numeric(export["quantity"])
            value = clean_numeric(export["value"])

            product = export["product"]
            product_id = product["id"]
            product_title = str(product["description"]).upper().strip()

            cursor.execute(
                "INSERT OR IGNORE INTO products (id, title) VALUES (?, ?)",
                (product_id, product_title),
            )

            cursor.execute(
                """
                INSERT OR IGNORE INTO trades (id, product_id, Year, from_country_id, to_country_id, quantity, value)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    trade_id,
                    product_id,
                    year,
                    from_country_id,
                    to_country_id,
                    quantity,
                    value,
                ),
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    nuke_and_rebuild_database("trades.json", "trades.db")