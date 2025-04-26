# 📦 Sales Orders Automation Project

This project automates the retrieval, transformation, and insertion of Sales Order data from **Redacted** Inventory API into a MySQL database, using Python.

It demonstrates real-world enterprise backend work involving:
- API Integration (**Redacted** Inventory)
- Data Flattening and Transformation
- Excel Export
- MySQL Insertion with Upsert Logic
- Secure Handling using `.env` and environment variables

---

## 🚀 Workflow Overview

1. Fetch Sales Orders  
   - Connects to **Redacted** Inventory API
   - Pulls all current sales orders

2. Expand and Transform Data  
   - Flattens nested fields (e.g., line items, billing address)
   - Handles multiple line items per sales order
   - Maps API fields to readable column headers

3. Export to Excel  
   - Saves transformed sales orders to an `.xlsx` file

4. Upload to MySQL Database  
   - Reads the Excel file
   - Maps Excel columns to MySQL table columns using `map_sql.json`
   - Inserts new records or updates existing ones (upsert behavior)

---

## 🛠 Tech Stack

- Python 3.10+
- Pandas
- Openpyxl
- Requests
- MySQL Connector Python
- dotenv (for environment management)

---

## 📚 Project Structure

```
freelancerC4-shirisha/
|
|├── SalesOrder/
|   |│
|   ├── main.py             # Main pipeline: API -> Excel -> MySQL
|   ├── map.json             # API field -> Excel column mapping
|   ├── map_sql.json         # Excel column -> SQL field mapping
|   ├── salesorders_Today.xlsx   # Output Excel file
|├── tests/                  # (Optional unit tests)
|├── .env                   # Secrets for API and DB
|├── .gitignore
|└── README.md
```

---

## 🔑 Environment Variables (`.env`)

```dotenv
# **Redacted** Inventory API
**Redacted**_ORG_ID=your_**Redacted**_organization_id
**Redacted**_ACCESS_TOKEN=your_**Redacted**_access_token

# MySQL Database
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=yourdbname
DB_PORT=3306
```

---

## 🧬 Key Features

- Dynamic Field Expansion  
  Flatten custom fields, billing/shipping addresses, and nested line item structures.

- Mapping Layer  
  Clean mapping from API -> Excel -> MySQL using JSON configs.

- Robust Upload Logic  
  Insert new records or update existing ones safely.

- Secure Secrets Handling  
  Using `.env` file instead of hardcoding credentials.

---

## 🏃 Running the Project

```bash
# Step 1: Install requirements
pip install pandas openpyxl requests python-dotenv mysql-connector-python

# Step 2: Setup your .env file with valid credentials

# Step 3: Run the main pipeline
python main.py
```

---

## 📊 Future Improvements

- Add unit tests
- Create a dashboard to monitor upload status
- Extend pipeline to include other **Redacted** modules (Invoices, Customers)
- Support PostgreSQL/MSSQL alongside MySQL

---

## 👨‍💻 Author

Anthony Olevester  
🔗 [Fiverr Profile](https://www.fiverr.com/olevester)  
🔗 [GitHub Profile](https://github.com/ANTHONY-OLEVESTER)

---

# 🚀 Ready to automate your sales order workflows with Python and SQL!

---

Note: Client-specific names and sensitive identifiers have been redacted to preserve confidentiality.