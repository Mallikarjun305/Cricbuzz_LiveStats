import sqlite3

# Read schema from file
with open("db_schema.sql", "r") as f:
    schema = f.read()

# Create DB
conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

# Execute schema
cursor.executescript(schema)

conn.commit()
conn.close()

print("✅ Database initialized successfully!")
