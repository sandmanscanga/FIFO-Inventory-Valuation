"""
This module serves as the entry point for the FIFO application.

It contains the main function that is executed when the script is
run. The application calculates FIFO inventory valuations based on
provided transactions and a specified day of the week.
"""

import logging
from argparse import ArgumentParser, Namespace
from collections import deque
from datetime import datetime
from typing import Dict, List, Union

from fifo import __version__

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class Week:
    """
    Represents specific dates for each day of the week.

    Attributes:
        Monday (datetime): Date for Monday.
        Tuesday (datetime): Date for Tuesday.
        Wednesday (datetime): Date for Wednesday.
        Thursday (datetime): Date for Thursday.
        Friday (datetime): Date for Friday.
        Saturday (datetime): Date for Saturday.
        Sunday (datetime): Date for Sunday.
    """

    Monday = datetime(2024, 8, 5)
    Tuesday = datetime(2024, 8, 6)
    Wednesday = datetime(2024, 8, 7)
    Thursday = datetime(2024, 8, 8)
    Friday = datetime(2024, 8, 9)
    Saturday = datetime(2024, 8, 10)
    Sunday = datetime(2024, 8, 11)


class Layer:
    """
    Represents a layer of inventory with a specific quantity and cost per unit.

    Attributes:
        quantity (int): The number of items in the layer.
        cost (float): The cost per unit of the items in the layer.
    """

    def __init__(self, quantity: int, cost: float) -> None:
        """
        Initializes a Layer instance.

        Args:
            quantity (int): The number of items in the layer.
            cost (float): The cost per unit of the items in the layer.
        """
        self.quantity = quantity
        self.cost = cost

    def __str__(self) -> str:
        """
        Returns a string representation of the Layer instance.

        Returns:
            str: A string in the format "(quantity @ $cost)".
        """
        return f"({self.quantity} @ ${self.cost:.2f})"


class Buy:
    """
    Represents a buy transaction that adds a layer to the inventory.

    Attributes:
        layer (Layer): The inventory layer created by the buy transaction.
        timestamp (datetime): The date and time of the transaction.
    """

    def __init__(self, layer: Layer, timestamp: datetime) -> None:
        """
        Initializes a Buy instance.

        Args:
            layer (Layer): The inventory layer created by the buy transaction.
            timestamp (datetime): The date and time of the transaction.
        """
        self.layer = layer
        self.timestamp = timestamp

    def __str__(self) -> str:
        """
        Returns a string representation of the Buy instance.

        Returns:
            str: A string in the format "[+] Buy: layer on day".
        """
        return f"[+] Buy: {self.layer} on {self.timestamp.strftime('%A')}"


class Sell:
    """
    Represents a sell transaction that reduces inventory.

    Attributes:
        quantity (int): The number of items sold.
        timestamp (datetime): The date and time of the transaction.
    """

    def __init__(self, quantity: int, timestamp: datetime) -> None:
        """
        Initializes a Sell instance.

        Args:
            quantity (int): The number of items sold.
            timestamp (datetime): The date and time of the transaction.
        """
        self.quantity = quantity
        self.timestamp = timestamp

    def __str__(self) -> str:
        """
        Returns a string representation of the Sell instance.

        Returns:
            str: A string in the format "[-] Sell: quantity on day".
        """
        return f"[-] Sell: {self.quantity} on {self.timestamp.strftime('%A')}"


def calculate_inventory(
    book: List[Union[Buy, Sell]], valuation_date: datetime
) -> deque:
    """
    Calculate the remaining inventory based on transactions and valuation date.

    Args:
        book (List[Union[Buy, Sell]]): List of buy and sell transactions.
        valuation_date (datetime): The date for inventory valuation.

    Returns:
        deque: The remaining inventory as a deque of layers.
    """

    inventory = deque()
    for order in book:
        if order.timestamp <= valuation_date:
            if isinstance(order, Buy):
                inventory.append(order.layer)

            elif isinstance(order, Sell):
                quantity_out = order.quantity

                while quantity_out > 0 and inventory:
                    first_layer = inventory[0]

                    if first_layer.quantity > quantity_out:
                        first_layer.quantity -= quantity_out
                        quantity_out = 0

                    elif first_layer.quantity <= quantity_out:
                        quantity_out -= first_layer.quantity
                        inventory.popleft()

    return inventory


def main(cmdline: Namespace) -> None:
    """
    Execute the main logic of the script.

    Args:
        cmdline (Namespace): The parsed command line arguments.

    Raises:
        ValueError: If an invalid day of the week is provided.
    """
    days_of_week: Dict[str, datetime] = {
        "monday": Week.Monday,
        "tuesday": Week.Tuesday,
        "wednesday": Week.Wednesday,
        "thursday": Week.Thursday,
        "friday": Week.Friday,
        "saturday": Week.Saturday,
        "sunday": Week.Sunday,
    }
    valuation_date = days_of_week.get(cmdline.day_of_week.lower())

    if not valuation_date:
        logger.error("Invalid day of the week: %s", cmdline.day_of_week)
        raise ValueError(f"Invalid day of the week: {cmdline.day_of_week}")

    buys: List[Buy] = [
        Buy(layer=Layer(10, 1.00), timestamp=Week.Monday),
        Buy(layer=Layer(20, 1.10), timestamp=Week.Tuesday),
        Buy(layer=Layer(30, 1.20), timestamp=Week.Thursday),
        Buy(layer=Layer(40, 1.30), timestamp=Week.Sunday),
    ]

    sells: List[Sell] = [
        Sell(quantity=10, timestamp=Week.Wednesday),
        Sell(quantity=20, timestamp=Week.Friday),
        Sell(quantity=25, timestamp=Week.Saturday),
    ]

    book: List[Union[Buy, Sell]] = []
    book.extend(buys)
    book.extend(sells)

    if cmdline.verbose:
        logger.info("Before sorting...")
        for thing in book:
            logger.info(thing)

    if cmdline.verbose:
        logger.info("\n%s", "#" * 80)

    book.sort(key=lambda transaction: transaction.timestamp)

    if cmdline.verbose:
        logger.info("After sorting...")
        for transaction in book:
            logger.info(transaction)

    inventory = calculate_inventory(book, valuation_date)

    if cmdline.verbose:
        logger.info("\n%s\n", "#" * 80)

    if cmdline.verbose:
        logger.info("Remaining inventory...")

    for transaction in inventory:
        logger.info(transaction)


if __name__ == "__main__":
    parser = ArgumentParser(
        description=(
            "The FIFO application, a solution for calculating FIFO "
            "inventory valuations based using Excel spreadsheets."
        )
    )
    parser.add_argument(
        "-d",
        "--day-of-week",
        type=str,
        default="Sunday",
        help="Day of the week to calculate inventory",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help=(
            "Specify the version flag to print the application's "
            "current version."
        ),
    )
    args = parser.parse_args()

    if args.version:
        logger.info("FIFO version %s", __version__)
    else:
        main(cmdline=args)
