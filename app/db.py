import sqlite3
import pandas as pd

CACHE_DB = "papers.db"

def init_db():
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            link TEXT,
            snippet TEXT,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_paper(paper):
    conn = sqlite3.connect(CACHE_DB)
    c = conn.cursor()
    c.execute("INSERT INTO papers (title, link, snippet) VALUES (?, ?, ?)",
              (paper['title'], paper['link'], paper['snippet']))
    conn.commit()
    conn.close()

def get_saved_papers():
    conn = sqlite3.connect(CACHE_DB)
    df = pd.read_sql_query("SELECT * FROM papers ORDER BY saved_at DESC", conn)
    conn.close()
    return df
