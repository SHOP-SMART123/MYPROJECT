from fastapi import FastAPI
from pydantic import BaseModel
from passlib.context import CryptContext  # ✅ For hashing passwords
from db import connect  # ✅ Your database connection function

app = FastAPI()

# ✅ Set up password hasher
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# ✅ Pydantic model for user data
class User(BaseModel):
    name: str
    email: str
    password: str

@app.get("/")
def read_root():
    return {"message": "FastAPI is working ✅"}

# ✅ POST route to add user to DB with encrypted password
@app.post("/add_user")
def add_user(user: User):
    # 🔐 Hash the password before storing it
    hashed_password = pwd_context.hash(user.password)

    # 🔌 Connect to DB and insert
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (user.name, user.email, hashed_password)
    )
    conn.commit()
    conn.close()

    # ✅ Return confirmation
    return {
        "message": "User added successfully",
        "name": user.name,
        "email": user.email,
        "hashed_password": hashed_password
    }

@app.get("/get_users")
def get_users():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT user_id, username, email, password_hash, full_name, phone, address, is_active, created_at
            FROM users
        """)
        users = cursor.fetchall()
        conn.close()

        # Convert each tuple into a dictionary
        user_list = []
        for row in users:
            user_list.append({
                "user_id": row[0],
                "username": row[1],
                "email": row[2],
                "password_hash": row[3],
                "full_name": row[4],
                "phone": row[5],
                "address": row[6],
                "is_active": row[7],
                "created_at": str(row[8])  # Convert datetime to string
            })

        return {"users": user_list}

    except Exception as e:
        return {"error": str(e)}