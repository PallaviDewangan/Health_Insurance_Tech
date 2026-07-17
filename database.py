"""
database.py
SQLite Database Handler for Guardian Health Insurance.
Implements the relational database schema, tables for users, premium logs, and plans,
with automatic seeding and helper transaction queries.
"""

import sqlite3
from pathlib import Path
from typing import Dict, List, Optional, Union
import pandas as pd

# Define absolute database path in the project workspace
DB_PATH = Path(__file__).resolve().parent / "insurance.db"

def get_connection() -> sqlite3.Connection:
    """
    Establishes a connection to the SQLite database.
    Enables foreign keys and sets row_factory to sqlite3.Row for dict-like rows.
    """
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database() -> None:
    """
    Initializes the SQLite database.
    Creates necessary tables and seeds initial insurance plans.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # 1. Create 'users' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fullname TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT NOT NULL,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user', -- 'user' or 'admin'
                city TEXT,
                state TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # 2. Create 'insurance_plans' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS insurance_plans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                coverage_amount REAL NOT NULL,
                hospitalization_pct INTEGER NOT NULL,
                cashless_hospitals INTEGER NOT NULL,
                critical_illness_cover INTEGER NOT NULL, -- 0 or 1
                health_checkups TEXT NOT NULL,
                emergency_support TEXT NOT NULL,
                base_price REAL NOT NULL,
                is_popular INTEGER DEFAULT 0 -- 0 or 1
            );
        """)

        # 3. Create 'premium_history' table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS premium_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                fullname TEXT,
                calculation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL,
                occupation TEXT NOT NULL,
                marital_status TEXT NOT NULL,
                city TEXT,
                state TEXT,
                height REAL NOT NULL,
                weight REAL NOT NULL,
                bmi REAL NOT NULL,
                bmi_category TEXT NOT NULL,
                bp_systolic INTEGER NOT NULL,
                bp_diastolic INTEGER NOT NULL,
                diabetes INTEGER NOT NULL, -- 0 or 1
                heart_disease INTEGER NOT NULL, -- 0 or 1
                surgery INTEGER NOT NULL, -- 0 or 1
                smoking INTEGER NOT NULL, -- 0 or 1
                alcohol INTEGER NOT NULL, -- 0 or 1
                exercise TEXT NOT NULL, -- 'None', 'Moderate', 'Regular'
                sleep_hours REAL NOT NULL,
                plan_name TEXT NOT NULL,
                coverage REAL NOT NULL,
                duration INTEGER NOT NULL,
                existing_insurance INTEGER NOT NULL, -- 0 or 1
                family_members INTEGER NOT NULL,
                annual_premium REAL NOT NULL,
                monthly_premium REAL NOT NULL,
                risk_level TEXT NOT NULL,
                breakdown_json TEXT NOT NULL, -- JSON string of surcharge calculations
                recommendation TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
            );
        """)

        conn.commit()
        print("[DB] Tables initialized successfully.")
        
        # Seed default insurance plans
        seed_default_plans()

    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to initialize database: {e}")
        raise e
    finally:
        conn.close()

def seed_default_plans() -> None:
    """
    Seeds default plans (Basic, Silver, Gold) into the insurance_plans table.
    Does not duplicate records if they already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    plans = [
        ("Basic", 500000.0, 90, 150, 0, "Basic checkups covered", "Standard Emergency Support", 5000.0, 0),
        ("Silver", 1000000.0, 100, 300, 1, "Annual Health Checkup included", "24/7 Helpline Support", 10000.0, 0),
        ("Gold", 2000000.0, 100, 500, 1, "Comprehensive Health Screening", "Priority 24/7 Emergency Support", 18000.0, 1)
    ]

    try:
        cursor.executemany("""
            INSERT OR IGNORE INTO insurance_plans (
                name, coverage_amount, hospitalization_pct, cashless_hospitals,
                critical_illness_cover, health_checkups, emergency_support, base_price, is_popular
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, plans)
        conn.commit()
        print("[DB] Default plans seeded successfully.")
    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to seed plans: {e}")
    finally:
        conn.close()

def register_user(fullname: str, email: str, phone: str, username: str, 
                  password_hash: str, role: str = "user", 
                  city: Optional[str] = None, state: Optional[str] = None) -> int:
    """
    Registers a new user in the database.
    Raises sqlite3.IntegrityError if email or username already exists.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (fullname, email, phone, username, password_hash, role, city, state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (fullname, email, phone, username, password_hash, role, city, state))
        conn.commit()
        user_id = cursor.lastrowid
        return user_id
    except sqlite3.IntegrityError as e:
        conn.rollback()
        raise e
    finally:
        conn.close()

def authenticate_user(username: str, password_hash: str) -> Optional[Dict]:
    """
    Checks credentials and logs in a user.
    Returns the user record as a dict if successful, otherwise None.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM users WHERE username = ? AND password_hash = ?
        """, (username, password_hash))
        row = cursor.fetchone()
        return dict(row) if row else None
    except sqlite3.Error as e:
        print(f"[DB Error] Authentication error: {e}")
        return None
    finally:
        conn.close()

def get_user_by_id(user_id: int) -> Optional[Dict]:
    """
    Fetches user profile details by their primary user_id.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return dict(row) if row else None
    except sqlite3.Error as e:
        print(f"[DB Error] Fetch user by ID failed: {e}")
        return None
    finally:
        conn.close()

def update_user(user_id: int, fullname: str, email: str, phone: str, 
                city: Optional[str], state: Optional[str]) -> bool:
    """
    Updates basic profile details of an existing user.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE users
            SET fullname = ?, email = ?, phone = ?, city = ?, state = ?
            WHERE id = ?
        """, (fullname, email, phone, city, state, user_id))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to update user profile: {e}")
        return False
    finally:
        conn.close()

def delete_user(user_id: int) -> bool:
    """
    Deletes a user account from the system. Cascade deletes premium histories.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to delete user: {e}")
        return False
    finally:
        conn.close()

def update_user_password(user_id: int, new_password_hash: str) -> bool:
    """
    Updates the hashed password of an existing user.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE users
            SET password_hash = ?
            WHERE id = ?
        """, (new_password_hash, user_id))
        conn.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to change password: {e}")
        return False
    finally:
        conn.close()

def save_premium_history(user_id: Optional[int], fullname: str, age: int, gender: str, 
                         occupation: str, marital_status: str, city: Optional[str], state: Optional[str],
                         height: float, weight: float, bmi: float, bmi_category: str, 
                         bp_systolic: int, bp_diastolic: int, diabetes: int, heart_disease: int, 
                         surgery: int, smoking: int, alcohol: int, exercise: str, sleep_hours: float, 
                         plan_name: str, coverage: float, duration: int, existing_insurance: int, 
                         family_members: int, annual_premium: float, monthly_premium: float, 
                         risk_level: str, breakdown_json: str, recommendation: str) -> int:
    """
    Inserts a newly calculated premium calculation record.
    Returns the generated record primary key.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO premium_history (
                user_id, fullname, age, gender, occupation, marital_status, city, state,
                height, weight, bmi, bmi_category, bp_systolic, bp_diastolic,
                diabetes, heart_disease, surgery, smoking, alcohol, exercise, sleep_hours,
                plan_name, coverage, duration, existing_insurance, family_members,
                annual_premium, monthly_premium, risk_level, breakdown_json, recommendation
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, fullname, age, gender, occupation, marital_status, city, state,
            height, weight, bmi, bmi_category, bp_systolic, bp_diastolic,
            diabetes, heart_disease, surgery, smoking, alcohol, exercise, sleep_hours,
            plan_name, coverage, duration, existing_insurance, family_members,
            annual_premium, monthly_premium, risk_level, breakdown_json, recommendation
        ))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        conn.rollback()
        print(f"[DB Error] Failed to write premium log: {e}")
        raise e
    finally:
        conn.close()

def get_user_history(user_id: int) -> List[Dict]:
    """
    Fetches all premium history records of a specific user.
    Ordered by calculation date descending.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT * FROM premium_history 
            WHERE user_id = ? 
            ORDER BY calculation_date DESC
        """, (user_id,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"[DB Error] Failed to get user history: {e}")
        return []
    finally:
        conn.close()

def get_all_users() -> List[Dict]:
    """
    Returns lists of all registered users in the database (admin operation).
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users ORDER BY created_at DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"[DB Error] Failed to get all users: {e}")
        return []
    finally:
        conn.close()

def get_all_premium_records() -> List[Dict]:
    """
    Returns list of all premium calculation records run on the system (admin operation).
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM premium_history ORDER BY calculation_date DESC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"[DB Error] Failed to fetch system premium records: {e}")
        return []
    finally:
        conn.close()

def get_all_plans() -> List[Dict]:
    """
    Returns list of seeded insurance plans.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM insurance_plans ORDER BY base_price ASC")
        rows = cursor.fetchall()
        return [dict(row) for row in rows]
    except sqlite3.Error as e:
        print(f"[DB Error] Failed to fetch plans: {e}")
        return []
    finally:
        conn.close()

def export_history_to_dataframe() -> pd.DataFrame:
    """
    Retrieves all records in premium_history and converts them to a Pandas DataFrame
    suitable for analysis or CSV exports (admin operation).
    """
    try:
        # Establish connection for pandas read
        conn = get_connection()
        df = pd.read_sql_query("SELECT * FROM premium_history ORDER BY calculation_date DESC", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"[DB Error] Failed to read into DataFrame: {e}")
        return pd.DataFrame()

def main() -> None:
    """
    Runs initial database configuration and seeding when executed directly.
    Creates an admin account if none exists.
    """
    print("--- Guardian Health Insurance DB Tool ---")
    print(f"Target DB Path: {DB_PATH}")
    initialize_database()
    
    # Try seeding a default admin account for developer testing
    # Username: admin, Password: admin_password_hash (pre-hashed SHA256 of 'admin123')
    # Pre-hashed of 'admin123' with salt 'admin':
    # hashlib.sha256(("admin" + "admin123").encode()).hexdigest()
    import hashlib
    admin_salt = "admin"
    admin_pw = "admin123"
    hashed = hashlib.sha256((admin_salt + admin_pw).encode()).hexdigest()
    
    try:
        register_user(
            fullname="System Administrator",
            email="admin@guardianhealth.com",
            phone="000-000-0000",
            username="admin",
            password_hash=hashed,
            role="admin",
            city="Noida",
            state="Uttar Pradesh"
        )
        print("[DB] Default admin account created: User='admin', Pass='admin123'")
    except sqlite3.IntegrityError:
        print("[DB] Admin account 'admin' already registered.")
    
    print("--- Database setup completed. ---")

if __name__ == "__main__":
    main()
