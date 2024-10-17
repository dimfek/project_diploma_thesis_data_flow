import psycopg2

try:
    conn = psycopg2.connect(
        database = "postgres",
        user = "###########",
        password = "###########",
        host= "############",
        port = "#########"
    )
    print("Database connected successfully")

except:
    print("Database not connected")
