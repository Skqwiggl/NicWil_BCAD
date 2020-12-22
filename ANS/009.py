"""Smaller First"""
# Display numbers in terms of value.

import time


def inequality():
    """Displays the smaller number first."""
    while True:
        a = input('Enter a value for indeterminate \'a\': ')
        time.sleep(1)
        print('Initialising...')
        time.sleep(1)
        try:
            if '.' in a:
                a = float(a)
                break
            elif '.' not in a:
                a = int(a)
                break
        except ValueError:
            print('Your value for indeterminate \'a\' cannot be anything but a number.')

    while True:
        b = input('Enter a value for indeterminate \'b\': ')
        time.sleep(1)
        try:
            if '.' in b:
                b = float(b)
                break
            elif '.' not in b:
                b = int(b)
                break
        except ValueError:
            print('Your value for indeterminate \'b\' cannot be anything but a number.')
        
        time.sleep(2)
        
    if a < b:
        print(a, '<', b)
    elif a == b:
        print(a, '=', b)
    else:
        print(b, '<', a)


inequality()
