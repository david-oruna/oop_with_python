#!/usr/bin/env python

# 05-init_constructor-2.py

# We add a test in the __init__() constructor to check
# if 'value' is an int or not.

#david-oruna: I changed and added some input functions, so it is more customizable :)


class MyNum:
    def __init__(self, value, message, favorite):
        try:
            value = int(value)
            print(f'Message is {message}')
            print(f'Is favorite: {favorite}')
        except ValueError:
            value = 0
        self.value = value
        self.message = message
        self.favorite = favorite

    def increment(self):
        try:
            addnum = int(input('Enter number to add: '))
            self.value = self.value + addnum
            print(f'Your new number is {self.value}')
        except ValueError as e:
            print(f'Value error: {e}')


a = MyNum(8, 'Hello', True)

a.increment()  # Prints your num + input
a.increment()  # Prints again your num + input
