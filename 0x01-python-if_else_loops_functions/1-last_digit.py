#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_last = abs(number) % 10

if 0 > number:
    last_last *= -1
    print(f"Last digit of {number} is {last_last} ")
    if 5 < last_last:
        print(f"and is greater than 5")
    elif last_last == 0:
        print(f"and is 0")
    else:
        print(f"and is less than 6 and not 0")

