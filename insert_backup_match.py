import sqlite3

# Connect to database
conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

# Insert backup sample match
cursor.execute("""
INSERT INTO matches (description, team1, team2, venue, match_date, winner)
VALUES ('India vs Australia - Demo Match', 'India', 'Australia', 'Wankhede Stadium', '2024-11-30', 'India')
""")

# Insert sample venue if not exists
cursor.execute("""
INSERT INTO venues (venue_name, city, country, capacity)
VALUES ('Wankhede Stadium', 'Mumbai', 'India', 33000)
""")

conn.commit()
conn.close()

print("✅ Backup match inserted successfully!")
