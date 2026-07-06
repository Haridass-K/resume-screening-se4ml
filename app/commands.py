import sqlite3
from datetime import datetime

DB_PATH = "database/prediction_history.db"


def create_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            resume_text TEXT,
            predicted_category TEXT,
            confidence REAL,
            prediction_time TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_prediction(resume_text, predicted_category, confidence):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (resume_text, predicted_category, confidence, prediction_time)

        VALUES (?, ?, ?, ?)
    """, (
        resume_text[:500],
        predicted_category,
        confidence,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()