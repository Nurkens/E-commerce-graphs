import psycopg2
import os

PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")
PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB   = os.getenv("PG_DB")

def create_db():
    try:
        conn = psycopg2.connect(dbname="postgres", user=PG_USER, password=PG_PASS, host=PG_HOST, port=PG_PORT)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname='{PG_DB}'")
        exists = cur.fetchone()
        if not exists:
            cur.execute(f"CREATE DATABASE {PG_DB}")
            print(f"Database {PG_DB} created.")
        else:
            print(f"Database {PG_DB} already exists.")
        cur.close()
        conn.close()
    except Exception as e:
        print("Error creating database:", e)

if __name__ == "__main__":
    create_db()
