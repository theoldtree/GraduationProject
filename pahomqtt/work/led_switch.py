from gpiozero import Button, LED
from signal import pause

led_red = LED(4)
button_red = Button(14)
status = 0

def do_signal():
    led_red.on()
    print(1)
    

while True:
    button_red.when_pressed = do_signal
    button_red.when_released = led_red.off
            
