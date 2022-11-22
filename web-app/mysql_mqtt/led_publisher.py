from gpiozero import Button
from gpiozero import LED
from datetime import datetime
import paho.mqtt.publish as publisher

button_red = Button(17)
led_red = LED(22)
button_green = Button(24)
led_green = LED(25)
state = 0


def red_button_pressed():
    state = 0
    led_red.on()
    stringdate = datetime.now()
    stringdate = stringdate.strftime("%Y-%d-%m %H:%M:%S")
    message = str(state) + "/" + stringdate
    publisher.single("iot/led",message,hostname='localhost')

def green_button_pressed():
    state = 1
    led_green.on()
    stringdate = datetime.now()
    stringdate = stringdate.strftime("%Y-%d-%m %H:%M:%S")
    message = str(state) + "/" + stringdate
    publisher.single("iot/led",message,hostname='localhost')

def red_button_released():
    led_red.off()

def green_button_released():
    led_green.off()

button_red.when_pressed = red_button_pressed
button_green.when_released = red_button_released
button_green.when_pressed = green_button_pressed
button_green.when_released = green_button_released
