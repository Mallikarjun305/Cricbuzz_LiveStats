import sqlite3

conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

matches = [
    ("India vs England - 1st Test", "India", "England", "Chennai Stadium", "2024-02-05", "England"),
    ("Australia vs New Zealand - T20", "Australia", "New Zealand", "SCG", "2024-03-12", "Australia"),
]

venues = [
    ("Chennai Stadium", "Chennai", "India", 40000),
    ("SCG", "Sydney", "Australia", 48000),
]

for m in matches:
    cursor.execute("INSERT INTO matches (description, team1, team2, venue, match_date, winner) VALUES (?, ?, ?, ?, ?, ?)", m)

for v in venues:
    cursor.execute("INSERT INTO venues (venue_name, city, country, capacity) VALUES (?, ?, ?, ?)", v)

conn.commit()
conn.close()
print("✅ Extra sample matches & venues inserted!")
