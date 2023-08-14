# Dingeborg

Search the online Graz library for things called _Dingeborg_ for specific items.

The online user interface of the library for things isn't that great. For convenience, this CLI app can fetch the current catalogue and allows you to search for things, optionally filtering for whether they are currently available to borrow, or not.

## Usage

```bash
$ python dings <search_term> [-d] [-r]
```

```text
usage: __main__.py [-h] [-d] [-r] item

positional arguments:
  item           Item to look for in Dingeborg

options:
  -h, --help     show this help message and exit
  -d, --da       Only show items that are currently available
  -r, --refresh  Fetch current data
```

## TODO

- [ ] Replace the HTML file generation with temporary in-memory files
- [ ] Maybe figure out how to check in SQLite and update records instead of dropping
- [x] Create a search script where we can look for specific items in the text description
      to find out whether they're currently available
- [x] Maybe remove "Objekt" from the right end of the string
- [ ] Maybe make a settings.toml file for defining the search objects, for recurrent search
- [x] Maybe add a cli script to search from the CLI
- [x] Also, give options of whether to show currently unavailable items or not
- [x] Add a CLI option to refresh the DB
- [x] Add page number (or even the direct URL) for quick borrowing
- [x] Make it case insensitive
- [ ] Package it somehow so that Elias can run it
- [x] Define `pyproject.toml` and an entry script
- [ ] ...
