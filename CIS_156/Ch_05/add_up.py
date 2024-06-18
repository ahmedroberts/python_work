# Ahmed O. Roberts
# Module 05 - Programming Assignment
# Part A

# This program adds up a series of numbers

sum = 0
print('\nEnter the numbers to add, one at a time.\nEnter zero (\"0\") when finished.\n')
num = int(input('Enter a number: '))

while num != 0:
  sum += num
  num = int(input('Enter a number: '))

print(f'\nThe sum of numbers you input is {sum}\n')