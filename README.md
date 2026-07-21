# Small Business Sales Calculator SL

## Overview

The **Small Business Sales Calculator SL** is a Python-based command-line application developed to demonstrate fundamental programming concepts while addressing a simple business problem. The system enables users to record sales transactions, automatically calculate discounts and taxes, and generate summary statistics to support basic sales management.

The application was developed using core Python features without external libraries, making it suitable as an introductory programming project for students learning structured programming, input validation, modular programming, and financial calculations.

---

## Objectives

The primary objectives of this project are to:

* Automate sales transaction calculations.
* Minimize human error in tax and discount computations.
* Demonstrate the use of Python functions and modular programming.
* Implement robust user input validation.
* Provide basic sales reporting and revenue analysis.
* Reinforce fundamental programming concepts through a real-world business scenario.

---

## Features

The system provides the following functionality:

* Record new sales transactions.
* Validate user input to prevent invalid or incomplete data.
* Automatically calculate:

  * Sales subtotal
  * Quantity-based discount
  * Applicable tax
  * Final payable amount
* Store sales records during program execution.
* Display all recorded transactions.
* Generate a business summary including:

  * Total number of transactions
  * Total revenue
  * Average revenue per transaction

---

## Business Rules

The application follows the business rules below:

| Rule                 |        Value |
| -------------------- | -----------: |
| Tax Rate             |          15% |
| Discount Rate        |          10% |
| Discount Eligibility | Quantity ≥ 5 |

### Calculation Process

For every transaction, the system performs calculations in the following order:

1. **Subtotal** = Unit Price × Quantity
2. **Discount** = 10% of the subtotal (only if quantity is five or more)
3. **Tax** = 15% of the discounted subtotal
4. **Total Amount** = (Subtotal − Discount) + Tax

---

## Program Structure

The application is organized into modular functions, each responsible for a specific task.

| Function               | Description                                                             |
| ---------------------- | ----------------------------------------------------------------------- |
| `get_string()`         | Validates text input to ensure it is not empty.                         |
| `get_positive_float()` | Accepts and validates positive decimal values for product prices.       |
| `get_positive_int()`   | Accepts and validates positive integer values for product quantities.   |
| `add_sale()`           | Records a sales transaction and performs all financial calculations.    |
| `view_sales()`         | Displays all recorded sales transactions.                               |
| `summary()`            | Generates summary statistics, including revenue and average sale value. |
| `main()`               | Controls the application's menu-driven interface and program execution. |

---

## Input Validation

To ensure data integrity, the application implements validation mechanisms that:

* Reject empty product names.
* Prevent negative or zero prices.
* Prevent invalid quantities.
* Handle non-numeric input using exception handling (`try-except`).
* Prompt users to re-enter invalid values until acceptable input is provided.

---

## Technologies Used

* **Programming Language:** Python 3
* **Programming Paradigm:** Structured Programming
* **Interface:** Command-Line Interface (CLI)

No third-party libraries or frameworks are required.

---

## Example Execution

```text
Small Business Sales Calculator SL

1. Add Sale
2. View Sales
3. Summary
4. Exit

Choice: 1

Product name: Rice
Unit price (SLL): 500
Quantity sold: 6

Subtotal : SLL 3,000.00
Discount : SLL 300.00
Tax (15%) : SLL 405.00
TOTAL : SLL 3,105.00
```

---

## Project Limitations

The current implementation has several limitations:

* Sales records are stored only in memory.
* Data is lost when the application terminates.
* The application supports only a single user.
* Records cannot be edited or deleted.
* No persistent database or file storage is implemented.
* Reporting capabilities are limited to basic summary statistics.

---

## Future Enhancements

Potential improvements include:

* Persistent storage using JSON, CSV, or SQLite.
* Customer management functionality.
* Product inventory management.
* Search, update, and delete operations.
* Receipt generation.
* Sales reporting by date or product.
* Graphical User Interface (GUI) using Tkinter.
* Export reports to PDF or Excel.
* User authentication and role-based access control.

---

## Learning Outcomes

This project demonstrates practical application of the following programming concepts:

* Variables and constants
* Functions and modular programming
* Lists and dictionaries
* Conditional statements
* Iteration using loops
* Exception handling
* Input validation
* Basic financial calculations
* Menu-driven program design

---

## Requirements

* Python 3.8 or later
* Any operating system capable of running Python (Windows, macOS, or Linux)

---

## Running the Application

1. Clone the repository:

```bash
git clone https://github.com/yourusername/your-repository.git
```

2. Navigate to the project directory:

```bash
cd your-repository
```

3. Execute the program:

```bash
python sales_calculator.py
```

---

## License

This project is distributed under the **MIT License**. You are free to use, modify, and distribute this software in accordance with the terms of the license.
