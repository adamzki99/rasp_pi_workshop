import RPi.GPIO as GPIO
import Adafruit_DHT # Importing a library used for the DHT22 which is the same as our AM2302 
#import botbook_mcp3002 as mcp # For MQ-2 smoke sensor

LED_PIN = 21
AM2302_PIN = 2
PIR_PIN = 8
DHT_SENSOR = Adafruit_DHT.DHT22

GPIO.setwarnings(False)

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
    Returns the temperature as celsius
    """
    temperature = 0
    
    temperature = Adafruit_DHT.read_retry(DHT_SENSOR, AM2302_PIN)[1]
    
    return temperature

def read_sensor_humidity():
    """
    Returns the humidity as relative humidity
    """
    humidity = 0
    
    humidity = Adafruit_DHT.read_retry(DHT_SENSOR, AM2302_PIN)[0]
    
    return humidity

def read_sensor_gas():
    """
    Returns the gas level as [some unit]
    """
    return -1 #mcp.readAnalog()

def read_sensor_distance():
    not_available = -1
    return not_available

def read_sensor_pir():
    """
    Returns motion as [some unit]
    """
    GPIO.setup(PIR_PIN, GPIO.IN)
    motion = GPIO.input(PIR_PIN)
    return motion

def led_on():    
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW) # Turn on LED


def led_off():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH) # Turn off LED
