from time import sleep
from  __init__ import connect, count, led_off, led_on, read_sensor_humidity, read_sensor_temperature


def main():
    print("Step 1/3: Count and print")
    for _ in range(3):
        c = count()
        print(c)
        sleep(1)

    print("\nStep 2/3: LED blinking for 5 seconds")
    for _ in range(5):
        led_on()
        sleep(.5)
        led_off()
        sleep(.5)

    print("\nStep 3/3: Display humidity, temp and blinking LED for 10 seconds")
    for i in range(10):
        is_even = i % 2 == 0
        led_on() if is_even else led_off()
        msg = (
            "=====================\n"
            f"Time: {i+1} seconds\n"
            f"Temperature: {read_sensor_temperature()}C\n"
            f"Humidity: {read_sensor_humidity()}%\n"
        )
        print(msg)
        sleep(1)
    return 0


if __name__ == "__main__":
    connect()
    main()
