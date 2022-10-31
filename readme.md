# Automation for Raspberry Pi Halloween Projection.

## Setup:
The setup is pretty straight forward
1. Install Raspberry pi os
2. Connect the projector using hdmi (mini hdmi adapter required)
3. Connect Bluetooth audio 

## How to install the code
1. Clone the repository into a folder.
2. Enable to run the program at startup
3. Enable bluetooth audio at startup
4. Install packages

### Enable to run the program at startup
1. sudo nano /etc/xdg/autostart/display.desktop
2. In the desktop add the following code
``` 
[Desktop Entry]
Name=PiCounter
Exec=sh /home/harsha2bits/Documents/HalloweenAutomation/launcher.sh >/home/harsha2bits/Documents/HalloweenAutomation/logs/cronlog 2>&1
```

### Enable Bluetooth at startup
source: https://wiretuts.com/connecting-bluetooth-audio-device-to-raspberry-pi

1. sudo apt-get update
2. sudo apt-get install pulseaudio*
3. sudo usermod -a -G lp harsha2bits
4. sudo reboot
5. pulseaudio --start
6. sudo bluetoothctl
7. power on
8. default-agent
9. scan on
10. You will something like xx:xx:xx sound core motion boom
11. trust xx:xx:xx:xx
12. pair xx:xx:xx:xx
13. connect xx:xx:xx:xx
14. exit
15. pactl list cards short
16. pactl list cards
17. paplay -p --device=2 /usr/share/sounds/alsa/Front_Center.wav
18. In your home type touch btconnect.sh
19. chmod +x btconnect.sh
20. nano btconnect.sh
21. paste this code in it 
22. ``` 
    #!/bin/bash
    pulseaudio --start
    bluetoothctl power on
    bluetoothctl connect XX:XX:XX:XX
    ```
23. crontab -e
24. @reboot /home/pi/btconnect.sh

