# Ahmed O. Roberts | June 13, 2025
# CIS 156 | Python Programming | Level 1
# Module 04 Programming Assignment
# Part B

# This program calculates weekly pay for an individual employee at Larry's Landscaping.

# Prompt User and collect data
print('\nPlease enter job title code. ')
job_title = input('("T" for tree trimmer, "L" for lawncare specialist, "C" for general cleanup): \n')
hours_worked = float(input('Please enter number of hours worked this week: \n'))
years = float(input('Please enter number of years employed: \n'))

# Check if job title is tree trimmer
if (job_title == 'T'):
  # Calculate hourly rate based on number of years
  hourly_pay = 15 if (years <= 1) else 16
# Check if job title is lawn care specialist
elif (job_title == 'L'):
  # Calculate hourly rate based on number of years
  hourly_pay = 13 if (years <= 2) else 14.5
# Check if job title is general cleanup
elif (job_title == 'C'):
  # Calculate hourly rate based on number of years
  hourly_pay = 14 if (years <= 1) else 15
# Warn user of invalid input
else:
  message = r'You did not select "T", "L", or "C"'

# Calculate gross pay for the week
gross_pay_weekly = hours_worked * hourly_pay
# Display final gross pay message
print(f'\nGross pay is ${gross_pay_weekly:.2f} this week.\n')