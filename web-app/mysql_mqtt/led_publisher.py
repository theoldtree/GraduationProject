from gpiozero import Button
from gpiozero import LED
from datetime import datetime
import paho.mqtt.publish as publisher

button_red = Button(17)
led_red = LED(22)
button_green = Button(24)
led_green = LED(25)
state = 0

stringdate = datetime.strftime(datetime.now())
print(stringdate)

def red_button_pressed():
    state = 0
    led_red.on()
    publisher.single("iot/led",state,hostname='localhost')

def red_button_released():
    led_red.off()

def green_button_released():
    led_green.off()

def green_button_pressed():
    state = 1
    led_green.on()
    publisher.single("iot/led",state,hostname='localhost')

while True:
    button_red.when_pressed = red_button_pressed
    button_green.when_released = red_button_released
    button_green.when_pressed = green_button_pressed
    button_green.when_released = green_button_released

if __name__ == "__main__":
    while True:
        showMenu()
        num = int(input("select your job"))
        led_state = ""
        if num == 1 :
            led_state = "led_on"
        elif num == 2:
            led_state = "led_off"
        else:
            exit(0)
            
        publisher.single("iot/led",state,hostname = "172.1.30.71")