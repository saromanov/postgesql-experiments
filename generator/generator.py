import psycopg2

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

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
generate_rows(conn, 10)