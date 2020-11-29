"""Currency Conversions"""
# 010.py
# Convert £ - €.

# Importing Modules
import time


# Defining Functions
def convertor():
    """Converts currency from one to another."""
    print('Conversion: £ - €')
    time.sleep(2)
    while True:
        value = input('Enter an amount you want to convert: ')
        try:
            value = float(value)
            break
        except ValueError:
            print('Your value for your indeterminate cannot be anything other than a number.')
            continue

    while True:
        conv = input('What currency do you want to convert from, Euros or Pounds? ')

        if conv == 'Pounds':
            pound = float(value) * 1.12
            time.sleep(1)
            print('Converting Pounds to Euros...')
            time.sleep(2)
            print(value, conv, 'is approximately', pound, 'euros.')
            break
        else:
            euro = float(value) * 0.89
            if conv == 'Euros':
                time.sleep(1)
                print('Converting Euros to Pounds...')
                time.sleep(2)
                print(value, conv, 'is approximately', euro, 'pounds.')
                break

        if not conv.isalpha():
            print('ERR_1: Your value cannot be anything other than Euros or Pounds.')
        elif conv != 'Euros' or 'Pounds':
            print('ERR_2: Please enter Euros or Pounds, nothing else.')


def main():
    """Driver"""
    convertor()


# Calling Functions
main()

# End
