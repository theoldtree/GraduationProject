import paho.mqtt.publish as publisher
def showMenu():
    print("select menu")
    print("1.led on")
    print("2.led off")
    print("3.system off")
    
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
            
        publisher.single("iot/led",led_state,hostname = "172.1.30.71")