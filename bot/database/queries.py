
import sqlite3
from bot.config import load_config
from collections import defaultdict

config = load_config()


async def get_all_alerts():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT user_id, coin, target_price FROM alerts")
    alerts = cursor.fetchall()
    conn.close()
    return alerts

async def get_all_alerts_by_id(user_id: int):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT coin, target_price FROM alerts WHERE user_id = ?", (user_id,))
    alerts = cursor.fetchall()
    conn.close()
    return alerts

async def remove_alert(user_id: int, coin: str, target_price: float):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alerts WHERE user_id = ? AND coin = ? AND target_price = ?", (user_id, coin, target_price))
    conn.commit()
    conn.close()

async def remove_all(user_id: int):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alerts WHERE user_id = ?",(user_id,))
    conn.commit()
    conn.close()


async def update_alert_price_in_db(alert_id: int, new_price: float, coin: str):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE alerts SET target_price = ? WHERE user_id = ? AND coin = ?", (new_price, alert_id, coin))
    conn.commit()
    conn.close()