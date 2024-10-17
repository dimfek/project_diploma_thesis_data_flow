from kafka import KafkaConsumer
import json
import pyrebase

firebaseConfig = {
    'apiKey': "################",
    'authDomain': "#################",
    'projectId': "#####################",
    'storageBucket': "###################",
    'messagingSenderId': "######################",
    'appId': "####################################",
    'databaseURL': "####################################"  #add database_url
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

