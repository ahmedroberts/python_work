# Ahmed Roberts The 9th Raikage 
# June 2024 - Estrella Mountain CC
# CIS156 Python Progamming - Level 1

code_break = '#-----------------------------------------------------------------------'
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Branch
bonus_val = 11

if bonus_val != 12:
   bonus_val = bonus_val + 1
else:
   bonus_val = bonus_val + 10

print(f'\n{code_break}\n')

user_age   = 43
num_people = 43
group_size = 43

if user_age == 62:
   item_discount = 15
else:
   item_discount = 0

print(f'\n{code_break}\n')

if num_people == 10:
   group_size = 2 * group_size
else:
   group_size = 3 * group_size
   num_people = num_people - 1



#-----------------------------------------------------------------------
print(f'\n{code_break}\n')

barcode_check_digit = int(input())  # Program will be tested with values: 5, 6, 7, 8.

''' Your code goes here '''
if barcode_check_digit != 7:
  group_id = 10
else:
  group_id = barcode_check_digit

print(group_id)

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')

num_difference = int(input())  # Program will be tested with values: -13 -14 -15 -16.

''' Your code goes here '''

print(total_difference)

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')
number_of_wheels = int(input())

''' Your code goes here '''
if number_of_wheels == 8:
    print('Eight-wheel drive')
else:
    print('Not an eight-wheel drive')

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')

item_count = int(input())
allowed_groups = int(input())
rejected_groups = int(input())

''' Your code goes here '''
if item_count >= 19:
    allowed_groups += 3
else:
    rejected_groups += 1

print(allowed_groups)
print(rejected_groups)

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')
'''When the input variable checked_bag_size is:

less than or equal to 43, output 'Too small'.
between 43 exclusive and 124 exclusive, output 'Luggage compartment'.
greater than or equal to 124, output 'Too large'.'''

checked_bag_size = int(input())
''' Your code goes here '''
if checked_bag_size <= 43:
    print('Too small')
elif checked_bag_size < 124:
    print('Luggage compartment')
else:
    print('Too large')

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')

'''When the input variable num_books is:

greater than 136, output 'Too many books'.
between 28 inclusive and 136 inclusive, output 'Full-wall bookshelf'.
between 1 inclusive and 27 inclusive, output 'Medium bookshelf'.
less than 1, output 'Invalid input'.'''

num_books = int(input())

if num_books > 136:
  print('Too many books')
elif 28 <= num_books <= 136:
  print('Full-wall bookshelf')
elif 1 <= num_books <= 27:
  print('Medium bookshelf')
else:
  print('Invalid input')

#-----------------------------------------------------------------------
print(f'\n{code_break}\n')
number_of_parts = int(input())

if number_of_parts == 1:
  print('Monad')
elif number_of_parts == 2:
  print('Dyad')
elif number_of_parts == 4:
  print('Tetrad')
else:
  print('Another number of components')

#-----------------------------------------------------------------------
# Practice if-else statements
print(f'\n{code_break}\n')

supplied_cups = int(input())

''' Your code goes here '''
if (55 < supplied_cups <= 90):
    print('Standard package')
elif (120 < supplied_cups <= 160):
    print('Full package')
else:
    print('Not efficient to ship')

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Nested if-else statements
user_choice = 2  # Hardcoded values for this tool. Could be input()...
num_items = 5

if user_choice == 1:    
   print('user_choice is 1')
elif user_choice == 2:
   if num_items < 0:
      print('user_choice is 2 and num_items < 0')
   else:
	      print('user_choice is 2 and num_items >= 0')
else:
	 print('user_choice is neither 1 or 2')


#-----------------------------------------------------------------------
print(f'\n{code_break}\n')

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
      print('The city is melting!')
    else:
        print(f"The temperature in New York is {temperatures['New York']}.")
else:
    print('The temperature in New York is unknown.')
    
print(f'Side length: {s} cm')
print(f'Area: {area:.2f} cm^2')
print(f'Perimeter: {perimeter:.2f} cm')

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Multiple distinct IF


print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Challenges
'''
If time_spent is greater than or equal to 36, then output 'I can complete my homework.'
If time_spent is greater than 53, then output 'I can finish my homework and have extra time.'
If time_spent is less than 7, then output 'I do not have time to do my homework.'
'''

time_after_class = int(input())

''' Your code goes here '''

if 14 <= time_after_class:
  print('I can complete my homework.')
  
if 30 < time_after_class:
  print('I can finish my homework and have extra time.')
  
if 6 > time_after_class:
  print('I do not have time to do my homework.')

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Challenges

'''
If input_num1 is greater than or equal to 30, then output 'input_num1 is greater than or equal to 30.'
If input_num2 is less than 15, then assign input_num2 with 1.
Otherwise, output 'input_num2 is greater than or equal to 15.'
'''

input_num1 = int(input())
input_num2 = int(input())

''' Your code goes here '''
if input_num1 >= 30:
  print('input_num1 is greater than or equal to 30.')
  
if input_num2 < 15:
  input_num2 = 1
else:
  print('input_num2 is greater than or equal to 15.')

print(f'input_num2 is {input_num2}.')

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Challenges
'''
Integers num_mangos and money_in_bank are read from input. Each mango costs 3 dollars.

Write the following if-else statement. Within the if branch, write the following assignment and nested if-else statement:

If num_mangos is greater than or equal to 4:
Assign variable total_cost with the product of num_mangos and 3.
If total_cost is less than or equal to money_in_bank, then output 'Mangos successfully purchased'.
Otherwise, output 'Not enough money to buy all'.
Otherwise, output 'Please purchase at least 4 mangos'.
'''

num_mangos = int(input())
money_in_bank = int(input())

''' Your code goes here '''
if num_mangos >= 4:
  total_cost = 3 * num_mangos
  if total_cost <= money_in_bank:
    print('Mangos successfully purchased')
  else:
    print('Not enough money to buy all')
else:
  print('Please purchase at least 4 mangos')
  
print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Membership and Identity

special_list = [-99, 0, 44]
special_num = int(input())

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
    
print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Fix the indentation in the code below
b = int(input())
h = int(input())
area = 0.5 * b * h

print(f'Base = {b} in')
print(f'Height = {h} in')
print(f'Area = {area:.2f} in^2')

child_age = input()
color = input()

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Implicit Join
# Modify the following line
biography_str = ('Gale is {0} years old and lives in Cheyenne, Wyoming. '
                 'Their favorite color is {1} and they want to be a marine '
                 'biologist when they grow up.')

# format() replaces the curly braces in a string with variables.
# This method is being used to test your code.
new_str = biography_str.format(child_age, color)
print(new_str)

print(f'\n{code_break}\n')
#-----------------------------------------------------------------------
# Conditional Expression
# OR
# Ternary Operator
x = 9
y = 0 if (x < 100) else x

user_val = int(input())
cond_str = ''' Your solution goes here '''
cond_str = 'negative' if (user_val < 0 ) else 'nonnegative'
print(f'{user_val} is {cond_str}')

num_users = int(input())
update_direction = int(input())
num_users = (num_users + 1) if (update_direction== 3) else (num_users - 1)
print(f'New value is: {num_users}')
