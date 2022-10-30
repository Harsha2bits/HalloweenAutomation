#import os
#import terminal_video_player_py as tvp
import vlc
path_folder ="assets/"
file_name ="1.jpeg"
path =path_folder+file_name
#os.open(path,3)
#tvp(path)
# creating vlc media player object
media = vlc.MediaPlayer(path)

# start playing video
media.play()
