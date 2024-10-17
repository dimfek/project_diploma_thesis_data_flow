import psycopg2

try:
    conn = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "admin",
        host= "localhost",
        port = "5432"
    )
    print("Database connected successfully")

except:
    print("Database not connected")
