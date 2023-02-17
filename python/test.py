import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825






#import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


# def button_callback(channel):
#     print("Button was pushed!")
# 	Motor1.TurnStep(Dir='forward', steps=1000, stepdelay = 0.00005)
	




# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# GPIO.add_event_detect(19,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
# message = input("Press enter to quit\n\n") # Run until someone presses enter
# GPIO.cleanup() # Clean up


try:
	Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20))
	# Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27))

	"""
	# 1.8 degree: nema23, nema14
	# softward Control :
	# 'fullstep': A cycle = 200 steps
	# 'halfstep': A cycle = 200 * 2 steps
	# '1/4step': A cycle = 200 * 4 steps
	# '1/8step': A cycle = 200 * 8 steps
	# '1/16step': A cycle = 200 * 16 steps
	# '1/32step': A cycle = 200 * 32 steps
	"""

	Motor1.SetMicroStep('hardward','fullstep')


	# while(1):
	# 	key = input()
	# 	if(key == 'a'): #forward

	# 		Motor1.TurnStep(Dir='forward', steps=1000, stepdelay = 0.00005)
	# 	if(key == 's'): #backward

	# 		Motor1.TurnStep(Dir='backward', steps=1000, stepdelay = 0.00005)

	# time.sleep(0.5)
	# Motor1.TurnStep(Dir='backward', steps=400, stepdelay = 0.005)
	# Motor1.Stop()

	"""
	# 28BJY-48:
	# softward Control :
	# 'fullstep': A cycle = 2048 steps
	# 'halfstep': A cycle = 2048 * 2 steps
	# '1/4step': A cycle = 2048 * 4 steps
	# '1/8step': A cycle = 2048 * 8 steps
	# '1/16step': A cycle = 2048 * 16 steps
	# '1/32step': A cycle = 2048 * 32 steps
	"""
	# Motor2.SetMicroStep('hardward' ,'halfstep')    
	# Motor2.TurnStep(Dir='forward', steps=2048, stepdelay=0.002)
	# time.sleep(0.5)
	# Motor2.TurnStep(Dir='backward', steps=2048, stepdelay=0.002)
	# Motor2.Stop()

	Motor1.Stop()
	
    
except:
    # GPIO.cleanup()
    print("\nMotor stop")
    Motor1.Stop()
    exit()



def button_callback(channel):
	print("Button was pushed!")
	Motor1.TurnStep(Dir='forward', steps=1700, stepdelay = 0.00005)
	




GPIO.setwarnings(False) # Ignore warning for now
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
