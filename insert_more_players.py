import sqlite3

conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

players = [
    ("Rohit Sharma", "Batsman", "Right-hand bat", "None"),
    ("Steve Smith", "Batsman", "Right-hand bat", "Right-arm legbreak"),
    ("Ben Stokes", "All-rounder", "Left-hand bat", "Right-arm fast-medium"),
    ("KL Rahul", "Wicket-keeper", "Right-hand bat", "None"),
    ("Mitchell Starc", "Bowler", "Left-hand bat", "Left-arm fast"),
]

for p in players:
    cursor.execute("INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES (?, ?, ?, ?)", p)

conn.commit()
conn.close()
print("✅ Extra sample players inserted!")
