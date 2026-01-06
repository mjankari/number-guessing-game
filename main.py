import random
import sys


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 5 chances to guess the correct number.")

    number = random.randrange(1, 100, 1)
    print(number)

    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    difficulty_level = 0

    try:
        difficulty_level = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid integer.")

    chances = 10

    match difficulty_level:
        case 1:
            chances = 10
            print("Great! You have selected the Easy difficulty level.")
        case 2:
            chances = 5
            print("Great! You have selected the Medium difficulty level.")
        case 3:
            chances = 3
            print("Great! You have selected the Hard difficulty level.")
        case _:
            print("something went wrong")


if __name__ == "__main__":
    sys.exit(main())
