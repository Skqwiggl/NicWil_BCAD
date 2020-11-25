"""Addition"""
# 004.py
# Find the sum of the values.


# Start
# Defining Functions
def addition():
    """Finds the sum; c."""
    while True:
        a = input('Please enter a number for the value for a: ')
        if not a.isnumeric():
            print('Your value for a cannot be alphanumeric/blank, please retry.')
        else:
            break

    while True:
        b = input('Now enter a value for b: ')
        if not b.isnumeric():
            print('Your value for b cannot contain anything other than numerals.')
        else:
            a, b = float(a), float(b)
            c = a + b
            print(a, '+', b, '=', c)


def main():
    """Driver"""
    addition()


# Calling Functions
main()

# End
