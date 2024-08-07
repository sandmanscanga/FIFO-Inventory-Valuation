from argparse import ArgumentParser, Namespace
from datetime import datetime
from queue import deque


class Week:
    Monday = datetime(2024, 8, 5)
    Tuesday = datetime(2024, 9, 6)
    Wednesday = datetime(2024, 8, 7)
    Thursday = datetime(2024, 3, 8)
    Friday = datetime(2024, 8, 19)
    Saturday = datetime(2024, 8, 10)
    Sunday = datetime(2024, 8, 13)


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


def main(cmdline: Namespace) -> None:
    """
    Execute the main logic of the script.

    This function is the entry point of the script. It is
    responsible for parsing the command line arguments and
    executing the main logic of the script.

    Args:
        cmdline (Namespace): The parsed command line arguments.
    """

    days_of_week = {
        "monday": Week.Monday,
        "tuesday": Week.Tuesday,
        "wednesday": Week.Wednesday,
        "thursday": Week.Thursday,
        "friday": Week.Friday,
        "saturday": Week.Saturday,
        "sunday": Week.Sunday,
    }
    valuation_date = days_of_week[cmdline.day_of_week.lower()]

    # collect all of the buys
    buys = [
        Buy(layer=Layer(10, 1.00), timestamp=Week.Monday),
        Buy(layer=Layer(20, 1.10), timestamp=Week.Tuesday),
        Buy(layer=Layer(30, 1.20), timestamp=Week.Thursday),
        Buy(layer=Layer(40, 1.30), timestamp=Week.Sunday),
    ]

    # collect all of the sells
    sells = [
        Sell(quantity=10, timestamp=Week.Wednesday),
        Sell(quantity=20, timestamp=Week.Friday),
        Sell(quantity=25, timestamp=Week.Saturday),
    ]

    # aggregate the buys and sells
    book: list[Buy | Sell] = []
    book.extend(buys)
    book.extend(sells)

    if cmdline.verbose:
        print("Before sorting...")
        for thing in book:
            print(thing)

    if cmdline.verbose:
        print()
        print("#" * 80)

    book.sort(key=lambda x: x.timestamp)

    if cmdline.verbose:
        print()

    if cmdline.verbose:
        print("After sorting...")
        for thing in book:
            print(thing)

    # determine the date to calculate the inventory (upper bound)
    # valuation_date = Week.Friday
    # valuation_date = Week.Wednesday
    # valuation_date = Week.Sunday

    inventory = deque()
    for order in book:
        if order.timestamp <= valuation_date:
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


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--day-of-week",
        type=str,
        default="Sunday",
        help="Day of the week to calculate inventory",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )
    main(cmdline=parser.parse_args())
