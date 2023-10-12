# Import Statements.
import random

def main():
    """
    This is the main function.
    """
    # Dictionary
    counties = {'Atascosa': 'Jourdanton', 'Bandera': 'Bandera', 'Bastrop': 'Bastrop',
              'Bexar': 'San Antonio', 'Caldwell': 'Lockhart', 'Comal': 'New Braunfels',
              'Guadalupe': 'Seguin', 'Hays': 'San Marcos', 'Kendall': 'Boerne',
              'Medina': 'Hondo', 'Travis': 'Austin', 'Williamson': 'Georgetown',
              'Wilson': 'Floresville'}
    # Local variables.
    correct = 0
    wrong = 0
    next_question = True
    index = 0
    user_input = ''

    while next_question:

        # Access the list of counties.
        county = iter(counties)

        # Get a random county name using random.
        index = random.randint(1, len(counties)) - 1
        for _ in range (index - 1):
            county_next = county.__next__()
        county_curr = str(county_next)
        # Get user answer.
        user_input = input(f'\nWhat is the county seat of {county_curr}\
 County? (Enter 0 to quit): ')
        # If the user wants to quit the game.
        if user_input == '0':
            next_question = False
            print(f'\nYou had {correct} correct {plurals(correct)} and '
                  f'{wrong} incorrect {plurals(wrong)}.\n')
        # If the answer is correct
        elif user_input == counties[county_curr]:
            correct += 1
            print('That is correct')
        # If the answer is incorrect
        else:
            wrong += 1
            print('That is incorrect.')

def plurals(count):
    """
    This function will return a response if there are less than two
    else responses.
    """
    if count <2:
        return 'response'
    else:
        return 'responses'

# Call the main function.
if __name__ == '__main__':
    main()
