"""Ask for the users' name then display it."""

import time


def forename():
    """Return primary name."""
    while True:
        fornam = input("Enter your forename: ")
        if not fornam.isalpha():
            print("Your firstname cannot contain anything other than alphabets.")
        else:
            print("Processing...")
            time.sleep(2)
            print("Hello " + fornam + "!")
            break


forename()
