"""Addition"""
# 004.py
# Find the sum of the values.


# Start
# Defining Functions
def addition():
    """Finds the sum of a + b."""
    while True:
        a = input('Please enter a value for a: ')
        if '.' in a:
            a = float(a)
            break
        elif not a.isnumeric():
            print('Your value for a cannot be anything but a number, please retry.')
        else:
            a = int(a)
            break

    while True:
        b = input('Please enter a value for b: ')
        if '.' in b:
            b = float(b)
            break
        elif not b.isnumeric():
            print('Your value for b cannot be anything but a number, please try again.')
        else:
            b = int(b)
            break

    c = a + b
    print(a, '+', b, '=', c)


def main():
    """Driver"""
    addition()


# Calling Functions
main()

# End
