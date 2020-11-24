"""Gummy Bear Joke"""
# 003.py
# Return "No, it's a GUMMY BEAR!" if joke incorrect, if joke == True return "Congratulations, you guessed it!".

# Importing Modules
import time


# Start
# Defining Functions
def jokes():
    """Gummy Bear Joke"""
    print("Before answering this question, the initials of the 2 words must be capital, otherwise it will return false.")
    time.sleep(5)
    answer = "Gummy Bear"
    joke = input("What do you call a bear with no teeth? ")
    if joke == answer:
        print("Congratulations, you guess it!")
    else:
        print("No, it's a GUMMY BEAR!")


def main():
    """Driver"""
    jokes()


main()

# End
