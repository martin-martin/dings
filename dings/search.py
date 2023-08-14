from dings.database import search_available_item_in_database

items = [
    "Mikro",
    # "Bohrer",
    # "Buttonmaschine",
    # "Massagerolle"
]


def search_item(item_name, only_available=False):
    # Replace 'dinge.db' with the actual path to your SQLite database file
    db_name = "dinge.db"
    table_name = "dinge"

    search_results = search_available_item_in_database(db_name, table_name, item_name, only_available)

    if search_results:
        for row in search_results:
            print(row)
    else:
        print("No matching results found.")


if __name__ == "__main__":
    for item in items:
        search_item(item)