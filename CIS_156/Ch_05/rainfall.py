# Ahmed O. Roberts
# Module 05 - Programming Assignment
# Part B

# This program calculates average rainfall for a week 7 user inputs

total_rainfall = 0
num_rainfalls = 1

print('\nEnter the daily rainfall, one day at a time.\nThe Aggregations will be calculated after 7 entries\n')

rainfall = float(input(f'Enter rainfall {num_rainfalls}: '))

while num_rainfalls < 7:
  total_rainfall += rainfall
  rainfall = float(input(f'Enter rainfall {num_rainfalls + 1}: '))
  num_rainfalls += 1
  
total_rainfall += rainfall
print(f'\nOver {num_rainfalls} days this week:')
print(f'Total rainfall for the week:   {total_rainfall}')
print(f'Average rainfall for the week:  {(total_rainfall / num_rainfalls):.2f}\n')