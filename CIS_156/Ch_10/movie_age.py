# Ahmed Roberts
# Module 10 Programming Assignment
# Part b

# This program calculates price of movie based on age

def get_price(customer_age):
  if customer_age < 3:
    admission_price = 0
  elif 3 <= customer_age <= 10:
    admission_price = 5
  elif 11 <= customer_age <= 14:
    admission_price = 6
  elif 15 <= customer_age <= 18:
    admission_price = 8
  elif 19 <= customer_age <= 50:
    admission_price = 10
  else:
    admission_price = 8
  return admission_price

try:
  try:
    current_age = int(input("\nEnter customer's age: "))
  except ValueError:
    raise ValueError('Please enter a valid age.')
  else:
    if current_age < 0:
      raise ValueError('Please enter a positve age.')
    
    admission_price = get_price(current_age)
    print(f'\nYour admission is ${admission_price:.2f} today.\n')
    
except ValueError as excpt1:
  print(f'Error: {excpt1}')
  
  