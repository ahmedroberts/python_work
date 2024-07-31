# Ahmed O. Roberts
# Module 12 Programming Assignment
# Part B

# This program creates an envelope-like formatted text file 'envelope.txt'

import os

# Path of file on my system: envelope = os.path.join('CIS_156', 'Ch_12', 'envelope.txt')
# Path of file if ran from same directory: envelope2 = "envelope.txt"
envelope = os.path.join('CIS_156', 'Ch_12', 'envelope.txt')
envelope2 = "envelope.txt"

# This function creates and formats envelope.txt
def create_envelope():
  # open the file in read mode
  envelope_file = open(envelope, 'w')
  spacer = '\n\n'
  spacer1 = ' '* 10

  envelope_file.write(f'{recipient.name}\n')
  envelope_file.write(f'{recipient.address}\n')
  envelope_file.write(f'{recipient.city},  {recipient.state}, {recipient.zip}\n')
  envelope_file.write(spacer)
  envelope_file.write(f'{spacer1}{sender.name}\n')
  envelope_file.write(f'{spacer1}{sender.address}\n')
  envelope_file.write(f'{spacer1}{sender.city},  {sender.state}, {sender.zip}\n')
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
sender.city = 'Metropolis'
sender.state = 'Wakanda'
sender.zip = '85340-9999'

# Create and populate recipient instance of Mailing_info
recipient = Mailing_info()
recipient.name = 'Ahmed O. Roberts'
recipient.address = '2814 Earth Way'
recipient.city = 'Metropolis'
recipient.state = 'Wakanda'
recipient.zip = '85340-9999'


# Create a dynamic prompt
print()
prompt1 = f"Please enter recipient's info: "
print(prompt1)

create_envelope()
print("\nThank you. Envelope created.\n")