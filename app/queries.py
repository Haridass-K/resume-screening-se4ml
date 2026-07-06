import sqlite3

DB_PATH = "database/prediction_history.db"


def view_history():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            predicted_category,
            confidence,
            prediction_time

        FROM predictions

        ORDER BY id DESC
    """)

    history = cursor.fetchall()

    conn.close()

    return history