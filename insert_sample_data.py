import sqlite3

# Connect to DB
conn = sqlite3.connect("cricbuzz.db")
cursor = conn.cursor()

# Insert sample players
cursor.execute("INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES ('Virat Kohli', 'Batsman', 'Right-hand bat', 'None')")
cursor.execute("INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES ('Jasprit Bumrah', 'Bowler', 'Right-hand bat', 'Right-arm fast')")
cursor.execute("INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES ('Ravindra Jadeja', 'All-rounder', 'Left-hand bat', 'Left-arm orthodox')")

# Insert sample match
cursor.execute("INSERT INTO matches (description, team1, team2, venue, match_date, winner) VALUES ('India vs Australia 1st ODI', 'India', 'Australia', 'Wankhede Stadium', '2024-11-27', 'India')")

# Insert sample venue
cursor.execute("INSERT INTO venues (venue_name, city, country, capacity) VALUES ('Wankhede Stadium', 'Mumbai', 'India', 33000)")

# Insert sample series
cursor.execute("INSERT INTO series (series_name, host_country, match_type, start_date, total_matches) VALUES ('India vs Australia ODI Series', 'India', 'ODI', '2024-11-25', 3)")

# Save and close
conn.commit()
conn.close()

print("✅ Sample data inserted successfully!")
