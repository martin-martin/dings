import re

import bs4

from dings.database import (add_tuple_to_database, create_table_if_not_exists,
                      drop_database)
from dings.fetch import BASE_URL, OBJECT_DB_URL, fetch_all_pages, get_html_page


def get_last_page():
    """Find the last page number."""
    html = get_html_page(OBJECT_DB_URL)
    soup = bs4.BeautifulSoup(html, features="html.parser")
    last_page = soup.find("a", string="Ende")
    page_number_in_url = re.compile(r"page=(\d+)")

    last_page_number = re.search(page_number_in_url, last_page["href"]).group(1)
    return last_page_number


def get_items_from_page(page_number):
    with open(f"page{page_number}.html") as html_file:
        html = html_file.read()
    soup = bs4.BeautifulSoup(html, features="html.parser")
    all_items = soup.find_all("a", class_="list-group-item")

    items_tuples = []
    for item in all_items:
        if "lightred" in item.get("class"):  # BORROWED
            items_tuples.append((_process_text(item.text), 0, f"{BASE_URL}{item['href']}"))
        else:  # AVAILABLE
            items_tuples.append((_process_text(item.text), 1, f"{BASE_URL}{item['href']}"))
    
    return items_tuples


def _process_text(text):
    if text[-6:] == "Objekt":
        text = text[:-6]
    return text


def combine_all_page_items(last_page_number):
    all_items_from_all_pages = []
    for page_number in range(1, last_page_number + 1):  # Offset 0-based indexing
        all_items_from_all_pages.extend(get_items_from_page(page_number))
    return all_items_from_all_pages


def refresh_database():
    drop_database("dinge.db")

    last_page_number = int(get_last_page())

    fetch_all_pages(OBJECT_DB_URL, last_page_number)

    create_table_if_not_exists()
    all_items_tuples = combine_all_page_items(last_page_number)

    for item_tuple in all_items_tuples:
        add_tuple_to_database(item_tuple)


if __name__ == "__main__":
    refresh_database()