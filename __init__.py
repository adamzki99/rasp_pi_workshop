import RPi.GPIO as GPIO
import adafruit_dht  # DHT22 library can be used for AM2302
from microcontroller import Pin

LED_PIN = 21
AM2302_PIN = Pin(2)
PIR_MOTION_PIN = 8
DHT_SENSOR = adafruit_dht.DHT22(AM2302_PIN)

GPIO.setwarnings(False)

INVALID_VALUE = -1


def connect():
    while True:
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            break

        except RuntimeError:
            print("Could not establish a connection to the Raspberry Pi")


_count = 0


def count():
    global _count
    _count += 1
    return _count


def read_sensor_temperature():
    """
    Returns the temperature as celsius
    """
    temperature = 0

    try:
        temperature = DHT_SENSOR.temperature
    except Exception:
        return INVALID_VALUE

    if temperature is None:
        return INVALID_VALUE

    return temperature


def read_sensor_humidity():
    """
    Returns the humidity as relative humidity
    """
    humidity = 0

    try:
        humidity = DHT_SENSOR.humidity
    except (RuntimeError, Exception):
        return INVALID_VALUE

    if humidity is None:
        return INVALID_VALUE

    return humidity


def led_on():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)  # Turn on LED


def led_off():
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.HIGH)  # Turn off LED
