"""Ask for the answer to the joke"""


def jokes():
    """Ask user for the answer of a joke."""
    while True:
        que = input('What do you call a bear with no teeth? ')
        ans = 'gummy bear'
        if que == ans:
            print('Congrats, you\'ve gotten it!')
            break
        elif que != ans and que.isalpha():
            print('Nope, it\'s a gummy bear.')
            break
        else:
            print('Your entrance must only contain alphabets.')


jokes()
