"""Datetime Conversion"""
# 009.py
# Convert number of days to hours, minutes, and seconds.

# Importing Modules
import time


# Start
# Defining Functions
def conversion():
    """Converts days to alternative time measurement units."""
    while True:
        days = input("Please enter an amount of days: ")
        if not days.isnumeric():
            print("The amount of days you entered cannot be anything other than an integer.")
        else:
            time.sleep(1)
            print("Converting...")
            time.sleep(2)
            hours = int(days) * 24
            minutes = int(days) * 1440
            seconds = int(days) * 86400
            print(days, "days has", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")
            break


def main():
    """Driver"""
    conversion()


# Calling Functions
main()

# End
