import sqlite3
import sys


def create_connection(db_name: str):
    try:
        connection = sqlite3.connect(db_name)
        print(sqlite3.version)
        return connection
    except Exception as e:
        print(e)
        sys.exit(1)


def load_file(path: str):
    f = open(path, 'r')
    sql = f.read()
    f.close()

    return sql


def run_from_file(cursor, path: str):
    sql = load_file(path)
    cursor.execute(sql)


def add_account(cursor, data: tuple):
    sql = load_file("sql/insert_account.sql")
    cursor.execute(sql, data)
