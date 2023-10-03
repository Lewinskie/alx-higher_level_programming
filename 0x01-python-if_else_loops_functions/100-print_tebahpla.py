#!/usr/bin/python3
for letter in range(ord('z'), ord('a') -1, -1):
    print("{:c}".format(letter if ord('z') - letter % 4 == 0 else letter - 32), end="")
