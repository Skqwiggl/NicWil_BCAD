"""Addition"""
# 004.py
# User enters 2 numbers, find sum & display.


# Start
# Defining Functions
def addition():
    """Finds the sum; c."""
    a = input("Please enter a number for the value for a: ")
    if not a.isnumeric():
        print("Your value for a cannot be alphanumeric/blank, please retry.")
    else:
        pass

    b = input("Now enter a value for b: ")
    if not b.isnumeric():
        print("Your value for b cannot be alphanumeric/blank, please re-enter.")
    else:
        a, b = float(a), float(b)
        c = a + b
        print(a, "+", b, "=", c)


def main():
    """Driver"""
    addition()


# Calling Functions
main()

# End
