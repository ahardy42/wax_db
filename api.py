from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("waxes.db")
    conn.row_factory = sqlite3.Row  # Enables dictionary-like access
    return conn

# Pydantic model for input validation
class Wax(BaseModel):
    brand: str
    model: str
    wax_type: str
    temp_range: str
    snow_type: str
    notes: str

# GET the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Ski Wax API!"}

# GET all waxes
@app.get("/waxes")
def get_waxes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ski_waxes")
    waxes = cursor.fetchall()
    conn.close()
    return {"waxes": [dict(wax) for wax in waxes]}

# GET a specific wax by ID
@app.get("/waxes/{wax_id}")
def get_wax(wax_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ski_waxes WHERE id = ?", (wax_id,))
    wax = cursor.fetchone()
    conn.close()
    if wax:
        return dict(wax)
    raise HTTPException(status_code=404, detail="Wax not found")

# ADD a new wax
@app.post("/waxes")
def add_wax(wax: Wax):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO ski_waxes (brand, model, wax_type, temp_range, snow_type, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (wax.brand, wax.model, wax.wax_type, wax.temp_range, wax.snow_type, wax.notes))
    
    conn.commit()
    wax_id = cursor.lastrowid
    conn.close()
    
    return {"message": "Wax added successfully", "id": wax_id}

# EDIT an existing wax
@app.put("/waxes/{wax_id}")
def update_wax(wax_id: int, wax: Wax):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ski_waxes
        SET brand = ?, model = ?, wax_type = ?, temp_range = ?, snow_type = ?, notes = ?
        WHERE id = ?
    """, (wax.brand, wax.model, wax.wax_type, wax.temp_range, wax.snow_type, wax.notes, wax_id))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Wax not found")
    
    conn.commit()
    conn.close()
    return {"message": "Wax updated successfully"}

# DELETE a wax
@app.delete("/waxes/{wax_id}")
def delete_wax(wax_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ski_waxes WHERE id = ?", (wax_id,))
    
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Wax not found")

    conn.commit()
    conn.close()
    return {"message": "Wax deleted successfully"}

# DELETE all waxes
@app.delete("/waxes")
def delete_all_waxes():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ski_waxes")
    conn.commit()
    conn.close()
    return {"message": "All waxes deleted successfully"}

# SEED the database with initial data
@app.post("/seed")
def seed_waxes():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Swix wax data to insert
    swix_waxes = [
        ("Swix", "V40 Blue Extra", "Hard Wax", "-1°C to -7°C", "New or fine-grained snow", "Ideal for typical winter conditions; widely used for its versatility."),
        ("Swix", "V60 Red/Silver", "Hard Wax", "0°C to +3°C", "Wet, transformed snow", "Suitable for moist and warm conditions; provides excellent grip."),
        ("Swix", "K22 Universal Klister", "Klister", "-3°C to +10°C", "Transformed, coarse, or icy snow", "Versatile klister for varying conditions; ensures reliable grip on icy tracks."),
        ("Swix", "K70 Red Klister", "Klister", "+1°C to +5°C", "Wet, coarse snow", "Optimal for very wet conditions; prevents icing and provides consistent grip."),
        ("Swix", "LF6 Blue", "Glide Wax", "-5°C to -10°C", "New or fine-grained snow", "Low-fluoro content; excellent for colder conditions; durable and provides good glide."),
        ("Swix", "HF8 Red", "Glide Wax", "-4°C to +4°C", "Varied, from fine-grained to coarse, wet snow", "High-fluoro content; ideal for high humidity and varying conditions; enhances speed."),
    ]
    
    # Insert data into the ski_waxes table
    cursor.executemany("""
        INSERT INTO ski_waxes (brand, model, wax_type, temp_range, snow_type, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    """, swix_waxes)
    
    conn.commit()
    conn.close()
    return {"message": "Database seeded successfully"}