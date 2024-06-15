# Ahmed O. Roberts | June 13, 2025
# CIS 156 | Python Programming | Level 1
# Module 04 Programming Assignment
# Part A

'''
Wanda's Wall Cleaning offers regularly scheduled wall cleaning and maintenance services for homeowner's. 
Write a program called wall_clean.py to help customers choose a service plan. 
Prompt the user to input the following information:

Wall height
Number of cleaning visits per month
Number of "deep cleaning" visits per year
Based on the input, use branching to recommend appropriate service plan options:

A customer with a wall height of 8 feet or less, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan A at $48 per month.
A customer with a wall height of 8 feet or less, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan B at $58 per month.
A customer with a wall height of more than 8 feet, with less than 4 visits per month and less than 3 deep cleanings per year should choose Plan C at $62 per month.
A customer with a wall height of more than 8 feet, with 4 or more visits per month OR 3 or more deep cleanings per year should choose Plan D at $66 per month.
'''

wall_height = float(input('Please enter wall height in feet: \n'))
monthly_visit = int(input('Please enter number of monthly visits: \n'))
deep_cleaning = int(input('Please enter number of yearly deep cleanings: \n'))
recommended_plan = 'Plan X'

if wall_height <= 8:
  if (monthly_visit < 4) and (deep_cleaning < 3):
    plan = 'A'
    price = 48
    recommended_plan = 'Plan A at $48 per month'
  elif (monthly_visit >= 4) or (deep_cleaning >= 3):
    plan = 'B'
    price = 58
    recommended_plan = 'Plan B at $58 per month.'
else:
  if (monthly_visit < 4) and (deep_cleaning < 3):
    plan = 'C'
    price = 62
    recommended_plan = 'Plan C at $62 per month'
  elif (monthly_visit >= 4) or (deep_cleaning >= 3):
    plan = 'D'
    price = 66
    recommended_plan = 'Plan D at $66 per month.'

# plan = 'Ahmed'
# price = 99
  
print(f'1. Recommended plan is: {recommended_plan}')
print('2. Recommended plan is: Plan {} at ${} per month.'.format(plan, price))