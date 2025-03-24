from gpiozero import Device, Button
from signal import pause

# Define Buttons using BCM numbering with internal pull-ups and debounce (bounce_time)
stop_button   = Button(5, pull_up=True, bounce_time=0.6)
preset1_button = Button(6, pull_up=True, bounce_time=0.6)
preset2_button = Button(13, pull_up=True, bounce_time=0.6)
preset3_button = Button(12, pull_up=True, bounce_time=0.6)
preset4_button = Button(20, pull_up=True, bounce_time=0.6)

# Callback for the STOP button
def stop_callback():
    print("Stop button pressed on GPIO 5")

# Callbacks for preset buttons
def preset1_callback():
    print("Preset 1 button pressed")

def preset2_callback():
    print("Preset 2 button pressed")

def preset3_callback():
    print("Preset 3 button pressed")

def preset4_callback():
    print("Preset 4 button pressed")

# Attach callbacks to button events
stop_button.when_pressed   = stop_callback
preset1_button.when_pressed = preset1_callback
preset2_button.when_pressed = preset2_callback
preset3_button.when_pressed = preset3_callback
preset4_button.when_pressed = preset4_callback

print("Monitoring buttons. Press Ctrl+C to exit.")
pause()
