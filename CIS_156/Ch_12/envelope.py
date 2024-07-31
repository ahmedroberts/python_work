# Ahmed O. Roberts
# Module 12 Programming Assignment
# Part B

# This program creates an envelope-like formatted text file 'envelope.txt'

import os

# Path of file on my system: envelope = os.path.join('CIS_156', 'Ch_12', 'envelope.txt')
# Path of file if ran from same directory: envelope = "envelope.txt"
envelope = os.path.join("envelope.txt")

# This function creates and formats envelope.txt
def create_envelope():
  # open the file in read mode
  envelope_file = open(envelope, 'w')
  spacer = '\n\n'
  spacer1 = ' '* 10

  envelope_file.write(f'{recipient.name}\n')
  envelope_file.write(f'{recipient.address}\n')
  envelope_file.write(f'{recipient.city}, {recipient.state}, {recipient.zip}\n')
  envelope_file.write(spacer)
  envelope_file.write(f'{spacer1}{sender.name}\n')
  envelope_file.write(f'{spacer1}{sender.address}\n')
  envelope_file.write(f'{spacer1}{sender.city}, {sender.state}, {sender.zip}\n')
  envelope_file.close()

# Create Mailing Information class
class Mailing_info:
  def __init__(self):
    self.name = ''
    self.address = ''
    self.city = ''
    self.state = ''
    self.zip = ''

# Create and populate sender instance of Mailing_info
sender = Mailing_info()
sender.name = 'Ahmed O. Roberts'
sender.address = '2814 Earth Way'
sender.city = 'Wakanda'
sender.state = 'AZ'
sender.zip = '90210'

# Create and populate recipient instance of Mailing_info
recipient = Mailing_info()

# Create a dynamic prompt
print()
prompt1 = f"Please enter the following recipient info: "
print(prompt1)
recipient.name    = input('name: ')
recipient.address = input('address: ')
recipient.city    = input('city: ')
recipient.state   = input('state: ')
recipient.zip     = input('zip: ')

# Call create_evelope
create_envelope()
print("\nThank you. Envelope created.\n")