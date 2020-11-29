"""Birthday"""
# 007.py
# Ask for users' forename and age, then display their age the following year. 


# Defining Functions
def primaryname():
    """Forename function; returns forename if forename is alphabetic"""
    while True:
        name_1 = input('Please enter your firstname: ')
        if not name_1.isalpha():
            print('Your firstname cannot contain anything other than alphabets.')
        else:
            break


def addage():
    """Adds age from current age."""
    while True:
        askage = input('Please enter your age: ')
        if not askage.isnumeric():
            print('Your age cannot be anything other than a integer.')
        else:
            askage = int(askage)
            newage = askage + 1
            print('You will be', newage, 'next year!')
            break


def main():
    """Driver"""
    primaryname()
    addage()


# Calling Functions
main()

# End
