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
$ python blood-donation.py
Enter donor name: Alice
Enter blood type: O+
Enter donation date (YYYY-MM-DD): 2025-08-27
Donor record saved.
```

## Resulting file (dictionary.txt)

```
Alice: O+, 2025-08-27
```

## Project Structure

blood-donation.py # Main script
donors.txt # Data file storing donor records

## Concepts Demonstrated

• File handling in Python
• Dictionaries for structured storage of records
• User input and validation
• Simple persistent data storage

## Next Steps (Optional Enhancements)

• Input validation for blood types and dates
• Display all donors in a formatted list
• Search donors by blood type
• Track donation history per donor
