import streamlit as st
import sqlite3
import pandas as pd
from utils import crud
from utils.api_handler import get_live_matches

# Streamlit App Config
st.set_page_config(page_title="Cricbuzz LiveStats", layout="wide")
st.title("🏏 Cricbuzz LiveStats Dashboard")

# Sidebar navigation
menu = ["Home", "CRUD Operations", "Live Matches", "SQL Queries"]
choice = st.sidebar.selectbox("📌 Navigation", menu)

# ------------------ HOME ------------------
if choice == "Home":
    st.subheader("Welcome to Cricbuzz LiveStats! 🎉")
    st.markdown("""
    This is your cricket analytics dashboard.  

    **Features:**  
    - 🛠️ CRUD Operations (Manage players)  
    - 🏏 Live Matches (via Cricbuzz API)  
    - 📊 SQL Queries (Database insights)  
    """)

# ------------------ CRUD ------------------
elif choice == "CRUD Operations":
    st.subheader("🛠️ Manage Players Database")

    tab1, tab2, tab3, tab4 = st.tabs(["➕ Add", "📋 View", "✏️ Update", "❌ Delete"])

    # Add Player
    with tab1:
        st.write("Add a new player")
        name = st.text_input("Full Name")
        role = st.selectbox("Playing Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
        batting = st.text_input("Batting Style")
        bowling = st.text_input("Bowling Style")
        if st.button("Add Player"):
            msg = crud.add_player(name, role, batting, bowling)
            st.success(msg)

    # View Players
    with tab2:
        st.write("View all players")
        players = crud.view_players()
        df = pd.DataFrame(players, columns=["ID", "Full Name", "Role", "Batting", "Bowling"])
        st.table(df)

    # Update Player
    with tab3:
        players = crud.view_players()
        if players:
            ids = [p[0] for p in players]
            selected_id = st.selectbox("Select Player ID", ids)
            new_name = st.text_input("Full Name")
            new_role = st.selectbox("Playing Role", ["Batsman", "Bowler", "All-rounder", "Wicket-keeper"])
            new_batting = st.text_input("Batting Style")
            new_bowling = st.text_input("Bowling Style")
            if st.button("Update Player"):
                msg = crud.update_player(selected_id, new_name, new_role, new_batting, new_bowling)
                st.success(msg)

    # Delete Player
    with tab4:
        players = crud.view_players()
        if players:
            ids = [p[0] for p in players]
            del_id = st.selectbox("Select Player ID to Delete", ids)
            if st.button("Delete Player"):
                msg = crud.delete_player(del_id)
                st.success(msg)

# ------------------ LIVE MATCHES ------------------
elif choice == "Live Matches":
    st.subheader("🏏 Live Matches")

    try:
        data = get_live_matches()
    except Exception as e:
        data = {"error": str(e)}

    # --- Case 1: API Failed ---
    if "error" in data or not data.get("typeMatches"):
        st.warning("⚠️ API unavailable or no live matches. Showing backup matches from database.")
        
        conn = sqlite3.connect("cricbuzz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT description, team1, team2, venue, match_date, winner FROM matches ORDER BY match_date DESC LIMIT 1")
        match = cursor.fetchone()
        conn.close()

        if match:
            desc, t1, t2, venue, mdate, winner = match
            st.markdown(f"### 📌 {desc}")
            st.write(f"🏟️ Venue: {venue}")
            st.write(f"📅 Date: {mdate}")
            st.write(f"**{t1} vs {t2}**")
            st.success(f"✅ Result: {winner} won")
        else:
            st.error("No backup matches found in database.")

    # --- Case 2: API Success ---
    else:
        matches = data.get("typeMatches", [])
        live_shown = False

        for match_type in matches:
            series = match_type.get("seriesAdWrapper", {})
            series_name = series.get("seriesName", "Unknown Series")

            for match in series.get("matches", []):
                match_info = match.get("matchInfo", {})
                status = match_info.get("status", "")
                team1 = match_info.get("team1", {}).get("teamName", "Team1")
                team2 = match_info.get("team2", {}).get("teamName", "Team2")

                if "Live" in status or "In Progress" in status:
                    live_shown = True
                    st.markdown(f"### 📌 {series_name}")
                    st.write(f"**{team1} vs {team2}**")

                    # --- Scores ---
                    score_details = match.get("matchScore", {})
                    team1_score = score_details.get("team1Score", {})
                    team2_score = score_details.get("team2Score", {})

                    if team1_score:
                        st.write(f"🏏 {team1}: {team1_score.get('inngs1', {}).get('runs',0)}/"
                                 f"{team1_score.get('inngs1', {}).get('wickets',0)} "
                                 f"({team1_score.get('inngs1', {}).get('overs',0)} overs)")

                    if team2_score:
                        st.write(f"🏏 {team2}: {team2_score.get('inngs1', {}).get('runs',0)}/"
                                 f"{team2_score.get('inngs1', {}).get('wickets',0)} "
                                 f"({team2_score.get('inngs1', {}).get('overs',0)} overs)")

                    st.caption(f"📌 Status: {status}")
                    st.divider()

        # --- Case 3: No live match, show last completed one from API ---
        if not live_shown:
            st.warning("⚠️ No live matches right now. Showing last completed match instead.")
            for match_type in matches:
                series = match_type.get("seriesAdWrapper", {})
                for match in series.get("matches", []):
                    match_info = match.get("matchInfo", {})
                    status = match_info.get("status", "")
                    if "won" in status or "Match Ended" in status or "Result" in status:
                        team1 = match_info.get("team1", {}).get("teamName", "Team1")
                        team2 = match_info.get("team2", {}).get("teamName", "Team2")
                        st.markdown(f"### 📌 {series.get('seriesName','Unknown Series')}")
                        st.write(f"**{team1} vs {team2}**")
                        st.caption(f"✅ Result: {status}")
                        break

# ------------------ SQL QUERIES ------------------
elif choice == "SQL Queries":
    st.subheader("📊 SQL Analytics")

    queries = {
        "1. All Players": "SELECT * FROM players;",
        "2. Players by Role": "SELECT playing_role, COUNT(*) as count FROM players GROUP BY playing_role;",
        "3. All Matches": "SELECT description, team1, team2, venue, match_date, winner FROM matches;",
        "4. Venues with Capacity > 20000": "SELECT venue_name, city, capacity FROM venues WHERE capacity > 20000;",
        "5. Top Venues by Capacity": "SELECT venue_name, capacity FROM venues ORDER BY capacity DESC LIMIT 5;"
    }

    choice_q = st.selectbox("🔽 Select a query", list(queries.keys()))

    conn = sqlite3.connect("cricbuzz.db")
    df = pd.read_sql_query(queries[choice_q], conn)
    conn.close()

    st.dataframe(df)

    # Optional: chart visualization
    if choice_q == "2. Players by Role":
        st.bar_chart(df.set_index("playing_role"))

