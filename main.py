import random
import sys


def main():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number = random.randint(1, 100)

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
            print("You have 10 chances to guess the correct number.")
        case 2:
            chances = 5
            print("Great! You have selected the Medium difficulty level.")
            print("You have 5 chances to guess the correct number.")
        case 3:
            chances = 3
            print("Great! You have selected the Hard difficulty level.")
            print("You have 3 chances to guess the correct number.")
        case _:
            print("something went wrong")

    attempts = 0

    while True:
        attempts += 1

        if attempts > chances:
            print("Condolences. You did not guess the correct number.")
            break

        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter a valid integer")

        if user_guess < number:
            print(f"Incorrect! The number is greater than {user_guess}.")
        elif user_guess > number:
            print(f"Incorrect! The number is less than {user_guess}.")
        else:
            print(
                f"Congratulations! You guessed the correct number in {attempts} attempts."
            )
            break


if __name__ == "__main__":
    sys.exit(main())
