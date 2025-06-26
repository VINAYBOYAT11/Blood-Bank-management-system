import sqlite3
from datetime import datetime

#  to Connect  database
conn = sqlite3.connect("bloodbank.db")
cursor = conn.cursor()

# Create tables

#1. donors table created 
cursor.execute(''' 
               
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    blood_type TEXT,
    contact TEXT
)
''')

#creates inventory table
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    blood_type TEXT PRIMARY KEY,
    units INTEGER
)
''')


conn.commit()

# ---- Functions ----

def register_donor():
    name = input("Donor name: ")
    age = int(input("Age: "))
    blood = input("Blood type: ").upper()
    contact = input("Contact: ")
    cursor.execute("INSERT INTO donors (name, age, blood_type, contact) VALUES (?, ?, ?, ?)", 
                   (name, age, blood, contact))
    conn.commit()
    print("Donor registered.\n")

def add_blood():
    blood = input("Blood type: ").upper()
    units = int(input("Units to add: "))
    cursor.execute("SELECT units FROM inventory WHERE blood_type = ?", (blood,))
    result = cursor.fetchone()
    if result:
        total = result[0] + units
        cursor.execute("UPDATE inventory SET units = ? WHERE blood_type = ?", (total, blood))
    else:
        cursor.execute("INSERT INTO inventory (blood_type, units) VALUES (?, ?)", (blood, units))
    conn.commit()
    print("Blood added.\n")

def show_inventory():
    print("Current Blood Inventory:")
    cursor.execute("SELECT * FROM inventory")
    for row in cursor.fetchall():
        print(f"{row[0]}: {row[1]} units")
    print()

def request_blood():
    patient = input("Patient name: ")
    blood = input("Required blood type: ").upper()
    units = int(input("Units needed: "))
    cursor.execute("SELECT units FROM inventory WHERE blood_type = ?", (blood,))
    result = cursor.fetchone()
    if result and result[0] >= units:
        new_units = result[0] - units
        cursor.execute("UPDATE inventory SET units = ? WHERE blood_type = ?", (new_units, blood))
        cursor.execute("INSERT INTO transfusions (patient, blood_type, units_used, date) VALUES (?, ?, ?, ?)",
                       (patient, blood, units, str(datetime.now().date())))
        conn.commit()
        print("Blood issued.\n")
    else:
        print("Not enough blood available.\n")

def show_donors():
    print("Donor List:")
    cursor.execute("SELECT name, blood_type FROM donors")
    for donor in cursor.fetchall():
        print(f"{donor[0]} ({donor[1]})")
    print()



# ---- Menu ----

def menu():
    while True:
        print("=== Blood Bank Menu ===")
        print("1. Register Donor")
        print("2. Add Blood Units")
        print("3. View Inventory")
        print("4. Request Blood")
        print("5. View Donors")
   
        print("0. Exit")
        choice = input("Enter option: ")

        if choice == "1":
            register_donor()
        elif choice == "2":
            add_blood()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            request_blood()
        elif choice == "5":
            show_donors()
        elif choice == "0":
            break
        else:
            print("Invalid choice.\n")

menu()
