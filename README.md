# CLI Inventory Management System

The CLI Inventory Management System is a command-line application built in Python to help small businesses track their inventory, manage suppliers, and handle basic user authentication. It uses a local MySQL database to store product data, user roles, and supplier details. The current implementation focuses on providing a functional interface for core inventory workflows such as stock monitoring, product modification, and supplier tracking, directly from the terminal.

## Table of Contents
- [About the Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Folder Structure](#folder-structure)
- [Important Code Concepts](#important-code-concepts)
- [Architectural Decisions](#architectural-decisions)
- [Data Model](#data-model)
- [Main User Flows](#main-user-flows)
- [Setup Instructions](#setup-instructions)
- [Future Improvements](#future-improvements)
- [Learning Outcomes](#learning-outcomes)
- [License](#license)

## About the Project

Managing inventory manually is error-prone, especially when keeping track of different suppliers, varying stock levels, and multiple employees making changes. This project addresses those challenges by providing a terminal-based interface connected to a persistent local MySQL database.

The application is intended for managers and employees who need a fast, low-overhead tool to check stock, add incoming shipments, and verify product details. The current implementation relies on local state and a local MySQL instance, making it useful as a prototype to test the data model and workflows before potentially building out a web-based frontend or cloud database.

## Key Features

### User Authentication
Users can either log in or create a new account. The system prompts for a username, name, role, and password, ensuring that only authorized individuals can access the inventory dashboard.

### Inventory Management
Once logged in, users can perform full CRUD operations on the inventory:
- **View Products:** Displays a table of all products, their cost price, selling price, and current inventory levels.
- **Add Products:** Prompts the user for a 6-digit product ID, name, supplier, cost, and initial stock count.
- **Modify Products:** Allows users to selectively update a product's name, supplier, cost price, selling price, or add to its existing stock.
- **Delete Products:** Removes a product entirely from the system using its ID.

### Stock Alerting
The system proactively alerts the user about low-stock items. When the main inventory screen is accessed, a query runs to check if any products have an inventory count below 10 and prints a warning for those items.

### Supplier Management
Users can view all products associated with a specific supplier or completely remove a supplier from the database (which cascades to their products based on the current implementation).

### Transaction Stub
The application contains the initial logic and table creation (`Transactions`) to track daily sales, quantities, and profit/loss. This flow is partially integrated and exists as a separate transaction menu.

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python | Core application logic and CLI interaction |
| Database | MySQL | Persistent data storage for products, users, and transactions |
| DB Driver | `mysql-connector-python` | Facilitates the connection and queries between Python and MySQL |
| Environment | `python-dotenv` | Manages environment variables (such as the database password) |

## System Architecture

The application uses a straightforward CLI-to-database architecture. The user interacts with the terminal running `main.py`, which delegates specific workflows (like inventory or supplier management) to modular scripts in the `Functions` directory. These functions execute parameterized SQL queries using a shared database cursor, and the results are printed back to the terminal.

```txt
User
  ↓
CLI Terminal (main.py)
  ↓
Domain Modules (inventory.py / supplier.py / transaction.py)
  ↓
MySQL Database (Products / Users / Transactions)
```

## Folder Structure

```txt
.
├── Functions/
│   ├── inventory.py       # Handles CRUD operations and low stock alerts
│   ├── supplier.py        # Logic for fetching and removing supplier data
│   └── transaction.py     # Stubs for handling sales volume and profit/loss
├── .env                   # Environment variables (password)
├── main.py                # Main application loop, database setup, and routing
├── requirments.txt        # Python dependencies
└── README.md              # Project documentation
```

## Important Code Concepts

### Parameterized SQL Queries
To prevent SQL injection and ensure safe data handling, the codebase relies on parameterized queries (`%s` placeholders) when inserting or querying data based on user input.

### Shared Database Cursor
Instead of opening a new database connection for every operation, `main.py` establishes a connection on startup and passes the connection object (`test_connection`) and cursor (`cur`) into the imported functions. This improves performance and ensures transactions are committed correctly.

### Direct Terminal Routing
The application acts as its own router. Using `while True` loops and simple conditional logic, it captures input and routes the user into specific sub-menus (like the main inventory menu or the transactions menu).

## Architectural Decisions

### CLI-First Approach
The application is built completely within the terminal. Given the goal of testing the core data model and CRUD operations, building a CLI avoids the overhead of a frontend framework. This makes sense for a prototype stage where validating the database schema and query logic is the main priority.

### Local MySQL Database
Using a local MySQL instance instead of a file-based database (like SQLite) or a cloud database ensures the schema (`CREATE TABLE IF NOT EXISTS`) and data types are tested in a robust relational database environment. It paves the way for migrating to a managed SQL database later without rewriting the queries.

### Modular `Functions` Directory
Instead of placing all logic in `main.py`, the code separates concerns by placing domain-specific logic (inventory vs. suppliers) into their own files. This makes the codebase easier to read, test, and extend.

## Data Model

### Users
Tracks authorized individuals. It stores `USERID` (a randomly generated 6-digit number), `USERNAME`, `PASSWORD`, `ROLE`, and `NAME`.

### Products
The core entity of the application. It uses a 6-digit `PRODUCT_ID` as the primary key and tracks `PRODUCT_NAME`, `SUPPLIER`, `COST_PRICE`, `SELLING_PRICE`, and `INVENTORY`.

### Transactions
A newly implemented table intended to track `Day`, `Quantity`, `Sales`, `Profit`, and `Loss` to provide daily summaries.

## Main User Flows

### Initial Setup and Login
1. User starts the application and enters the MySQL root password.
2. The application ensures the database `test1` and required tables are created if they don't exist.
3. User selects the option to log in or create a new account.
4. Upon successful login, the application enters the main inventory loop.

### Restocking a Product
1. A user logs in and selects option `3` to modify a product.
2. The system prompts for the product ID.
3. The user selects option `5` (Inventory) and enters the additional quantity received.
4. The system queries the current inventory, adds the new amount, updates the database, and commits the transaction.

## Setup Instructions

### Prerequisites
- Python 3.8+
- A local MySQL Server running on `localhost` with the `root` user.

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirments.txt
```

### Environment Variables
The application expects a local `.env` file to read the database password (though `main.py` also prompts for it during execution). Create a `.env` file in the root directory:

```env
PASSWORD=your_mysql_root_password
```

### Running Locally

Ensure your local MySQL server is running, then execute the main entry point:

```bash
python main.py
```

## Future Improvements

- **Password Hashing:** Passwords are currently stored in plain text. Implementing `bcrypt` or `argon2` would significantly improve security.
- **Relational Integrity:** The current implementation removes suppliers by deleting products matching the supplier string. Creating a dedicated `Suppliers` table with foreign keys would enforce data integrity.
- **Completed Transactions Flow:** The `transaction.py` file has table creation logic, but the flow needs to be fully integrated so that removing stock automatically updates the day's profit/loss records.
- **Cloud Database:** Migrating from a local MySQL setup to a managed database (like Supabase or PlanetScale) would allow multi-user access across different machines.

## Learning Outcomes

This project demonstrates how to build a stateful, interactive command-line application backed by a real relational database. It highlights practical software engineering decisions, such as using parameterized queries to avoid SQL injection, modularizing domain logic into separate files, and managing database connections cleanly. It shows an understanding of CRUD workflows and prepares the ground for adapting these backend patterns to a REST API or full-stack application in the future.

## License

License information has not been specified yet.
