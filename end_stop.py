# using gpio 2

#working with end stop limit switch with signal(green) on pin 19 using GPIO.BOARD
#red: voltage(4), black:ground (6), green:signal(19)
button = 0

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    global button
    print("Button was pushed!:")
    print(button)
    button +=1
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(19,GPIO.FALLING,callback=button_callback,bouncetime=50) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
