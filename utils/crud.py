import sqlite3

DB_NAME = "cricbuzz.db"

def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)

# Add a player
def add_player(full_name, role, batting_style, bowling_style):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO players (full_name, playing_role, batting_style, bowling_style) VALUES (?, ?, ?, ?)",
        (full_name, role, batting_style, bowling_style)
    )
    conn.commit()
    conn.close()
    return "✅ Player added successfully!"

# View all players
def view_players():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM players")
    data = cursor.fetchall()
    conn.close()
    return data

# Update a player
def update_player(player_id, full_name, role, batting_style, bowling_style):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE players SET full_name=?, playing_role=?, batting_style=?, bowling_style=? WHERE player_id=?",
        (full_name, role, batting_style, bowling_style, player_id)
    )
    conn.commit()
    conn.close()
    return "✅ Player updated successfully!"

# Delete a player
def delete_player(player_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players WHERE player_id=?", (player_id,))
    conn.commit()
    conn.close()
    return "✅ Player deleted successfully!"
