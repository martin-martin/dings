import requests

BASE_URL = "https://www.stadtbibliothek.graz.at/"
OBJECT_DB_URL = "https://www.stadtbibliothek.graz.at/index.asp?mgrp-type=OBJ"
PAGE_QUERY_PARAM = "&page="


def get_html_page(url):
    """Get a HTML resource from the Web."""
    return requests.get(url).text
    

def save_html_page(url, filename):
    """Fetch a HTML resource from the Web and write it to a local file."""
    html = requests.get(url).text
    with open(f"{filename}.html", "w") as html_file:
        html_file.write(html)


def fetch_all_pages(base_url, number_of_pages):
    """Fetch all Dingeborg pages and save them to local files."""
    
    # TODO: Refactor to use temporary in-memory files

    for page_nr in range(1, number_of_pages + 1):
        if page_nr == 1:
            # Using the `&page=1` query parameter sends you to the wrong page
            # You need to use the BASE_URL without a `page` query parameter
            save_html_page(base_url, "page1")
        else:
            save_html_page(f"{base_url}{PAGE_QUERY_PARAM}{page_nr}", f"page{page_nr}")


if __name__ == "__main__":
    # save_html_page(BASE_URL, "index")
    fetch_all_pages(OBJECT_DB_URL, 7)