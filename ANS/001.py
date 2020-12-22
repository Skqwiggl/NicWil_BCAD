"""Ask for the user's fullname and display it."""

import time


def wholename():
    """Returns name when function is satisfied."""
    while True:
        fornam = input('Enter your forename: ')
        if not fornam.isalpha():
            print('Your forename cannot contain anything other than alphabets.')
        else:
            print('Processing...')
            time.sleep(2)
            break

    while True:
        surnam = input('Enter your surname: ')
        if not surnam.isalpha():
            print('Your surname cannot contain anything other than alphabets.')
        else:
            print('Initialising...')
            time.sleep(2)
            print('Hello ' + fornam + ' ' + surnam + '!')
            break


wholename()
