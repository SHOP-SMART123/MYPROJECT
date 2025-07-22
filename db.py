import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            dbname="SHOP SMART BY MAHRUKH",
            user="postgres",
            password='123456789',  # ✅ Add your password
            host="localhost",
            port="5432"
        )
        print("Connected successfully!")
        return conn
    except Exception as e:
        print("Connection failed:", e)

print("Script is running!")

# Call the function to check the connection
connect()
