import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",          # change if needed
        password="",  # change if needed
        database="python_db",   # optional
        port=3306             # default MySQL port
    )
    print("✅ Connected to MySQL Server")

    # Create cursor
    cursor = conn.cursor()

    # Check database
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    print("Connected to database:", db_name[0])

except pymysql.MySQLError as e:
    print("❌ Error while connecting:", e)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) UNIQUE NOT NULL
# )
# """)
# print("✅ Table 'users' is ready")


# cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
# conn.commit()
# print("✅ Inserted a user")

# cursor.execute("SELECT * FROM users")
# for row in cursor.fetchall():
#     print(row)

# cursor.execute("UPDATE users SET email=%s WHERE id=%s", ("alice_new@example.com", 1))
# conn.commit()
# print("✅ Updated user email")

# cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Ross", "ross@example.com"))
# conn.commit()

  
  

# cursor.execute("DELETE FROM users WHERE id=%s", (1,))
# conn.commit()

  # Insert multiple
# sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
# values = [
#     ("Bob", "bob@example.com"),
#     ("Charlie", "charlie@example.com"),
# ]

# cursor.executemany(sql, values)
# conn.commit()

# print(cursor.rowcount, "rows inserted.")

# cursor.execute("DELETE FROM users WHERE id=%s", (2,))
# conn.commit()

# Example 1: Names starting with 'B'
cursor.execute("SELECT * FROM users WHERE name LIKE %s", ("B%",))
print("Names starting with B:", cursor.fetchall())

# Example 2: Emails ending with 'example.com'
cursor.execute("SELECT * FROM users WHERE email LIKE %s", ("%@example.com",))
print("Emails ending with example.com:", cursor.fetchall())

# Example 3: Names containing 'ar'
cursor.execute("SELECT * FROM users WHERE name LIKE %s", ("%ar%",))
print("Names containing 'ar':", cursor.fetchall())

cursor.close()
conn.close()