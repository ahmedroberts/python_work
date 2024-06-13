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
