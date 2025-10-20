import sqlite3
conn = sqlite3.connect("db.sqlite3")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS cars (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  price REAL,
  image TEXT
);
""")
conn.commit()
conn.close()
print("Cars table created successfully.")