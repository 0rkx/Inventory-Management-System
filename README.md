# Inventory Management Software
This Python-based Inventory Management Software uses MySQL as the database backend to manage products, suppliers, and transactions efficiently.

## Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd inventory-management-software
```
2.Install required dependencies:

```bash 
pip install -r requirements.txt
```

3.Create a .env file in the project root and set your MySQL password:

```bash
PASSWORD=your-mysql-password
```

4. Set up the MySQL database and tables using the **setup_database.py** script:

```bash
python inventory.py
```

5. Start the Inventory Management Software:

```bash
python main.py

```
##  Features
- View data on all products
- Add a new product
- Modify product details
- Fetch details about a product
- Delete a product
- View supplier data
- Remove a supplier

## Future Enhancements
- **Transaction Tracking:** Implement a comprehensive transaction tracking system to monitor sales, purchases, and inventory adjustments.

- **User Authentication:** Enhance security with user authentication and authorization mechanisms.

- **Reports**: Generate insightful reports like sales analysis, inventory status, and financial statements.

- **Graphical User Interface (GUI):** Develop an intuitive GUI for a user-friendly experience.

- **Barcode Integration:** Streamline data entry and retrieval through barcode scanning.

- **Notifications:** Set up notifications for low inventory, successful transactions, and more.

- **Data Analytics:** Utilize data analysis to identify trends, patterns, and make informed decisions.

## Contributing
Contributions are welcomed! Feel free to submit pull requests for enhancements or bug fixes.

## # License
This project is licensed under the MIT License.
