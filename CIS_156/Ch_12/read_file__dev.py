# Ahmed O. Roberts
# Module 12 Programming Assignment
# Part A

# This program returns a line from a file given the line number

import os

# Path of file on my system: gettysburg = os.path.join('CIS_156', 'Ch_12', 'address.txt')
# Path of file if ran from same directory: gettysburg = "address.txt"
gettysburg = os.path.join("address.txt")
gettysburg2 = os.path.join('CIS_156', 'Ch_12', 'address.txt')
print('1.', gettysburg, gettysburg2)

# open the file
myfile = open(gettysburg2, 'r')
lines = myfile.readlines()

# Create a dynamic prompt
print()
prompt = f"Please enter a line number (1 - {len(lines)}) or 'q' to quit: "

user_input = input(prompt)

# get input until 'q' and display a line
while user_input != 'q':
  print(lines[int(user_input) - 1])
  user_input = input(prompt)
  
# spacing and close
print()
myfile.close()