import requests
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DEBOUNCE = 600  # switch debounce time in ms
loop_count = 0  # loop counter for checking the current sound status
now_playing = ""  # name of currently playing file or emply string

P1_GPIO = 6
P2_GPIO = 13
P3_GPIO = 12 # was 19
P4_GPIO = 20
STOP_GPIO = 5

def button_stop(channel):
    #
    # stop payback
    #
    global now_playing
    r = requests.post('http://noise:5000/stop/')
    print("Stop button pressed.")
    #now_playing = ""
    #display_now(idle_image)

def button_preset(channel):
    #
    # play a preset
    #
    # get preset number (1-4) from channel
    preset_channel = [P1_GPIO, P2_GPIO, P3_GPIO, P4_GPIO]
    presety = preset_channel.index(channel)
    # get preset name value from redis
    r = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
    p = r.get("p" + str(presety + 1))
    print("Preset {0} ({1}) pressed.".format(p, presety))
    # play/display the file image
    if p is None:
        print("No preset value for {}".format(presety))
    else:
        text_icon = ["\U000F03A4", "\U000F03A7", "\U000F03AA", "\U000F03AD"]
        play_file(p, text_icon[presety])  

print("Starting...")

# Set button inputs
# stop
GPIO.setup(STOP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(STOP_GPIO, GPIO.RISING, callback=button_stop, bouncetime=DEBOUNCE)

# preset 1
GPIO.setup(P1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(P1_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)

# preset 2
GPIO.setup(P2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(P2_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)

# preset 3
GPIO.setup(P3_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(P3_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)

#preset 4
GPIO.setup(P4_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(P4_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)

while True:
    loop_count = loop_count + 1
    if loop_count == 5:
        loop_count = 0
        #  Check to see if some other process has changed the status
        try:
            r = requests.get('http://noise:5000/')
        except:
            print("Error accessing noise service.")
        j = r.json()
        if j["status"] == "stop":
            if now_playing != "":
                now_playing = ""
                display_now(idle_image)
        else:
            if now_playing != j["file"]:
                now_playing = j["file"]
                display_now(img_list[wav_list.index(now_playing)])
        # See if we need to save a new volume level in Redis
        #if current_volume != new_volume:
            # Save volume in Redis
        #    try:
        #        redis_conn.set('v', current_volume)
        #   except:
         #       print("Error saving volume data to Redis.")
         #   new_volume = current_volume

    time.sleep(2)
