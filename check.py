from time import sleep
from __init__ import *
from __motor_controll__ import *

def main():
    print("Testing workshop")
    c = 0
    while c < 3:
        c = count()
        print(c)

    c = 0
    print("The LED lamp should blink for 5 seconds")
    while c < 5:
        led_on()
        sleep(.5)
        led_off()
        sleep(.5)
        c += 1

    c = 0
    print("The terminal should display humidity, temp and motion for 20 seconds")
    print("and the LED should blink")
    while c < 20:
        led_on() if c%2==0 else led_off()
        print("=====================")
        print(f"Time: {c+1} seconds")
        print(f"Temperature: {read_sensor_temperature()}C")
        print(f"Humidity: {read_sensor_humidity()}%")
        string = "DETECTED!" if read_sensor_motion() else "Nothing..."
        print(f"Motion: {string}")
        c += 1
        sleep(1)
    return 0
if __name__ == "__main__":
    connect()
    main()