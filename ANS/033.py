"""Float Quotient"""
# Find the whole and remainder quotient.


def floatdiv():
    """Divide 2 float digits"""
    while True:
        num_1 = input('Please enter a number: ')
        if '.' in num_1:
            float(num_1)
            break
        elif not num_1.isnumeric():
            print('Your variable entered cannot be anything other than a number.')
        else:
            int(num_1)
            break

    while True:
        num_2 = input('Now enter a second number: ')
        if '.' in num_2:
            print('Your whole quotient is:', float(num_1) // float(num_2), 'and your remainder quotient is:',
                  float(num_1) % float(num_2))
            break
        elif not num_2.isnumeric():
            print('Number 2 cannot be anything other than a number.')
        else:
            print('Your whole quotient is:', int(num_1) // int(num_2), 'and your remainder quotient is:', int(num_1) %
                  int(num_2))
            break


floatdiv()
