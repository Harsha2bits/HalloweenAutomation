from paho.mqtt import client as mqtt_client
import time


broker = '192.168.1.113'
port = 1883
pubtopic = "python/mqttpub"
topicsub = "python/mqttsub"
client_id = f'python-mqtt-1'
username = 'harsha2bits'
password = 'LeanderLion@1604'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(pubtopic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent `{msg}` to topic `{pubtopic}`")
        else:
            print(f"Failed to send message to topic {pubtopic}")
        msg_count += 1


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(client)
        print(userdata)
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topicsub)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
