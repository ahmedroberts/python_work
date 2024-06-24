# Ahmed O. Roberts
# Module 06 - Programming Assignment
# Part B

# This program calculates the fee charged for a shopping trip.

print('\nThis program calculates the fee charged for a shopping trip.\n')

num_items = int(input('Enter number of items: '))
num_stores = int(input('Enter number of stores: '))

def fee_calulator(items, stores):
  fee = 0
  print('So..... items', items, 'stores', stores)
  
  if(items < 3 and stores == 1):
    fee = 5
  elif (items < 3 and stores == 2):
    fee = 7.5
  elif (3 <= items <= 5) and stores < 3:
    fee = 8.5
  else:
    fee = 10
  
  return fee

print(f'${fee_calulator(num_items, num_stores):.2f} fee.\n')