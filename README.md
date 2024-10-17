The purpose of this application is to represent the data flow from the acquisition of data from sensors to the storage of data in databases 
(such as PostgreSQL and MongoDB) and the visualization of data in various charts (dashboards). Initially, a sensor transmits its values to 
a topic on the MQTT Broker. Subsequently, these values are transferred via a mediator to the Kafka Broker. Finally, the data is transferred 
to various databases and is represented in charts (Grafana).
