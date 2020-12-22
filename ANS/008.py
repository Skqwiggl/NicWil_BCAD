"""Convert £ - €"""

import time


def convertor():
    """Converts currency from one to another."""
    print('£:€')
    time.sleep(2)
    while True:
        value = input('Enter an amount of money\n')
        try:
            value = float(value) or int(value)
            break
        except ValueError:
            print('Your value for your indeterminate cannot be anything other than a number.\n')
            continue

    while True:
        conv = input('What currency do you want to convert from, Euros or Pounds?\n')

        if conv == 'Pounds':
            pound = float(value) * 1.12
            time.sleep(1)
            print('Converting Pounds to Euros...\n')
            time.sleep(2)
            print(value, conv, 'is approximately', pound, 'euros.')
            break
        elif conv:
            euro = float(value) * 0.89
            if conv == 'Euros':
                time.sleep(1)
                print('Converting Euros to Pounds...\n')
                time.sleep(2)
                if conv == 1:
                    print(value, conv, 'is approximately', euro, 'pounds.')
                else:
                    print(value, conv, 'are approximately', euro, 'pounds.')
                    break
        elif conv:
            print('ERR_1: Your value cannot be anything other than Euros or Pounds.\n')
        else:
            print('ERR_2: Please enter Euros or Pounds, nothing else.\n')


convertor()
