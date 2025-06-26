# 🩸 Blood Bank Management System

A simple terminal-based Blood Bank Management System built using Python and SQLite. This application helps manage donor registrations, blood inventory, and transfusion records effectively.

---

## 📌 Features

- Donor registration with essential details
- Adding and tracking available blood units
- Requesting blood for transfusion (with inventory checks)
- Viewing current blood inventory
- Listing all registered donors

---

## 🧰 Technologies Used

- **Python 3**
- **SQLite** (built-in Python library)
- **Command Line Interface (CLI)**

---

## 🗃️ Database Structure

### 1. `donors` Table

| Column       | Type    | Description                   |
|--------------|---------|-------------------------------|
| `id`         | INTEGER | Auto-incremented donor ID     |
| `name`       | TEXT    | Donor's full name             |
| `age`        | INTEGER | Donor's age                   |
| `blood_type` | TEXT    | Donor's blood type (e.g., A+) |
| `contact`    | TEXT    | Contact information           |

### 2. `inventory` Table

| Column       | Type    | Description                   |
|--------------|---------|-------------------------------|
| `blood_type` | TEXT    | Blood group (Primary Key)     |
| `units`      | INTEGER | Available units in stock      |

### 3. (Optional) `transfusions` Table

> _Note: This table is referenced in the code but not yet created in the schema. You can add it as shown below:_

```sql
CREATE TABLE IF NOT EXISTS transfusions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient TEXT,
    blood_type TEXT,
    units_used INTEGER,
    date TEXT
);
