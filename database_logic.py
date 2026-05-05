import psycopg2

DATABASE_URL = "postgresql://crrae:crrae_umoa@postgresql34636-0.cloudclusters.net:34636/crrae_umoa?sslmode=require"

def load_accounts_db():
    with psycopg2.connect(DATABASE_URL) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, name, email, balance FROM accounts ORDER BY id")
            return cur.fetchall()