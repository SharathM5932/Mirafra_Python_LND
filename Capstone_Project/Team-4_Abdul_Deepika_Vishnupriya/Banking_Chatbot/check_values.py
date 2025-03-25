import sqlite3

DB_PATH = "database.db"  # Adjust this to your database file path

try:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT user_name FROM users WHERE =1")
    tables = cursor.fetchall()

    if tables:
        print("✅ Connection successful! Tables in the database:")
        for table in tables:
            print(table[0])
    else:
        print("✅ Connected, but no tables found.")

    connection.close()
except sqlite3.Error as e:
    print(f"❌ SQLite Error: {e}")
