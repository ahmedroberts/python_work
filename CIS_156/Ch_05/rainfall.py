# Ahmed O. Roberts
# Module 05 - Programming Assignment
# Part B

# This program calculates average rainfall for a week 7 user inputs

'''
Create a program called rainfall.py that calculates the average rainfall for a week.
Use a loop to prompt the user seven times for the daily rainfall amount.
After the seventh number, calculate and display both the 
- total rainfall for the week and 
- the average daily rainfall.
'''

total_rainfall = 0
num_rainfalls = 0

rainfall = float(input(f'Enter rainfall {num_rainfalls + 1}: '))
while num_rainfalls < 7:
  total_rainfall += rainfall
  rainfall = float(input(f'Enter rainfall {num_rainfalls + 1}: '))
  num_rainfalls += 1
  
print(f'Over {num_rainfalls} days:\n')
print(f'Total rainfall for the week:  {total_rainfall}')
print(f'Average rainfall for the week: {total_rainfall / num_rainfalls}')