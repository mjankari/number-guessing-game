import random
import sys


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    number = random.randrange(1, 100, 1)
    print(number)


if __name__ == "__main__":
    sys.exit(main())
