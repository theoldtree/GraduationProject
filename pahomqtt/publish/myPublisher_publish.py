import paho.mqtt.client as client

# 메세지를 전송하고 다시 되돌아와서 실행돌 callback 함수
def publish_ok(client,userdata,mid):
    print(client,userdata,mid)
    print("data transmit complete 메세지를 봰고 되돌아와서 처리할 일이 잇는경우") 
try:
    mqttClient = client.Client("python_pc_pub")
    mqttClient.connect("172.30.1.71",1883)
    mqttClient.on_publish = publish_ok
    result = mqttClient.publish("iot/led","led on")
    print("호출결과",result)
    mqttClient.loop(2)
except Exception as err:
    print("에러",err)