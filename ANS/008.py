"""£ : €"""

from time import sleep
from random import uniform
from tqdm import tqdm
from forex_python.converter import CurrencyRates

c = CurrencyRates()


def convertor():
    """Converts currency from one to another."""
    print('£ : €')
    sleep(1)
    value = ''

    while type(value) != float and type(value) != int:
        value = input('Enter an amount of money:\n')
        try:
            if '.' in value:
                value = float(value)
            else:
                value = int(value)
        except ValueError:
            print('Your entrance for a cannot be anything but a number.')

    conv = ''

    while conv.lower() != 'euros' and conv.lower() != 'pounds':
        sleep(.2)
        conv = input('What currency do you want to convert from, Euros or Pounds?\n')
        if conv.lower() != 'euros' and conv.lower() != 'pounds':
            print('You may only enter Euros or Pounds')

    if conv.lower() == 'pounds':
        pound = c.convert('GBP', 'EUR', value)
        for _ in tqdm(range(100), desc='Converting Pounds to Euros'):
            sleep(uniform(0.004, 0.01))
        sleep(.2)
        if conv == 1:
            print(f'£{value} is approximately €{pound}')
        else:
            print(f'£{value} are approximately €{pound}')

    else:
        euro = c.convert('EUR', 'GBP', value)
        for _ in tqdm(range(100), desc='Converting Euros to Pounds'):
            sleep(uniform(0.004, 0.01))
        sleep(.2)
        if conv == 1:
            print(f'€{value} is approximately £{euro}.')
        else:
            print(f'€{value} are approximately £{euro}.')


convertor()
