import paho.mqtt.publish as publisher

publisher.single("iot/led","led_on",hostname="192.168.1.73")