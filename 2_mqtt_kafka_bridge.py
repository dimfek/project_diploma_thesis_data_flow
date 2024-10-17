'''
mqtt_kafka_bridge consumes messages from mqtt broker
and then publishes the messages to kafka broker
'''
import paho.mqtt.client as mqtt
from pykafka import KafkaClient
import time

#must connect to mqtt broker and to kafka producer (or mqtt client)

mqtt_client = mqtt.Client('Apache Kafka')
mqtt_client.connect('localhost', 1883, 60)

#connect to apache kafka broker and produce data to topic temperature
kafka_client = KafkaClient(hosts='localhost:9092')
kafka_topic = kafka_client.topics['temperature']
kafka_producer = kafka_topic.get_sync_producer()

#whenever we receive a message from the mqtt broker, we publish it to kafka broker (topic temperature)
def on_message(client, userdata, message):
    msg_payload = str(message.payload.decode("utf-8"))
    print('Received MQTT message ', msg_payload)
    kafka_producer.produce(str(msg_payload).encode('ascii'))
    print('KAFKA: Just published ' + msg_payload + ' to topic temperature')

#read messages from mqtt topic temperature
mqtt_client.loop_start()
mqtt_client.subscribe('temperature')
mqtt_client.on_message = on_message
time.sleep(100)
mqtt_client.loop_stop()

