import sqlite3

# Connect to SQLite
# Connect to SQLite (creates a new database if it doesn't exist)
conn = sqlite3.connect("my_database.db")

# Create a cursor object
cursor = conn.cursor()

#Create a Table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL
# )
# """)

# conn.commit()


# Insert single record
# cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))

# # Insert multiple records
# users = [
#     ("Bob", "bob@example.com"),
#     ("Charlie", "charlie@example.com")
# ]
# cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

# conn.commit()

# Fetch all rows
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# # Fetch one row
# cursor.execute("SELECT * FROM users WHERE id = ?", (1,))
# user = cursor.fetchone()
# print(user)

# cursor.execute("UPDATE users SET email = ? WHERE id = ?", ("alice_new@example.com", 1))
# conn.commit()


# cursor.execute("DELETE FROM users WHERE id = ?", (2,))
# conn.commit()

# conn.close()




# Example: search for users whose name starts with 'A'
cursor.execute("SELECT * FROM users WHERE name LIKE ?", ("A%",))
results = cursor.fetchall()
print("Names starting with A:", results)

# Example: search for users whose email ends with 'example.com'
cursor.execute("SELECT * FROM users WHERE email LIKE ?", ("%@example.com",))
results = cursor.fetchall()
print("Emails ending with example.com:", results)

# Example: search for names containing 'ar'
cursor.execute("SELECT * FROM users WHERE name LIKE ?", ("%ar%",))
results = cursor.fetchall()
print("Names containing 'ar':", results)

conn.close()
