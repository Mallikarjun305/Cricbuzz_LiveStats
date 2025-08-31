\# 📝 Final `README.md`



\# 🏏 Cricbuzz LiveStats Dashboard



A **Cricket Analytics Dashboard built with Python**, Streamlit, and SQLite .  

This project fetches live cricket scores  using the Cricbuzz API, allows **CRUD operations** for players, and provides  **SQL-based analytics** with visualizations.  

Designed as a final-year project / demo-ready app.  



---



🚀 **Features**



🛠️  **CRUD Operations** 

&nbsp; - Add new players

&nbsp; - Update player info

&nbsp; - Delete players

&nbsp; - View all players



🏏 **Live Matches** 

&nbsp; - Fetches live scores via  Cricbuzz API (RapidAPI) 

&nbsp; - If no live matches → shows  last completed match 

&nbsp; - If API unavailable → falls back to  backup matches in SQLite DB 



📊  **SQL Queries \& Analytics** 

&nbsp; - Dropdown with 5 pre-defined queries:

&nbsp;   1. All Players

&nbsp;   2. Players by Role (with bar chart)

&nbsp;   3. All Matches

&nbsp;   4. Venues with Capacity > 20000

&nbsp;   5. Top Venues by Capacity

&nbsp; - Results shown in  interactive tables 



🎨  **UI Design** 

&nbsp; - Streamlit-based dashboard

&nbsp; - Cricket-themed icons

&nbsp; - Images/logos support (optional)



---



\## 📂 **Project Structure**



```



Cricbuzz\\\_LiveStats/

│── main.py              # Main Streamlit app

│── init\\\_db.py           # Initialize SQLite database

│── test\\\_db.py           # Test DB connection

│── insert\\\_backup\\\_match.py   # Insert demo India vs Australia match

│── insert\\\_more\\\_players.py   # Insert extra players

│── insert\\\_more\\\_matches.py   # Insert extra matches

│── utils/

│   └── api\\\_handler.py   # Cricbuzz API handler

│── cricbuzz.db          # SQLite database (auto created)

│── images/              # (Optional) Banner \& team logos

│── README.md            # Project documentation

│── requirements.txt     # Python dependencies



````



---



⚙️ **Installation \& Setup**



1\. Clone / Download Project

git clone <your\_repo\_link>

cd Cricbuzz\_LiveStats



2\. Create Virtual Environment

python -m venv venv

venv\\Scripts\\activate     # On Windows



3\. Install Dependencies



pip install -r requirements.txt



**Contents of `requirements.txt`:**



streamlit

pandas

requests

sqlite3-binary



4\. Initialize Database



python init\_db.py

python insert\_backup\_match.py

python insert\_more\_players.py

python insert\_more\_matches.py

```



5\. Add Your RapidAPI Key



Edit `utils/api\_handler.py`:



headers = {

&nbsp;   "X-RapidAPI-Key": "YOUR\_KEY\_HERE",

&nbsp;   "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com"

}



6\. Run Application



streamlit run main.py



---



🖼️ **Screenshots (placeholders)**



\*  Home Page 



\*  CRUD Operations Page 



\*  Live Matches Page 



\*  SQL Queries Page 

---



📊 **Example SQL Queries**



\*  Players by Role 



SELECT playing\_role, COUNT(\*) as count 

FROM players 

GROUP BY playing\_role;



\*  Top Venues by Capacity 



SELECT venue\_name, capacity 

FROM venues 

ORDER BY capacity DESC 

LIMIT 5;



---



👨‍💻 **Technologies Used**



\*  Frontend : Streamlit

\*  Backend : Python

\*  Database : SQLite

\*  API : Cricbuzz (via RapidAPI)

\*  Visualization : Pandas, Streamlit Charts



---



🎯 **Future Enhancements**



\* Add Player Photos \& Team Logos

\* Export Reports to PDF/Excel

\* User Authentication

\* Historical match analysis



---



🏆 **Project Demo Ready**



This project is fully functional for demo:



\* Live Matches (API or fallback DB)

\* CRUD with Players

\* SQL Queries \& Visualizations



---



💡  Tip for Demo : If no live match is happening, your app will  automatically show last completed match or backup India vs Australia demo match  → so you’ll always have data to present!



---



