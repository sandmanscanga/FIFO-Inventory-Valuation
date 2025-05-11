# FIFO Inventory Valuation (fifo) [0.1.0]

A Python package for calculating inventory valuation using the FIFO (First In, First Out) method. This package processes buy and sell transactions to determine the remaining inventory as of a specified date.

## Features

- **FIFO Logic**: Implements the FIFO method to manage inventory layers.
- **Transaction Support**: Handles both buy and sell transactions.
- **Customizable Evaluation Date**: Allows users to specify a date for inventory valuation.
- **Verbose Mode**: Provides detailed output for debugging and analysis.

## Key Concepts

### Layer

Represents a unit of inventory with the following attributes:

- **Quantity**: The number of items in the layer.
- **CPU**: Cost per unit of the items in the layer.

### Buy

Represents a purchase transaction that adds a new layer to the inventory.

Attributes:

- **Layer**: The inventory layer created by the buy transaction.
- **Timestamp**: The date and time of the transaction.

### Sell

Represents a sale transaction that reduces inventory.

Attributes:

- **Quantity**: The number of items sold.
- **Timestamp**: The date and time of the transaction.

## How It Works

1. **Buy Transactions**: Each buy transaction adds a new layer to the inventory.
2. **Sell Transactions**: Each sell transaction reduces inventory, starting with the oldest layer.
3. **Moment of Evaluation**: The script calculates the remaining inventory as of a user-specified date.

### Process Overview

- **Initial Inventory**: The script initializes the inventory with predefined buy transactions.
- **Buys**: Each buy transaction creates a new layer in the inventory.

  ```python
  Buy(layer=Layer(10, 1.00), timestamp=Week.Monday)
  ```

- **Sells**: Each sell transaction reduces inventory, starting with the oldest layer (FIFO).

  ```python
  Sell(quantity=10, timestamp=Week.Wednesday)
  ```

- **Moment of Evaluation**: The script calculates the remaining inventory as of a specific date.

  - **Input**: The day of the week specified by the user.
  - **Output**: Remaining inventory layers, sorted by FIFO.

### Script Features

- **Verbose Mode**: When enabled, the script provides detailed output, including:
  - Transactions before and after sorting.
  - Remaining inventory after processing all transactions.
- **Sorting**: Transactions are sorted by their timestamps to ensure proper processing order.
- **FIFO Logic**: The script uses a deque to manage inventory layers, ensuring that the oldest layers are processed first during sales.

## Usage

Run the script using the following command:

```bash
python -m fifo -d <day_of_week> [-v]
```

### Arguments

- `-d`, `--day-of-week`: Specifies the day of the week for inventory valuation (e.g., Monday, Tuesday). Defaults to `Sunday`.
- `-v`, `--verbose`: Enables verbose output for detailed transaction and inventory information.
- `--version`: Displays the current version of the application.

### Example

```bash
python -m fifo -d Friday -v
```

This command calculates the inventory valuation as of Friday and provides detailed output.

## Example Output

### Input Transactions

**Buys:**

- [+] Buy: (10 @ $1.00) on Monday
- [+] Buy: (20 @ $1.10) on Tuesday
- [+] Buy: (30 @ $1.20) on Thursday
- [+] Buy: (40 @ $1.30) on Sunday

**Sells:**

- [-] Sell: 10 on Wednesday
- [-] Sell: 20 on Friday
- [-] Sell: 25 on Saturday

### Remaining Inventory (as of Friday)

- (10 @ $1.20)
- (40 @ $1.30)

## Requirements

- Python 3.13 or higher

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
