"""Find the sum of the 2 numbers."""


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

    while True:
        c = input('Please enter a value for c: ')
        try:
            if '.' in c:
                c = float(c)
                break
            elif '.' not in c:
                c = int(c)
                break
        except ValueError:
            print('Your value for c cannot be anything but a number, please')

    d = a + b
    e = d * c
    print('The answer is, ', e)


addition()
