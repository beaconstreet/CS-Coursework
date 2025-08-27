'''

A simple Python project that demonstrates working with **files, dictionaries, and object-oriented programming**.  
This program allows users to store, retrieve, and update key–value pairs (e.g., names and building numbers) in a text file.

'''



class DictionaryFileManager:
    '''
    This class reads and writes a dictionary from and to a file.
    The constructor takes a dictionary filename and stores it for reference for
    use by the object methods
    '''


    def __init__(self, dict_txt_file):
        self.filename = dict_txt_file

    def read_dictionary_from_file(self):
        '''
        Reads key/value pairs as strings, converts to a dictionary format.
        If the file does not exist, it returns an empty dictionary
        '''
        # create new dictionary
        new_dictionary = {}

        # try/except to make sure file exists, otherwise return empty dictionary
        try:
            # open file
            read_file = open(self.filename, 'r')
        except FileNotFoundError:
            # return empty dictionary if file doesn't exist
            return new_dictionary

        # Return a new dictionary based on the file's content
        print(f'accessing {self.filename} through object')
        for line in read_file:
            key_value_pair = line.strip().split(': ')
            key = key_value_pair[0]
            value = int(key_value_pair[1])
            new_dictionary[key] = value

        # close file
        read_file.close()

        # return dictionary
        return new_dictionary


    def write_dictionary_to_file(self, dictionary):
        '''
        Takes a dictionary parameter and writes its key/value pairs to the file.
        Each pair is writte on a new line in the format key: value
        
        '''
        # Open file and write mode 
        write_file = open(self.filename, 'w')
            
        # Take the dictionary it is given and output it to a file
        for key, value in dictionary.items():
            write_file.write(f'{key}: {value}\n')
        
        # close file
        write_file.close()


def main():

    # Initialize instance with dictionary filename
    manager = DictionaryFileManager('dictionary.txt')

    # Call object instance read_dictionary_from_file
    building_numbers = manager.read_dictionary_from_file() 
    
    # User input a name they'd like to add (string)
    manager_name = str(input('Enter new name: '))
    
    # If user enters empty string, program skips building number
    if manager_name != '':
        
        # User input a building number (integer)
        build_number = int(input('Enter new building number: '))

        # Update dictionary
        building_numbers[manager_name] = build_number
    
    
    # Puts key (name) and value (building number) into a dictionary
    # Ask user for a name they'd like to look up (string)
    manager_lookup = str(input('Enter name to look up: '))

    # If user name input matches key in dictionary, print matching
    # building number.  Else print nothing
    if manager_lookup in building_numbers:
        print(building_numbers[manager_lookup])

    # Save updated dictionary
    manager.write_dictionary_to_file(building_numbers)
    
    

main()
