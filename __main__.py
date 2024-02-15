from db import create_connection, run_from_file, add_account


conn = create_connection("db.sqlite3")

cursor = conn.cursor()

run_from_file(cursor, "sql/create_table.sql")

account_data = (0, "myuser",
                "1234", "myuser@gmail.com",
                "06.02.2024", "06.02.2024")

add_account(cursor, account_data)
conn.commit()

conn.close()
