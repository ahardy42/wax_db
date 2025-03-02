import sqlite3

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("waxes.db")
cursor = conn.cursor()

# Create the ski_waxes table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS ski_waxes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    brand TEXT NOT NULL,
    model TEXT NOT NULL,
    wax_type TEXT NOT NULL,
    temp_range TEXT NOT NULL,
    snow_type TEXT,
    notes TEXT
);
""")

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
INSERT INTO ski_waxes (brand, model, wax
::contentReference[oaicite:0]{index=0}
_type, temp_range, snow_type, notes)
VALUES (?, ?, ?, ?, ?, ?)
""", swix_waxes)