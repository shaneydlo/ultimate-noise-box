from gpiozero import Device, Button
from gpiozero.pins.lgpio import LgpioFactory
from signal import pause

# Use the lgpio pin factory for Pi 5 hardware
Device.pin_factory = LgpioFactory()

# Define button inputs on GPIO pins 5 and 6 (using BCM numbering)
button_pin5 = Button(5, pull_up=True)#, bounce_time=0.2)
button_pin6 = Button(6, pull_up=True)#, bounce_time=0.2)

# Define callback functions for when the buttons are pressed
def on_button5_pressed():
    print("Button on GPIO 5 pressed")

def on_button6_pressed():
    print("Button on GPIO 6 pressed")

print("Polling button states. (Idle state should be 1; pressed state should be 0)")
while True:
    print("Button 5:", button5.value, "Button 6:", button6.value)
    time.sleep(0.5)

# Attach the callbacks to the button events
#button_pin5.when_pressed = on_button5_pressed
#button_pin6.when_pressed = on_button6_pressed

#print("Monitoring button inputs on GPIO 5 and 6. Press Ctrl+C to exit.")
#pause()
