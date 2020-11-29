"""FirstName"""
# 001.py
# Ask for users' forename and display it.

# Importing Modules
import time


# Start
# Defining Functions
def primaryname():
    """Return primary name."""
    while True:
        name_1 = input('Please enter your firstname: ')
        if not name_1.isalpha():
            print('Your firstname cannot contain anything other than alphabets.')
        else:
            print('Processing...')
            time.sleep(2)
            print('Hello ' + name_1 + '!')
            break


def main():
    """Driver"""
    primaryname()


# Calling Functions
main()

# End
