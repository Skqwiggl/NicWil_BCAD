"""Addition"""
# User enters 2 numbers, find sum & display.


def addition():
    """Finds the sum; c."""
    while True:
        a = input("Please enter a number for the value for a: ")
        if not a.isnumeric():
            print("Your value for a cannot be alphanumeric/blank, please retry.")
        else:
            break

    while True:
        b = input("Now enter a value for b: ")
        if not b.isnumeric():
            print("Your value for b cannot be alphanumeric/blank, please re-enter.")
        else:
            break

    while True:
        c = input("Enter a value for c: ")
        if not c.isnumeric():
            print("Your value for c cannot be alphanumeric/blank, please try again.")
        else:
            d = float(a) + float(b)
            e = float(d) * float(c)
            print("The product of the sum", d, "*", c, "=", e)
            break


def main():
    """Driver"""
    addition()


main()
