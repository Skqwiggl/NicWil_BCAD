"""Wholename"""
# 002.py
# User enters name, returns name if script satisfied.

# Importing Modules
import time


# Start
# Defining Functions
def wholename():
    """Returns name when function is satisfied."""
    while True:
        name_1 = input("Please enter your firstname: ")
        if not name_1.isalpha():
            print("Your firstname cannot be alphanumeric/blank, please retry.")
        else:
            print("Processing...")
            time.sleep(2)
            break

    while True:
        name_2 = input("Now enter your surname: ")
        if not name_2.isalpha():
            print("Your surname cannot be alphanumeric/blank, please try again!")
        else:
            print("Initialising...")
            time.sleep(2)
            print("Hello " + name_1 + " " + name_2 + "!")
            break


def main():
    """Driver"""
    wholename()


# Calling Functions
main()

# End
