# Building Manager Tracker

A simple Python project that demonstrates working with **files, dictionaries, and object-oriented programming**.  
This program allows users to store, retrieve, and update key–value pairs (e.g., names and building numbers) in a text file.

## Features

- Reads a dictionary of key–value pairs from a text file
- Safely handles missing files by returning an empty dictionary
- Adds or updates entries via user input
- Looks up values by key and prints results
- Saves the updated dictionary back to the file

## Example Usage

```
$ python building-manager-tracker.py
Enter new name: Alice
Enter new building number: 101
Enter name to look up: Alice
101
```

## Resulting file (dictionary.txt)

Alice: 101

## Project Structure

building_manager_tracker.py # Main script
dictionary.txt # Data file storing manager–building assignments

## Concepts Demonstrated

    •	File input/output in Python
    •	Error handling (FileNotFoundError)
    •	Dictionaries for storing and updating key–value pairs
    •	Classes and methods for code organization
    •	User input and simple data persistence

## Next Steps (Optional Enhancements)

    •	Validate building numbers to ensure numeric input
    •	Use with open(...) for safer file handling
    •	Add unit tests for the DictionaryFileManager class
    •	Expand functionality (e.g., remove entries, list all managers)
