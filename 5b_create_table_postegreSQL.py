import psycopg2


conn = psycopg2.connect(
    database = "postgres",
    user = "##########",
    password = "##########",
    host= "##########",
    port = "##########"
)

print("Database Connected Successfully")

cur = conn.cursor()
cur.execute("""

CREATE TABLE SensorData
(
ID INT PRIMARY KEY NOT NULL,
TIME TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
TEMPERATURE FLOAT NOT NULL
)
""")

conn.commit()
print("Table created successfully")
    
