from paho.mqtt import client as mqtt_client
import time
import vlc

# VLC video path
path_folder = "assets/"
file_name = "1.mp4"
path = path_folder+file_name

# MQTT info
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


# def publish(client):
#     msg_count = 0
#     while True:
#         time.sleep(1)
#         msg = f"messages: {msg_count}"
#         result = client.publish(pubtopic, msg)
#         # result: [0, 1]
#         status = result[0]
#         if status == 0:
#             print(f"Sent `{msg}` to topic `{pubtopic}`")
#         else:
#             print(f"Failed to send message to topic {pubtopic}")
#         msg_count += 1


def publish_complete(client):
    msg = "done"
    result = client.publish(pubtopic,msg)
    status = result[0]
    if status == 0:
        print(f"Sent `{msg}` to topic `{pubtopic}`")
    else:
        print(f"Failed to send message to topic {pubtopic}")


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(client)
        print(userdata)
        data = msg.payload.decode()
        print(f"Received `{data}` from `{msg.topic}` topic")
        if data == "1":
            print("play_the_video")
            play_video()  #Function to play video
            print("Video played")
            publish_complete(client)

    client.subscribe(topicsub)
    client.on_message = on_message


def play_video():
    # creating vlc media player object
    media_player = vlc.MediaPlayer()
    # toggling full screen
    media_player.toggle_fullscreen()
    # media object
    media = vlc.Media(path)
    # setting media to the media playergit
    media_player.set_media(media)
    media_player.play()
    playing = set([1, 2, 3, 4])
    play = True
    while play:
        time.sleep(0.5)
        state = media.get_state()
        if state in playing:
            continue
        else:
            play = False
            media_player.stop()
            return


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    # Play blank video in loop
    while True:
        None


if __name__ == '__main__':
    run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
