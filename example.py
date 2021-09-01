import RPi.GPIO as GPIO
import adafruit_dht # Importing a library used for the DHT22 which is the same as our AM2302 
import board
from time import sleep
from datetime import datetime

# These might be placed in a seperate "constants.py"
_ledPin = 17
_am2302Pin = board.D2

humThreashold = 55
tempThreashold = 30

def main():

    #Generall GPIO setup
    GPIO.setmode(GPIO.BCM) # Each pin on the Raspberry Pi has several different names, so you need to tell the program which naming convention is to be used.
    GPIO.setwarnings(False)

    GPIO.setup(_ledPin, GPIO.OUT) # Setting the led pin as an output to be able to turn it on and off
    GPIO.output(_ledPin, GPIO.HIGH) # Turn of LED
    
    while True:
        sleep(1) #Because the AM2302 is tricky to read from, this will smooth out the terminal output
        try:
            am2302 = adafruit_dht.DHT22(_am2302Pin, use_pulseio=False) # Read data from the AM2302

            h = am2302.humidity
            t = am2302.temperature

            print("Humidity:%d - Temperature:%d" %(h, t))

            if h > humThreashold:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Warning: The humidity(%d) is too high -" % h, dt_string)
                GPIO.output(_ledPin, GPIO.LOW) # Turning on the LED
            else:
                GPIO.output(_ledPin, GPIO.HIGH) # Turning off the LED

            # If the temperature is higher than a given threashold the led will flash
            while t > tempThreashold:
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                print("Warning: The temperature(%d) is too high -" % t, dt_string)
                GPIO.output(_ledPin,GPIO.LOW) # Turn on LED
                sleep(1)
                GPIO.output(_ledPin,GPIO.HIGH) # Turn off LED
                am2302 = adafruit_dht.DHT22(board.D2, use_pulseio=False) # Read the current values
        
        except RuntimeError as error:
            continue # Using the AM2302 needs some of this "tom foolery"

        except Exception as error:
            am2302.exit
            raise error
        
             
if __name__ == "__main__":
    main()