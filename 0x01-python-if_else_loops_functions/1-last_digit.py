#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_last = abs(number) % 10

if 0 > number:
    last_last *= -1
    print("Last digit of {} is {}".format(number, last_last), end=" ")
    if last_last > 5:
        print("and is greater than {}".format(last_last))
    elif last_last == 0:
        print("and is {}".format(last_last))
    else:
        print("and is less than 6 and not 0")
