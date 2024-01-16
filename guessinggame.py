import random

import math

small = int(input("Enter small integer:"))

larger = int(input("Enter larger integer: "))

x = random.randint(small, larger)
print("\n\tYou've only ", round(math.log(larger - small + 1, 2)),
      " chances to guess the integer!\n")

count = 0

while count < math.log(larger - small + 1, 2):
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations you did it in ", count, " try")

        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(larger - small + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
