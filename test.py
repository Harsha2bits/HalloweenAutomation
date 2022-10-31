# #import os
# import vlc
path_folder ="assets/"
file_name ="1.mp4"
path =path_folder+file_name
# #os.open(path,os.O_RDONLY)
# print("playing video")
# # creating vlc media player object
# media = vlc.MediaPlayer(path)
#
# # start playing video
# media.play()

# importing vlc module
import vlc

# importing time module
import time

# creating vlc media player object
media_player = vlc.MediaPlayer()

# toggling full screen
media_player.toggle_fullscreen()

# media object
media = vlc.Media(path)

# setting media to the media playergit
media_player.set_media(media)

media_player.set_nsobject(self.GetHandle())

# start playing video
media_player.play()

# wait so the video can be played for 5 seconds
# irrespective for length of video
#time.sleep(10)

import vlc
import time

media = vlc.MediaPlayer("video.mp4")
media.play()
playing = set([1,2,3,4])
play = True
while play:
    time.sleep(0.5)
    state = media.get_state()
    if state in playing:
        continue
    else:
        play = False



VIDEO_PATH="/path/to/video.mp4"

def get_end_callback(mediaplayer):
    def end_callback(event):
        print("End of playing reached")
        mediaplayer.stop()
        mediaplayer.get_media().release()
        mediaplayer.release()
        mediaplayer.get_instance().release()
    return end_callback

def play():
    vlc_instance = vlc.Instance(["--no-xlib"])
    media_player = vlc.MediaPlayer(vlc_instance, VIDEO_PATH)
    media_player.set_xwindow(window.xid)
    media_player.play()

    event_manager = media_player.event_manager()
    event_manager.event_attach(vlc.EventType.MediaPlayerEndReached, get_end_callback(media_player))

play()
