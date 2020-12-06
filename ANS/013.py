"""Favourite Colour"""
# Ask the user for their favourite colour then display BooLean.


def colour():
    """Ask user for fav col"""
    while True:
        favcol = input("Enter your favourite colour\n")
        if favcol == "red":
            print("I like red too")
            break
        elif favcol != "red":
            print(f"I don't like {favcol}, I like red.")
            break
        else:
            print("You can only input strings that are pure alphabets.")


colour()
