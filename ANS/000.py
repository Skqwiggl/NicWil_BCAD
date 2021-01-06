"""Test"""

import re


def input_name():
    """
User inputs their name
    :return:
    """
    while True:
        forename = input('Enter your forename:\n')
        if match := re.fullmatch(r'[A-Za-z \-_]+', forename):
            match.group(0)
            break
        else:
            print('Your name may only contain alphabets.')

    while True:
        surname = input('Enter your surname:\n')
        if match := re.fullmatch(r'[A-Za-z \-_]+', surname):
            match.group(0)
            break
        else:
            print('Your name may only contain alphabets.')

    print(f'Hello, {forename} {surname}!')


input_name()
