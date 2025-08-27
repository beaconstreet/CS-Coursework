# Blood Donation

A Python program that manages blood donation information and returns an average.  
This project demonstrates file I/O, dictionaries, and user input handling to track and update donor data.

## Features

- Reads donor information from a text file (or starts fresh if none exists)
- Adds new donors with their blood type and donation details
- Looks up existing donors by name
- Updates and saves donor data persistently in the file

## Example Usage

```
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

```

## Project Structure

blood-donation.py # Main script
donors.txt # Data file storing donor records

## Concepts Demonstrated

- File handling in Python
- Dictionaries for structured storage of records
- User input and validation
- Simple persistent data storage

## Next Steps (Optional Enhancements)

- Input validation for blood types and dates
- Display all donors in a formatted list
- Search donors by blood type
- Track donation history per donor
