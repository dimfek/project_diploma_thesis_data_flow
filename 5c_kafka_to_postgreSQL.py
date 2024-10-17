import psycopg2
from kafka import KafkaConsumer
import json
from datetime import datetime, timezone
import pytz

conn = psycopg2.connect(
    database = "postgres",
    user = "##########",
    password = "##########",
    host= "##########",
    port = "##########"
)

print("Database Connected Successfully")
cur = conn.cursor()
#connect to apache kafka and subscribe to topic temperature
consumer = KafkaConsumer('temperature')

i=0
timeZ_At = pytz.timezone('Europe/Athens')

for msg in consumer:
    data = msg.value.decode("utf-8")
    dt = datetime.now(timeZ_At)
    print(data, dt)
    i = i + 1
    # insert data to postgreSQL database
    cur.execute("INSERT INTO SensorData (ID, TIME,TEMPERATURE) VALUES(%s, %s, %s)", (i, dt, data))
    conn.commit()
print("Data inserted successfully")
conn.close()
