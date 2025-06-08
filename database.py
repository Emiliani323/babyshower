import os
import psycopg2
from dotenv import load_dotenv
from contextlib import contextmanager

load_dotenv()

@contextmanager
def db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port=os.getenv('DB_PORT')
    )
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def db_cursor():
    with db_connection() as conn:
        cur = conn.cursor()
        try:
            yield cur
            conn.commit()
        except:
            conn.rollback()
            raise
        finally:
            cur.close()

def init_db():
    with db_cursor() as cur:
        # Create gifts table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS gifts (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                amazon_link TEXT NOT NULL UNIQUE,
                reserved_by TEXT,
                image_url TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create index for better performance
        cur.execute("""
            CREATE INDEX IF NOT EXISTS idx_reserved_by 
            ON gifts(reserved_by)
        """)
        
        # Check if table is empty
        cur.execute("SELECT COUNT(*) FROM gifts")
        if cur.fetchone()[0] == 0:
            from initial_data import initial_gifts
            # Insert all gifts using executemany for efficiency
            cur.executemany(
                """INSERT INTO gifts (name, amazon_link, image_url) 
                VALUES (%(name)s, %(link)s, %(image_url)s)
                ON CONFLICT (amazon_link) DO NOTHING""",
                initial_gifts
            )

def get_all_gifts():
    with db_cursor() as cur:
        cur.execute("""
            SELECT id, name, amazon_link, reserved_by, image_url 
            FROM gifts ORDER BY id
        """)
        return [
            {
                "id": id,
                "name": name,
                "link": amazon_link,
                "reserved_by": reserved_by,
                "image_url": image_url
            }
            for id, name, amazon_link, reserved_by, image_url in cur.fetchall()
        ]

def reserve_gift(gift_id, guest_name):
    with db_cursor() as cur:
        cur.execute("""
            UPDATE gifts 
            SET reserved_by = %s, updated_at = CURRENT_TIMESTAMP
            WHERE id = %s AND reserved_by IS NULL
            RETURNING id
        """, (guest_name, gift_id))
        return cur.fetchone() is not None