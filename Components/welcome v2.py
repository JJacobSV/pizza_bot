import random
from random import randint

# List of random names
names = ["Alice", "Patrica", "Jeremy", "Micky", "Dees", "Lisa", "Veronica", "Mike", "Ox", "Slong"]
def welcome():
    '''
    Purpose: to generate a random name from the list and print out a welcome message
    Parameters: none
    Returns: none
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welome to Dream Pizza ***")
    print("*** My name is", name, "***")
    print("*** I will be here to help you order our delicious Dream Pizza ***")


def main():
    '''
    Purpose: to run all functions
    Parameters: none
    Returns: none
    '''
    welcome()

main()