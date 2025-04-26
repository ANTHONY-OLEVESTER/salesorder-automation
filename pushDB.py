import os
import re
import mysql.connector
import pandas as pd
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
    "port": int(os.getenv("DB_PORT", 3306))
}

TABLE_NAME = "sales_orders"
EXCEL_FOLDER = "SalesOrder"

# Load mapping from map_sql.json
with open("map_sql.json", "r", encoding="utf-8") as f:
    FIELD_MAP = json.load(f)

REVERSE_MAP = {v: k for k, v in FIELD_MAP.items()}  # Maps Excel headers → DB columns


def connect_to_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        print("✅ Connected to database")
        return conn
    except mysql.connector.Error as err:
        print("❌ DB Connection Error:", err)
        return None


def upload_to_db(df, conn):
    cursor = conn.cursor()

    # Get actual DB columns
    cursor.execute(f"SHOW COLUMNS FROM {TABLE_NAME}")
    db_cols = set(row[0].lower() for row in cursor.fetchall())

    for index, row in df.iterrows():
        valid_cols = []
        values = []
        seen = set()

        for excel_col in df.columns:
            db_col = REVERSE_MAP.get(excel_col)
            if db_col and db_col.lower() in db_cols and db_col.lower() not in seen:
                valid_cols.append(db_col)
                values.append(None if pd.isna(row[excel_col]) else str(row[excel_col]))
                seen.add(db_col.lower())

        if not valid_cols:
            print(f"⚠️ Row {index} skipped: No matching columns found in DB for this row")
            continue

        placeholders = ["%s"] * len(valid_cols)
        sql = f"""
        INSERT INTO {TABLE_NAME} ({', '.join(valid_cols)})
        VALUES ({', '.join(placeholders)})
        ON DUPLICATE KEY UPDATE {', '.join([f'{col}=VALUES({col})' for col in valid_cols])}
        """
        try:
            cursor.execute(sql, values)
        except Exception as e:
            print(f"❌ Failed to insert row {index}: {e}")

    conn.commit()
    print(f"✅ Uploaded {len(df)} rows to `{TABLE_NAME}`")


def load_excel_files_from_folder(folder):
    all_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".xlsx")]
    print(f"📁 Found {len(all_files)} Excel files in '{folder}'")
    return all_files


if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        for file in load_excel_files_from_folder(EXCEL_FOLDER):
            print(f"\n📥 Reading {file}...")
            df = pd.read_excel(file)
            print(f"✅ Loaded {len(df)} rows.")
            upload_to_db(df, conn)
        conn.close()
