from kafka import KafkaConsumer
import json
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyD61QMHqVQjPvK2ZlpJ5Hl5rAH0DJ2hEMo",
    'authDomain': "mqtt-apachekafka.firebaseapp.com",
    'projectId': "mqtt-apachekafka",
    'storageBucket': "mqtt-apachekafka.appspot.com",
    'messagingSenderId': "339179220797",
    'appId': "1:339179220797:web:355350b4d787a8a69d1f54",
    'databaseURL': "https://mqtt-apachekafka-default-rtdb.europe-west1.firebasedatabase.app/"  #add database_url
}
#To inititialize the app with these configuration information
firebase = pyrebase.initialize_app(firebaseConfig)

#Realtime Database
db = firebase.database()    #connect to database

#connect to apache kafka and subscribe to topic temperature
consumer = KafkaConsumer('temperature')
for msg in consumer:
    data = msg.value.decode("utf-8")
    print(data)
    db.child('temperature').push(data) #push data to firebase database

