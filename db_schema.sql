-- Players Table
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    playing_role TEXT,
    batting_style TEXT,
    bowling_style TEXT
);

-- Matches Table
CREATE TABLE IF NOT EXISTS matches (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    team1 TEXT,
    team2 TEXT,
    venue TEXT,
    match_date TEXT,
    winner TEXT
);

-- Venues Table
CREATE TABLE IF NOT EXISTS venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    venue_name TEXT,
    city TEXT,
    country TEXT,
    capacity INTEGER
);

-- Series Table
CREATE TABLE IF NOT EXISTS series (
    series_id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_name TEXT,
    host_country TEXT,
    match_type TEXT,
    start_date TEXT,
    total_matches INTEGER
);
