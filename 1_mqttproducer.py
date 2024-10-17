import paho.mqtt.client as mqtt
from pyfirmata import Arduino, util
import pyfirmata
import time

#connect mqtt client(Arduino - sensor) to mqtt broker (shiftr.io)
mqtt_client = mqtt.Client('Arduino')        #name of mqtt client
mqtt_client.connect('localhost', 1883, 60)  #connect to mqtt broker


#Arduino - mqtt client producer (temperature data)
port = "COM3"
board = Arduino(port) #connect arduino to usb port

it = pyfirmata.util.Iterator(board) #start reading analog input
it.start()

pin = board.get_pin('a:0:i')  #A0 Analog Input

while True:
        time.sleep(0.1)
        voltage = pin.read()  #read voltage input
        #print(voltage)
        if voltage is not None: #first read after startup is sometimes None
                temp = 3.3  * 100 * voltage #convert voltage to temperarture
                #publish temperature data to topic temperature
                mqtt_client.publish('temperature', temp)
                print('MQTT: Just published ', temp,'°C', 'to topic temperature')
                time.sleep(1)  #1 sec waiting



