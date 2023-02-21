# Raspberry Pi Workshop Instructions

## Introduction

First we are going to command the computer to recognize the world through the Terminal.
Secondly we will make the computer say your name(s).
Thirdly we will make the computer count (and in seconds)
Fourthly we will have the computer turn on a LED lamp
5 we will make the LED lamp blink
6 we will read the humidity/temperature sensor
7 we will control the LED lamp based on humidity
Bonus: Make the LED blink if humidity is to high

Welcome to the Raspberry Pi Workshop!
Today you will learn how to program a small computer to detect the room's humidity and make a light turn on if the humidity is too high.
There will be a total of 7 tasks for you follow and complete for this workshop.

To perform the tasks, you will be using a Raspberry Pi; one of the smallest and fully featured computers available to hobbyists and professionals alike.

To control the Raspberry Pi you will make use of your previous computer experience and the easy-to-learn programming language Python.

Why Python? Python has become one of the most popular programming languages in the world in recent years. It is used in everything from creating Artificial Inteligenses (AIs) to building websites and connecting smart homes. It can be used by developers and non-developers alike.

## Task 0: Hello World

Before we begin, I want you to take a look on what you can see in the other document. 
You have a section called `List of available commands` where you can see what our software is capable of.
Underneeth is a section called `def main()`, this is where we will write all our code for this workshop.

The program that most developers begin with is "Hello World". In Python, this is a piece of cake! In the section `def main()` you use the command `print()` to get an output from your program. Between the parentheses, you write "Hello World" in citation notations, now you can execute the program by pressing the F5 key on your keyboard and see that the Raspberry Pi displays "Hello World" on the screen.

## Task 1: Hello You

One of the best and most useful features of software is that you can change it! Now change the output from the previous task to greet you with your name(s) instead of greeting the world. When finished, press F5 to run the code!

## Task 2: Good at counting

The second most powerful feature of software is repition, which makes computers great at counting. We will build a new section under your `print()` command called a "while loop" in python.
Create a new line under your `print()` and type `while True:` and then enter for a new line.
Great! Everything on this new line will now be repeated, but how do we check if it repeats? We make the computer print changes over time. 

We have a `count()` command telling the computer to count for us, and we can combine `print()` and `count()` to make the computer tell us how many times it have counted.
On the new line we created, type `print(count())` and then run the code with F5. If you see a number rapidly increasing its value, then you can go to the next task.

## Task 3: Counting seconds

Told you that computers are good at counting, look how fast it goes! Maybe a bit too fast...
As of now, counting as fast as possible won't be useful for us, let us make the computer count seconds instead so that we can track the time!

First however, we need to tell the computer to stop counting, we can force it to stop by pressing the red square that have appeared in the top middle of the screen, you can also hold down shift and press F5 to stop the program, or you can ask your guide for help.

How do we make the program count seconds? The easiest way would be to tell the computer to wait one second between counting. With python, we can do exactly that! We can make the program wait by using the `sleep()` command.
Let's add a new line underneath `print(count())` and type `sleep(1)`. Now our program will display the count, then wait a second, then loop back to count again!

## Task 4: Turn on the light

Refer to wiring schematic
Make led turn on after 1 second

## Task 5: Make a light show

Using the command `led_on()` and `led_off()` you can control the LED that is plugged in to the Raspberry Pi.

By using the command `while True:` we can make program run forever. and by using the command `sleep(0.5)` we can make the program wait for 0.5 second.

By using the commands mentioned above, make the LED blink.

If you did not wired everything you can start by just connecting the red LED to the Raspberry Pi.

![wiring schematic led](../images/wiring_schematic_only_led.png)

## Task 6: What is the humidity?

Refer to wiring schematic
print humidity

## Task 7: It's getting humid in here

Besides the song "Hot In Herre" by Nelly, it feels like the temperature is getting hotter with the Raspberry Pi, and your brain of yours working to complete the tasks. By using the `read_sensor_temperature()` and `read_sensor_humidity()` we can get the temperature and humidity of the surroundings into our program.

Python supports an "if" statement which allows the programmer to ask questions to the system. A statement like the following asks the program if the temperature in the room is lower than 1-degree Celsius: `if read_sensor_temperature() < 1:`.

Now, have the program turn on the LED if the temperature is higher than value X and turn it off if it is lower than value X. You can choose the value of X as you like.

![wiring schematic](../images/wiring_schematic.png)

## Task Bonus: To the great beyond

make the led blink instead of simply turning it on if humidity is too high

You have reached the finish line! Now ask your guide what to do. For me, the document, I can't continue further. So I guess this is goodbye... Goodbye!
