import psycopg2
from psycopg2 import sql
from datetime import datetime

def create_customers_table():
    commands = (
        """
        CREATE TABLE IF NOT EXIST customers(
            id INTEGER PRIMARY KEY,
            first_name text,
            last_name text,
            created_at timestampz NOT NULL,
            info jsonb,
            priority int4,
        )
        """
    )

    with conn.cursor() as cursor:
        for data in commands:
            conn.execute(data)
def generate_customers_rows(conn, table_name, n):
    cursor = conn.cursor()
    conn.autocommit = True
    values = [
        ('Sergey', 'Rom', datetime.now()),
        ('Ivan', 'Ivanov', datetime.now()),
        ('Petr', 'Petrov', datetime.now()),
    ]
    insert = sql.SQL('INSERT INTO {} (code, name, country_name) VALUES {}').format(
        table_name, sql.SQL(',').join(map(sql.Literal, values))
    )
    cursor.execute(insert)

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost', port=5433)
generate_customers_rows(conn, 10, 10)