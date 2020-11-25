"""Wholename"""
# 002.py
# Return whole name of user.

# Importing Modules
import time


# Start
# Defining Functions
def wholename():
    """Returns name when function is satisfied."""
    while True:
        name_1 = input('Please enter your firstname: ')
        if not name_1.isalpha():
            print('Your forename cannot contain anything other than alphabets..')
        else:
            print('Processing...')
            time.sleep(2)
            break

    while True:
        name_2 = input('Now enter your surname: ')
        if not name_2.isalpha():
            print('Your surname cannot contain anything other than alphabets.')
        else:
            print('Initialising...')
            time.sleep(2)
            print('Hello ' + name_1 + ' ' + name_2 + '!')
            break


def main():
    """Driver"""
    wholename()


# Calling Functions
main()

# End
