import RPi.GPIO as GPIO
import board
import adafruit_dht # Importing a library used for the DHT22 which is the same as our AM2302 
#import botbook_mcp3002 as mcp # For MQ-2 smoke sensor

_led_pin = 21
_am2302_pin = board.D2
_pir_pin = 8

def create_connection():
    while 1:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            break

        except RuntimeError as error:
            print("Could not establish a connection to the Raspberry Pi")

def read_sensor(sensor_type:str):
    
    if sensor_type == 'Temperature':
        t = 0
        while t == 0:
            try:
                am2302 = adafruit_dht.DHT22(_am2302_pin, use_pulseio=False)
                t = am2302.temperature
            except RuntimeError as error:
                continue
        
        return t

    elif sensor_type == 'Humidity':
        h = 0
        while h == 0:
            try:
                am2302 = adafruit_dht.DHT22(_am2302_pin, use_pulseio=False)
                h = am2302.humidity
            except RuntimeError as error:
                continue
        
        return h

    elif sensor_type == "Gas": # Seems like we need another chip (MCP 3002) to read the value
        return mcp.readAnalog()

    elif sensor_type == "Distance":
        return -1
    elif sensor_type == "PIR":
        GPIO.setup(_pir_pin, GPIO.IN)
        motion = GPIO.input(_pir_pin)
        return motion
    elif sensor_type == "":
        return -1
    elif sensor_type == "":
        return -1

def led_on():    
    GPIO.setup(_led_pin, GPIO.OUT)
    GPIO.output(_led_pin, GPIO.LOW) # Turn on LED


def led_off():
    GPIO.setup(_led_pin, GPIO.OUT)
    GPIO.output(_led_pin, GPIO.HIGH) # Turn off LED
