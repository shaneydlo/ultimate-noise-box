import requests
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

P1_GPIO = 6
P2_GPIO = 13
P3_GPIO = 12 # was 19
P4_GPIO = 20
DISP_GPIO = 22 # was 21
STOP_GPIO = 5

print("Starting...")

# Set button inputs
# stop
GPIO.setup(STOP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(STOP_GPIO, GPIO.RISING, callback=button_stop, bouncetime=DEBOUNCE)

#display
GPIO.setup(DISP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(DISP_GPIO, GPIO.RISING, callback=button_display, bouncetime=DEBOUNCE+200)

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

#rotaryio interrupt
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(17, GPIO.FALLING, callback=rotary_incoming)

time.sleep(2)
