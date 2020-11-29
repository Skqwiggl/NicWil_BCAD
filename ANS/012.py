"""Intervals"""
# 012.py
# Enter a number 10 <= x <= 20


# Start
# Defining Functions
def intervals():
    """Intervals between two integers."""
    while True:
        a = input('Enter a value for indeterminate \'a\' which cannot be less than 10 or more than 20: ')
        try:
            if '.' in a:
                a = float(a)
                break
            elif '.' not in a:
                a = int(a)
                break
        except ValueError:
            print('Your value for indeterminate \'a\' cannot be anything but a number.')

    if 10 <= a <= 20:
        print('Thank you.')
    else:
        print('Incorrect answer.')


def main():
    """Driver"""
    intervals()


# Calling Functions
main()

# End
