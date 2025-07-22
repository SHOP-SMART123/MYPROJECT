from db import connect
from datetime import datetime

def insert_user(conn):
    cursor = conn.cursor()
    query = """
    INSERT INTO Users (username, email, password_hash, full_name, phone, address)
    VALUES (%s, %s, %s, %s, %s, %s)
    RETURNING user_id;
    """
    data = ('testuser', 'test@example.com', 'hashed_pw', 'Test User', '03001234567', 'Test Address')
    cursor.execute(query, data)
    user_id = cursor.fetchone()[0]
    conn.commit()
    print("User inserted:", user_id)

conn = connect()
if conn:
    insert_user(conn)
    conn.close()
pass