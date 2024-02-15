from db import create_connection, run_from_file


conn = create_connection("db.sqlite3")

cursor = conn.cursor()

run_from_file(cursor, "sql/show_usernames.sql")

rows = cursor.fetchall()

for row in rows:
    print(*row)

conn.close()
