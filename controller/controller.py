import os
import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# Define your GPIO pins
P1_GPIO = 6
P2_GPIO = 13
P3_GPIO = 12
P4_GPIO = 20
STOP_GPIO = 5

DEBOUNCE = 600  # debounce time in milliseconds

# Callback for the STOP button
def button_stop(channel):
    print("Stop button pressed on GPIO", channel)
    
# Callback for preset buttons (P1-P4)
def button_preset(channel):
    if channel == P1_GPIO:
        print("Preset 1 button pressed")
    elif channel == P2_GPIO:
        print("Preset 2 button pressed")
    elif channel == P3_GPIO:
        print("Preset 3 button pressed")
    elif channel == P4_GPIO:
        print("Preset 4 button pressed")
    else:
        print("Unknown preset button pressed on GPIO", channel)

# Setup GPIO inputs with internal pull-up resistors
GPIO.setup(STOP_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(P1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(P2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(P3_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(P4_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Add edge detection to each button with debouncing
GPIO.add_event_detect(STOP_GPIO, GPIO.RISING, callback=button_stop, bouncetime=DEBOUNCE)
GPIO.add_event_detect(P1_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)
GPIO.add_event_detect(P2_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)
GPIO.add_event_detect(P3_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)
GPIO.add_event_detect(P4_GPIO, GPIO.RISING, callback=button_preset, bouncetime=DEBOUNCE)

print("Monitoring buttons. Press Ctrl+C to exit.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()
