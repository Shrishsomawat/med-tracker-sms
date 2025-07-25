import sqlite3

# 🔸 Connect to SQLite (creates db if it doesn't exist)
conn = sqlite3.connect('../db/med_data.db')
cursor = conn.cursor()

# 🔹 Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS medicines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        barcode TEXT,
        batch_no TEXT,
        expiry_date TEXT,
        phone TEXT
    )
''')

# 🔸 Get user input (or can be auto-filled from QR/barcode later)
name = input("Enter Medicine Name: ")
barcode = input("Enter Barcode (from scan): ")
batch = input("Enter Batch No: ")
expiry = input("Enter Expiry Date (YYYY-MM-DD): ")
phone = input("Enter your Phone Number (for SMS): ")

# 🔹 Insert into DB
cursor.execute('''
    INSERT INTO medicines (name, barcode, batch_no, expiry_date, phone)
    VALUES (?, ?, ?, ?, ?)
''', (name, barcode, batch, expiry, phone))

conn.commit()
conn.close()

print(f"✅ Medicine '{name}' saved successfully to database.")
