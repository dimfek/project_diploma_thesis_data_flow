from kafka import KafkaConsumer
import json
import pymongo   #pip install  pymongo


#connect to mongodb database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Kafka_to_MongoDB"]
mycol = mydb["SensorData"]

#connect to apache kafka and subscribe to topic temperature
consumer = KafkaConsumer('temperature')
for msg in consumer:
    data = msg.value.decode("utf-8")
    print(data)

    mydict = { "temperature": data}
    x = mycol.insert_one(mydict) #push data to 'SensorData' collection
