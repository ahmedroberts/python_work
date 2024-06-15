# Ahmed O. Roberts | June 13, 2025
# CIS 156 | Python Programming | Level 1
# Module 04 Programming Assignment
# Part B

'''
Larry's Landscaping pays employees differently depending on their job title and experience. 
In a program called landscape_pay.py, use separate prompts to collect the following input:

Job title ("T" for tree trimmer, "L" for lawncare specialist, "C" for general cleanup)
Number of hours worked
Number of years employed at the restaurant
Then, output their gross pay amount (i.e., the amount they earn before taxes and other deductions) for one week based on the following:

Tree trimmers earn $15/hour until they've worked 1 year, then earn $16/hour
Lawncare specialists earn $13/hour for the first 2 years, then go up to $14.50/hour
General cleanup employees make $14/hour for the first year, then go to $15/hour
'''

print('\nPlease enter job title: ')
job_title = input('("T" for tree trimmer, "L" for lawncare specialist, "C" for general cleanup): \n')
hours_worked = float(input('\nPlease enter number of hours worked this week: \n'))
years = float(input('\nPlease enter number of years employed: \n'))

if (job_title == 'T'):
  message = 'tree trimmer'
  hourly_pay = 15 if (years <= 1) else 16
elif (job_title == 'L'):
  message = 'lawn care specialist'
  hourly_pay = 13 if (years <= 2) else 14.5
elif (job_title == 'C'):
  message = 'general cleanup'
  hourly_pay = 14 if (years <= 1) else 15
else:
  message = r'You did not select "T", "L", or "C"'

gross_pay_weekly = hours_worked * hourly_pay
print(f'\n --- {message} ---')
print(f'\nGross pay is ${gross_pay_weekly:.2f} this week.\n')