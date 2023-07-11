#!/usr/bin/python3
for digit_one in range(0, 8):
    for digit_two in range(1, 10):
        if digit_one < digit_two:
            print(f"{digit_one}{digit_two}", end = ", ")
print("{}{}" .format(digit_one + 1, digit_two))
