import math
import random

# Guess Game#
from time import sleep

print("*="*38)
print("I am going to think in a number between 0 and 5, try to guess!")
print("*="*38)
guess = int(input("What is your guess?"))
print("Processing....")
sleep(2)
computer = random.randint(0, 5)
if guess == computer:
    print("Good guess I thought in number {}!".format(guess))
else:
    print("Try again!This time I thought number {}!".format(computer))
