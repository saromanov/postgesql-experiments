import psycopg2


def create_table():
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

        with conn.cursor() as cursor:
            for data in commands:
                conn.execute(data)
    )
def generate_rows(conn, table_name, n):
    with conn.cursor() as cursor:
        conn.autocommit = True
        values = [
            ('ALA', 'Almaty', 'Kazakhstan'),
            ('TSE', 'Astana', 'Kazakhstan'),
            ('PDX', 'Portland', 'USA'),
        ]
        insert = sql.SQL('INSERT INTO {} (code, name, country_name) VALUES {}').format(
            table_name, sql.SQL(',').join(map(sql.Literal, values))
        )
        cursor.execute(insert)

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost', port=5433)
generate_rows(conn, 10)