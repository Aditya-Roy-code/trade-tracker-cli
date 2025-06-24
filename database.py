import sqlite3
from models import Trade
from datetime import datetime

def create_connection():
    return sqlite3.connect("trades.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            trade_type TEXT CHECK(trade_type IN ('BUY', 'SELL')) NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def insert_trade(symbol, quantity, price, trade_type):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO trades (symbol, quantity, price, trade_type)
        VALUES (?, ?, ?, ?)
    ''', (symbol.upper(), quantity, price, trade_type.upper()))
    conn.commit()
    conn.close()

def query_trades(symbol=None):
    conn = create_connection()
    cursor = conn.cursor()
    if symbol:
        cursor.execute('SELECT symbol, quantity, price, trade_type, timestamp FROM trades WHERE symbol = ?', (symbol.upper(),))
    else:
        cursor.execute('SELECT symbol, quantity, price, trade_type, timestamp FROM trades')
    rows = cursor.fetchall()
    conn.close()

    trades = []
    for row in rows:
        trade = Trade(
            symbol=row[0],
            quantity=row[1],
            price=row[2],
            trade_type=row[3],
            timestamp=row[4]
        )
        trades.append(trade)
    return trades
