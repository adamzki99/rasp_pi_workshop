import RPi.GPIO as GPIO
import Adafruit_DHT as dht # Importing a library used for the DHT22 which is the same as our AM2302 
from time import sleep
from datetime import datetime

# These might be placed in a seperate "constants.py"
_ledPin = 17
_am2302Pin = 2

humThreashold = 0
tempThreashold = 0

def main():

    #Generall GPIO setup
    GPIO.setmode(GPIO.BCM) # Each pin on the Raspberry Pi has several different names, so you need to tell the program which naming convention is to be used.
    GPIO.setwarnings(False)

    GPIO.setup(_ledPin, GPIO.OUT) # Setting the led pin as an output to be able to turn it on and off
    
    while True:
        
        h,t = dht.read_retry(dht.DHT22, _am2302Pin) # Reading the temperature (t) and humidity (h)

        if h > humThreashold:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Warning: The humidity is high - ", dt_string)
            GPIO.output(_ledPin, GPIO.HIGH) # Turning on the LED
        else:
            GPIO.output(_ledPin, GPIO.LOW) # Turning off the LED

        # If the temperature is higher than a given threashold the led will flash
        while t > tempThreashold:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Warning: The temperature is high - ", dt_string)
            GPIO.output(_ledPin,GPIO.HIGH)
            sleep(0.5)
            GPIO.output(_ledPin,GPIO.LOW)
             
if __name__ == "__main__":
    main()