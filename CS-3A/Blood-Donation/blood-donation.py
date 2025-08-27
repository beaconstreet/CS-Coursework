'''
A Python program that manages blood donation information and returns an average.  
This project demonstrates file I/O, dictionaries, and user input handling to track and update donor data.

'''


def main():

    again = 'no' # declare again variable for whether user wants to end program

    while again == 'no':
        
        # Initialize all the variables inside the loop so it clears the list
        # each time
        pints = [] # initialize empty pints list
        total_pints = 0 # initialize total_pints variable
        average_pints = 0 # initialize total_pints variable
        high_pints = 0 # initialize total_pints variable
        low_pints = 0 # initialize total_pints variable

        # Call the functions
        get_pints(pints)
        total_pints = get_total(pints, total_pints)
        average_pints = get_average(total_pints, average_pints)
        high_pints = get_high(pints, high_pints)
        low_pints = get_low(pints, low_pints)
        display_results(average_pints, high_pints, low_pints)

        # Give user the option to loop through the program again
        again = str(input('\nDo you want to end program? (Enter no or yes): '))
        
    

# get_pints function receives user input for pints collected, and returns
# pints list

def get_pints(pints):
    for index in range(7):
        pint_collected = int(input('Enter pints collected: '))
        pints.append(pint_collected)
    return pints


# get_total function receives pints list and adds the list elements,
# returning total_pints

def get_total(pints, total_pints):
    for index in pints:
        total_pints += index
    return total_pints


# get_average function returns an average donation per hour, returning
# average_pints

def get_average(total_pints, average_pints):
    average_pints = total_pints / 7
    return average_pints

# get_high function finds the highest number of pints collected

def get_high(pints, high_pints):
    high_pints = max(pints)
    return high_pints

# get_low function finds the lowest number of pints collected

def get_low(pints, low_pints):
    low_pints = min(pints)
    return low_pints

# display_results function displays values for average_pints, high_pints,
# and low_pints

def display_results(average_pints, high_pints, low_pints):
    print(f'\nThe average number of pints donated is {average_pints:.2f}')
    print(f'The highest pints donated is {high_pints}')
    print(f'The lowest pints donated is {low_pints}')

main()



''' --- SAMPLE RUN -----

Enter pints collected: 43
Enter pints collected: 25
Enter pints collected: 64
Enter pints collected: 35
Enter pints collected: 19
Enter pints collected: 37
Enter pints collected: 46

The average number of pints donated is 38.43
The highest pints donated is 64
The lowest pints donated is 19

Do you want to end program? (Enter no or yes): yes

'''
