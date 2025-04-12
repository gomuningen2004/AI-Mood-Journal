import sqlite3
from datetime import datetime

DB_NAME = "data/mood_journal.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            entry TEXT NOT NULL,
            mood TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(entry, mood):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO journal (entry, mood, timestamp) VALUES (?, ?, ?)",
              (entry, mood, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def fetch_entries():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT timestamp, entry, mood FROM journal ORDER BY timestamp ASC")
    data = c.fetchall()
    conn.close()
    return data
