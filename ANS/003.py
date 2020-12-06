"""Addition"""
# Find the sum of the values.


def addition():
    """Finds the sum; c."""
    while True:
        a = input("Enter a value for indeterminate \'a\': ")
        try:
            if "." in a:
                a = float(a)
                break
            elif "." not in a:
                a = int(a)
                break
        except ValueError:
            print("Your value for indeterminate \'a\' cannot be anything but a number.")

    while True:
        b = input("Enter a value for indeterminate \'b\': ")
        try:
            if "." in b:
                b = float(b)
                break
            elif "." not in b:
                b = int(b)
                break
        except ValueError:
            print("Your value for indeterminate \'b\' cannot be anything but a number.")

    c = a + b
    print("The total is ", c)


addition()
