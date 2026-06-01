import psycopg2

DB_CONFIG = {
    "dbname": "finance_db",
    "user": "postgres",
    "password": "Postgres123",
    "host": "localhost",
    "port": 5432
}


def get_conn():
    return psycopg2.connect(**DB_CONFIG)