import sqlite3

conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM players;")
players = cursor.fetchall()
print("✅ Players:", players)

conn.close()
