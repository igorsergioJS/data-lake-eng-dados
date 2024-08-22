import sys
import os
import psycopg2

# Database connection parameters
dbname = "postgres"
user = "postgres"
password = "postgres"
host = "localhost"

# Connect to the database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
cur = conn.cursor()

def try_execute_sql(sql: str):
    try:
        cur.execute(sql)
        conn.commit()
        print(f"Executed table creation successfully")
    except Exception as e:
        print(f"Couldn't execute table creation due to exception: {e}")
        conn.rollback()

def create_table():
    """
    Cria a tabela weather_data com as colunas apropriadas.
    """
    create_table_sql = """
    CREATE TABLE weather_data (
        id SERIAL PRIMARY KEY,
        temperature FLOAT,
        humidity INT,
        pressure INT,
        weather_description TEXT,
        wind_speed FLOAT,
        timestamp INT
    );
    """
    try_execute_sql(create_table_sql)

    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
