
import sqlite3
from bot.config import load_config

config = load_config()

def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            coin TEXT,
            target_price REAL
        )
    """)
    conn.commit()
    conn.close()

async def save_alerts(user_id: int, coin: str, target_price: float):
    conn = sqlite3.connect(config.db_path)
    c = conn.cursor()
    c.execute("INSERT INTO alerts (user_id, coin, target_price) VALUES (?, ?, ?)", (user_id, coin, target_price))
    conn.commit()
    conn.close()