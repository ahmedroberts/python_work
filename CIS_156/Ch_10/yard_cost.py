# Ahmed Roberts
# Module 10 Programming Assignment
# Part A

# This program calculates profit from yard landscaping based on dimensions

try:
  lawn_length = float(input('\nEnter length in yards: '))
  lawn_width = float(input('Enter width of lawn: '))
  fertilizer_cost = float(input('Enter cost of fertilizer ($): '))

  lawn_area = lawn_length * lawn_width
  cost_per_sq_yd = fertilizer_cost / lawn_area

  print(f'\nArea of the lawn: {lawn_area} square yards.')
  print(f'Cost per square yard: ${cost_per_sq_yd:.2f} per square yard.\n')
except ValueError:
  print('\nPlease only enter numbers.\n')
except ZeroDivisionError:
  print('Lawn length nor width can equal zero.\n')
except:
  print('Sorry that did not work.\n\t-MGMT\n')