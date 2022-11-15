import paho.mqtt.publish as publisher

publisher.single("iot/led","led_on",hostname="localhost")