#!/usr/bin/env python3
# Created By: Bryson Grant
# Date: 11 17, 2026
# This program runs a guessing game where the user
# has to guess a number between 0 and 9
# but if you get it wrong it asks you to guess again until you get it right

import random


def main():
    # Generate a random number between 0 and 9
    random_number = random.randint(0, 9)

    # Get the user's guess
    user_guess = input("Guess a number between 0 and 9: ")

    # See if the guess is correct
    while True:
        try:
            user_guess_int = int(user_guess)
            if user_guess_int < 0 or user_guess_int > 9:
                print("{} is outside of the range 0 - 9".format(user_guess))
                user_guess = input("Guess a number between 0 and 9: ")
                # If they guess right
            elif user_guess_int == random_number:
                print("You guessed it! The number was {}".format(random_number))
                break
            # If they guess wrong
            else:
                print("Sorry, that's not it. Try again.")
                user_guess = input("Guess a number between 0 and 9: ")
        except ValueError:
            print("{} is not a valid guess".format(user_guess))
            user_guess = input("Guess a number between 0 and 9: ")


if __name__ == "__main__":
    main()
