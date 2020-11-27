"""Smaller First"""
# 012.py
# Display numbers in terms of value.


# Start
# Defining Functions
def inequality():
    """Displays the smaller number first."""
    while True:
        a = input('Enter a value for indeterminate \'a\': ')
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
        try:
            if '.' in b:
                b = float(b)
                break
            elif '.' not in b:
                b = int(b)
                break
        except ValueError:
            print('Your value for indeterminate \'b\' cannot be anything but a number.')

    if a < b:
        print(a, b)
    elif a == b:
        print("False")
    else:
        print(b, a)


def main():
    """Driver"""
    inequality()


# Calling Functions
main()
