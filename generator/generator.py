import psycopg2

def generate_rows(conn, n):
    with conn.cursor() as cursor:
        conn.autocommit = True
        values = [
            ('ALA', 'Almaty', 'Kazakhstan'),
            ('TSE', 'Astana', 'Kazakhstan'),
            ('PDX', 'Portland', 'USA'),
        ]
        insert = sql.SQL('INSERT INTO city (code, name, country_name) VALUES {}').format(
            sql.SQL(',').join(map(sql.Literal, values))
        )
        cursor.execute(insert)

conn = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
cursor = conn.cursor()