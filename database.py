import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS gifts (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            amazon_link TEXT NOT NULL UNIQUE,
            reserved_by TEXT
        )
    """)
    
    cur.execute("SELECT COUNT(*) FROM gifts")
    if cur.fetchone()[0] == 0:
        from initial_data import raw_gifts
        for gift in raw_gifts:
            cur.execute(
                "INSERT INTO gifts (name, amazon_link) VALUES (%s, %s) ON CONFLICT DO NOTHING",
                (gift['name'], gift['link'])
            )
    
    conn.commit()
    cur.close()
    conn.close()

def get_all_gifts():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, amazon_link, reserved_by FROM gifts ORDER BY id")
    gifts = [{
        "id": row[0],
        "name": row[1],
        "link": row[2],
        "reserved_by": row[3]
    } for row in cur.fetchall()]
    cur.close()
    conn.close()
    return gifts

def reserve_gift(gift_id, name):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE gifts SET reserved_by = %s WHERE id = %s AND reserved_by IS NULL RETURNING id",
        (name, gift_id)
    )
    success = cur.fetchone() is not None
    conn.commit()
    cur.close()
    conn.close()
    return success