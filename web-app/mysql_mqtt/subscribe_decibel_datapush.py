# callback - 구독신청 후 broker와 접속이 완료됐을때
# callback - broker가 보낸 메세지가 도착했을때
import paho.mqtt.client as mqtt
import pymysql
import datetime

#Client(subscriber)가 broker에 접속이 완료된 경우 호출
def connect_result(client,userdata,flags,rc): #rc가 0이면 접속성공, 1이면 접속실패
    print("connect...", rc)
    if rc == 0 :
        client.subscribe("iot/decibel") # iot/로 시작하는 topic은 모두 구독
    else :
        print("연결실패")

def on_message(client,userdata,message):
    print(client)
    myval = message.payload.decode("utf-8")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    (room,decibel) = myval.split(",")
    print(time,room,decibel)
    con = pymysql.connect(host='localhost',user='root',passwd='tlqkf12!@',db='pighouse')
    cur = con.cursor()
    sql = "INSERT INTO decibel (time,room,decibel) values (%s,%s,%s)"
    cur.execute(sql,(time,room,decibel))
    con.commit()
    con.close()



try:
    mqttClient = mqtt.Client()
    mqttClient.on_connect = connect_result
    mqttClient.on_message = on_message

    # broker에 접속하기
    mqttClient.connect("localhost",1883,60)
    mqttClient.loop_forever()
except KeyboardInterrupt:
    pass
finally:
    pass