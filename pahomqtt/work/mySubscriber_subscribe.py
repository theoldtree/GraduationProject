#callback - 구독신청 후 broker와 접속이 완료됐을때
#callback - broker가 보낸 메세지가 도착했을때

import paho.mqtt.client as mqtt

#client(subscriber)가  broker에 접속이 완료된 경우 호출
def connect_result(client,userdata,flag,rc): #rc가 0이면 접속 성공, 1이면 실패
    print("connect..."+str(rc))
    if rc ==0:
        client.subscribe("iot/#") # 구독신청 - iot 로 시작하는 모든 토픽 구독
    else:
        print("연결실패")

def on_message(client,userdata,message):
    myval = message.payload.decode("utf-8")
    print(myval)
    
try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message
    
    #broker에 접속하기
    mqttClient.connect("172.30.1.71",1883,10)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass