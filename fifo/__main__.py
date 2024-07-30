"""
This module serves as the entry point for the FIFO application.

It contains the main function that is executed when the script is
run. Currently, it only prints a welcome message to the user. You
can also check the application version that is currently running.
"""

from argparse import ArgumentParser, Namespace

from fifo import __version__


def main(cmdline: Namespace) -> None:
    """
    Main function for the FIFO inventory valuation application.

    This function services as the entry point for the Katz
    application. There is a CLI parser that is used to parse
    command line arguments. The function currently prints a
    welcome message to the user and the version of the
    application if the user requests it.

    Args:
        cmdline (Namespace): The command line arguments parsed
        by the CLI parser.
    """
    if cmdline.version:
        print(f"FIFO version {__version__}")
    else:
        print("The FIFO application is running.")


if __name__ == "__main__":
    parser = ArgumentParser(
        description=(
            "The FIFO application, a solution for calculating FIFO "
            "inventory valuations based using Excel spreadsheets."
        )
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help=(
            "Specify the version flag to print the "
            "application's current version."
        ),
    )
    main(cmdline=parser.parse_args())
