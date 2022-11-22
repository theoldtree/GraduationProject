import paho.mqtt.client as client

# 메세지 전송하고 다시 돌아와서 실행될 callback 함수
def publish_ok(client,userdata,mid):
    print(client,userdata,mid)
    print("data complete, publish를 다양한 위치했을때 처리하고 싶은 일이 있는 경우")

try:
    mqttClient = client.Client("python_pc_pub")
    mqttClient.connect("localhost")
    mqttClient.on_publish = publish_ok
    result = mqttClient.publish("iot/led","led~~~~")
    print("호출결과",result)
    mqttClient.loop(2)
except Exception as err:
    print("에러",err)