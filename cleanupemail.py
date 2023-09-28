import re
import csv

# Read the input text file
with open('input.txt', 'r') as file:
    data = file.read()

# Expression to find email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', data)

# Write the emails to a CSV file
with open('emails.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([[email] for email in emails])
  
