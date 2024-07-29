# Ahmed Roberts
# Module 10 Programming Assignment
# Part A

# This program calculates profit from yard landscaping

try:
  lawn_length = int(input('\nEnter length in yards: '))
  lawn_width = int(input('Enter width of lawn: '))
  fertilizer_cost = int(input('Enter cost of fertilizer ($): '))

  lawn_area = lawn_length * lawn_width
  cost_per_sq_yd = fertilizer_cost / lawn_area

  print(f'\nArea of the lawn: {lawn_area} square yards.')
  print(f'Cost per square yard: ${cost_per_sq_yd:.2f} per square yard.\n')
except:
  print('Sorry that did not work.\n\t-Raikage\n')