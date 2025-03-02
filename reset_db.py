import sqlite3
import os

DB_NAME = "waxes.db"

def reset_database():
    # Remove the existing database file
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print(f"Deleted existing database: {DB_NAME}")

    # Recreate the database and the ski_waxes table
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE ski_waxes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        wax_type TEXT NOT NULL,
        temp_range TEXT NOT NULL,
        snow_type TEXT,
        notes TEXT
    );
    """)
    
    conn.commit()
    conn.close()
    print("Database reset and ski_waxes table created.")

if __name__ == "__main__":
    reset_database()
