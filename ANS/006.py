"""Bill"""
# Calculate the amount of money each individual has to pay.


def bill():
    """Bill for each person."""
    while True:
        input_ = input('Please enter the total price of the bill: ')
        try:
            input_ = float(input_)
            break
        except ValueError:
            print('Your variable cannot be anything than a number.')
            continue

    while True:
        diners = input('How many diners do you have? ')
        if not diners.isnumeric():
            print('Your variable cannot be anything other than an integer.')
        else:
            input_, diners = float(input_), int(diners)
            pay = input_ / diners
            print('Each person has to pay', pay)
            break


bill()
