import argparse


def parse_args() -> argparse.Namespace:
    """Parse command-line input."""
    parser = argparse.ArgumentParser()
    parser.add_argument("item", type=str, help="Item to look for in Dingeborg")
    parser.add_argument("-d", "--da", action="store_true", help="Only show items that are currently available")
    parser.add_argument("-r", "--refresh", action="store_true", help="Fetch current data")
    return parser.parse_args()
