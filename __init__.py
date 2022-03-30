import RPi.GPIO as GPIO
import board
import adafruit_dht # Importing a library used for the DHT22 which is the same as our AM2302 
#import botbook_mcp3002 as mcp # For MQ-2 smoke sensor

_led_pin = 21
_am2302_pin = board.D2
_pir_pin = 8

def connect():
    while True:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            break

        except RuntimeError as error:
            print("Could not establish a connection to the Raspberry Pi")

def read_sensor_temperature():
    """
    Returns the temperature as [some unit]
    """
    t = 0
    while t == 0:
        try:
            am2302 = adafruit_dht.DHT22(_am2302_pin, use_pulseio=False)
            t = am2302.temperature
        except RuntimeError as error:
            continue
    
    return t

def read_sensor_humidity():
    """
    Returns the humidity as [some unit]
    """
    h = 0
    while h == 0:
        try:
            am2302 = adafruit_dht.DHT22(_am2302_pin, use_pulseio=False)
            h = am2302.humidity
        except RuntimeError as error:
            continue
    
    return h

def read_sensor_gas():
    """
    Returns the gas level as [some unit]
    """
    return mcp.readAnalog()

def read_sensor_distance():
    not_available = -1
    return not_available

def read_sensor_pir():
    """
    Returns motion as [some unit]
    """
    GPIO.setup(_pir_pin, GPIO.IN)
    motion = GPIO.input(_pir_pin)
    return motion

def led_on():    
    GPIO.setup(_led_pin, GPIO.OUT)
    GPIO.output(_led_pin, GPIO.LOW) # Turn on LED


def led_off():
    GPIO.setup(_led_pin, GPIO.OUT)
    GPIO.output(_led_pin, GPIO.HIGH) # Turn off LED
