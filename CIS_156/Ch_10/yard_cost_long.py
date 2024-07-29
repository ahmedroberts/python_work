# Ahmed Roberts
# Module 10 Programming Assignment
# Part A

# This program calculates profit from yard landscaping

try:
  lawn_length = float(input('\nEnter length in yards: '))
  lawn_width = float(input('Enter width of lawn: '))
  fertilizer_cost = float(input('Enter cost of fertilizer ($): '))
  
  if (lawn_length < 0):
    raise ValueError('Lawn length must be a positve value')
  if (lawn_width < 0):
    raise ValueError('Lawn width must be a positve value')
  if (fertilizer_cost < 0):
    raise ValueError('Lawn length must be a positve value')
  
except ValueError as excpt:
  print(f'Error: {excpt}')

  lawn_area = lawn_length * lawn_width
  cost_per_sq_yd = fertilizer_cost / lawn_area
  
  print(f'Area of the lawn: {lawn_area} square yards.')
  print(f'Cost per square yard: ${cost_per_sq_yd:.2f} per square yard.\n')

except ZeroDivisionError:
  print('No values should equal zero.')
except:
  print('Sorry that did not work.\n\t-Raikage\n')