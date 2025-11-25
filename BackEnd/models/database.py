import sqlite3

DB_NAME = "wallet.db"


def db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db_connection()
    cur = conn.cursor()

    # groups table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_name TEXT
    )
    """)

    # users
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER,
        name TEXT,
        user_type TEXT,
        family_size INTEGER
    )
    """)

    # wallet
    cur.execute("""
    CREATE TABLE IF NOT EXISTS wallet (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER,
        user_id INTEGER,
        balance REAL
    )
    """)

    # transactions
    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER,
        paid_by INTEGER,
        amount REAL,
        description TEXT
    )
    """)

    # participants
    cur.execute("""
    CREATE TABLE IF NOT EXISTS participants (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        expense_id INTEGER,
        user_id INTEGER
    )
    """)

    conn.commit()
