The purpose of this application is to represent the data flow from the acquisition of data from sensors to the storage of data in databases 
(such as PostgreSQL, MongoDB, Firebase Real Time Database) and the visualization of data in various dashboards with the use of the Python 
programming language. Initially, a sensor transmits its temperature values from the Arduino microcontroller to a topic on the MQTT Broker. 
Subsequently, these values are transferred via a mediator to the Kafka Broker. Finally, the data is transferred to various databases and 
is represented in charts (Grafana).

![image](https://github.com/user-attachments/assets/5953ebbf-facc-4639-8fd4-deb24715cd86)
