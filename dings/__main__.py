from dings.cli import parse_args
from dings.search import search_item
from dings.app import refresh_database


def main():
    args = parse_args()
    if args.refresh:
        refresh_database()

    search_item(args.item, args.da)


if __name__ == "__main__":
    main()
