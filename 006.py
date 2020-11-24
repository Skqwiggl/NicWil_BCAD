"""Remainder of sweets"""
# Calculates the remaining amount of sweets.


def remainder():
    """Calculates the remaining amount of sweets."""
    while True:
        starter = input("How many sweets do you have now? ")
        if not starter.isnumeric():
            print("Your value cannot be a alphanumeric/blank, please enter again.")
        else:
            break

    while True:
        consumed = input("How many sweets have you eaten? ")
        if not consumed.isnumeric():
            print("Your variable cannot be alphanumeric/blank, please retry.")
        else:
            starter, consumed = int(starter), int(consumed)
            final = starter - consumed
            print(starter, "-", consumed, "=", final)
            print("You have", final, "sweets.")
            break


def main():
    """Driver"""
    remainder()


main()
