# Ahmed O. Roberts | June 13, 2025
# CIS 156 | Python Programming | Level 1
# Module 04 Programming Assignment
# Part A

# This program recommends appropriate service plan options from Wanda's Wall Cleaning.

wall_height = float(input('\nPlease enter wall height in feet: \n'))
monthly_visit = int(input('Please enter number of monthly visits: \n'))
deep_cleaning = int(input('Please enter number of yearly deep cleanings: \n'))

# Check if wall height is greater than on equal to 8
if wall_height <= 8:
  # Check monthly visits less tnan 4
  # - and deep cleaning is less than 3
  if (monthly_visit < 4) and (deep_cleaning < 3):
    plan = 'A'
    price = 48
  # all others
  elif (monthly_visit >= 4) or (deep_cleaning >= 3):
    plan = 'B'
    price = 58
# If wall height is less than 8
else:
  # Check monthly visits less tnan 4
  # - and deep cleaning is less than 3
  if (monthly_visit < 4) and (deep_cleaning < 3):
    plan = 'C'
    price = 62
  # all others
  elif (monthly_visit >= 4) or (deep_cleaning >= 3):
    plan = 'D'
    price = 66

# Display recommendation
print('\nWe recommend Plan {} at ${} per month.\n'.format(plan, price))