"""Addition"""
# 004.py
# Find the sum of the values.


# Start
# Defining Functions
def addition():
    """Finds the sum; c."""
    while True:
        a = input('Please enter a value for a: ')
        try:
            if '.' in a:
                a = float(a)
                break
            elif '.' not in a:
                a = int(a)
                break
        except ValueError:
            print('Your value for a cannot be anything but a number, please')

    while True:
        b = input('Please enter a value for b: ')
        try:
            if '.' in b:
                b = float(b)
                break
            elif '.' not in b:
                b = int(b)
                break
        except ValueError:
            print('Your value for b cannot be anything but a number, please')

    c = a + b
    print(a, '+', b, '=', c)


def main():
    """Driver"""
    addition()


# Calling Functions
main()

# End
