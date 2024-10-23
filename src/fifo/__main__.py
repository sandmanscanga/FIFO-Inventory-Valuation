from argparse import ArgumentParser, Namespace
from datetime import datetime
from queue import deque

from fifo import __version__


class Layer:
    def __init__(self, quantity: int, cost: float) -> None:
        self.quantity = quantity
        self.cost = cost

    def __str__(self) -> str:
        return f"({self.quantity} @ ${self.cost})"


class Buy:
    def __init__(self, layer: Layer, timestamp: datetime) -> None:
        self.layer = layer
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"[+] Buy: {self.layer} on {self.timestamp.strftime("%A")}"


class Sell:
    def __init__(self, quantity: int, timestamp: datetime) -> None:
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self) -> str:
        return f"[-] Sell: {self.quantity} on {self.timestamp.strftime("%A")}"


def calculate_fifo_valuation(
    cmdline: Namespace, product_id: str, target_date: datetime
) -> None:
    """
    Execute the main logic of the script.

    This function is the entry point of the script. It is
    responsible for parsing the command line arguments and
    executing the main logic of the script.

    Args:
        cmdline (Namespace): The parsed command line arguments.
    """

    # collect all of the buys
    # buys = [
    #     Buy(layer=Layer(10, 1.00), timestamp=Week.Monday),
    #     Buy(layer=Layer(20, 1.10), timestamp=Week.Tuesday),
    #     Buy(layer=Layer(30, 1.20), timestamp=Week.Thursday),
    #     Buy(layer=Layer(40, 1.30), timestamp=Week.Sunday),
    # ]
    # ! This will use the timestamp from each row
    buys = []

    # collect all of the sells
    # sells = [
    #     Sell(quantity=10, timestamp=Week.Wednesday),
    #     Sell(quantity=20, timestamp=Week.Friday),
    #     Sell(quantity=25, timestamp=Week.Saturday),
    # ]
    # ! This will use the timestamp from each row
    sells = []

    # aggregate the buys and sells
    book: list[Buy | Sell] = []
    book.extend(buys)
    book.extend(sells)

    book.sort(key=lambda x: x.timestamp)

    inventory = deque()
    for order in book:
        if order.timestamp <= cmdline.target_date:
            if isinstance(order, Buy):
                inventory.append(order.layer)

            elif isinstance(order, Sell):
                quantity_out = order.quantity  # quantity to sell

                while quantity_out > 0:
                    first_layer = inventory[0]  # first in

                    if first_layer.quantity > quantity_out:
                        first_layer.quantity -= quantity_out
                        quantity_out = 0  # awkward

                    elif first_layer.quantity <= quantity_out:
                        quantity_out -= first_layer.quantity
                        # we ran out of first layer
                        inventory.popleft()  # so pop it off

    if cmdline.verbose:
        print()
        print("#" * 80)
        print()

    if cmdline.verbose:
        print("Remaining inventory...")

    for thing in inventory:
        print(thing)


def main(cmdline: Namespace) -> None:
    """Execute the main logic of the script.

    This function is the entry point of the script. It is
    responsible for parsing the command line arguments and
    executing the main logic of the script. The main logic
    of the script is to calculate the FIFO valuation of a
    given product ID on a target date. The script reads the
    transactions from a CSV file and categorizes them by
    product ID. It then calculates the FIFO valuation for
    each product ID on the target date. The results are
    printed to the console. The script also prints the
    version of the application if the user requests it.

    Args:
        cmdline (Namespace): The parsed command line arguments.

    """

    # load the file into memory
    # evaluate target date, convert it to datetime
    # categorize the data into groups by product IDs
    # for each product ID...
    # ... calculate the FIFO valuation for the target date

    if cmdline.version:
        print(f"FIFO version {__version__}")
    else:
        print("The FIFO application is running.")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Specify the version flag to print the application's current version.",
    )
    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        default="data.csv",
        dest="filename",
        help="Path to the input CSV file containing the transactions",
    )
    parser.add_argument(
        "-t",
        "--target-date",
        type=str,
        default="1970-01-01",
        dest="target_date",
        help="Target date to calculate fifo valuation",
    )
    main(cmdline=parser.parse_args())
