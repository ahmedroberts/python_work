
def print_operation(number1, number2):
    print(f'{number1} - {number2} = {number1 - number2}')

even_number = 4
odd_number = 3
print_operation(even_number, odd_number)
# ----------------------------------------------------------------------

def print_operation(number1, number2):
    print(f'{number1} + {number2} = {number1 + number2}')

even_number = 4
odd_number = 3
print_operation(even_number, odd_number)
# ----------------------------------------------------------------------

def print_points(name, age, total_points):
    print(f'{name} is {age}')
    print(f'{name} made {total_points} points')

user_name = 'May'
user_age = 20
regular_time_points = 26
overtime_points = 5

print_points(user_name, user_age, regular_time_points + overtime_points)

# ----------------------------------------------------------------------
def print_beverages_list(a, b, c):
  print('Top drinks:')
  print('1:', a)
  print('2:', b)
  print('3:', c)
# ----------------------------------------------------------------------
def print_region_capital(capital_name, region_name):
    msg = f"{capital_name} is {region_name}'s capital."
    print(msg)

capital_name1 = input()
region_name1 = input()
capital_name2 = input()
region_name2 = input()

print_region_capital(capital_name1, region_name1)
print_region_capital(capital_name2, region_name2)
# ----------------------------------------------------------------------
def print_calculation(x, y):
  xy_diff = x - y
  print(f'Outcome: {xy_diff:.2f}')

# ----------------------------------------------------------------------
def print_state_details(state_code, state_name):
    print(f"{state_code} is {state_name}'s state code.")

first_val = input()
second_val = input()
third_val = input()
fourth_val = input()

print_state_details(first_val, third_val)
print_state_details(second_val, fourth_val)
# ----------------------------------------------------------------------

def shift_right(list_to_modify):
    index = len(list_to_modify) - 1
    temp = list_to_modify[len(list_to_modify) - 1]
    while index > 0:
        list_to_modify[index] = list_to_modify[index - 1]
        index -= 1
    list_to_modify[0] = temp
    print(f'Shifted right: {list_to_modify}')

values_list = input().split()
new_values = values_list.copy()
shift_right(new_values)
print(f'Original: {values_list}')
# ----------------------------------------------------------------------

def pop_three_elements(list_1):
    del list_1[-3:]

items_to_update = input().split()

pop_three_elements(items_to_update)
print(items_to_update)

# ----------------------------------------------------------------------
def number_of_pennies(dollars, pennies = 0):
  total_pennies = 100 * dollars + pennies
  return total_pennies

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only

# ----------------------------------------------------------------------

def split_check(bill, people, new_tax_percentage=0.09, new_tip_percentage=0.15):
  the_split = bill + (bill * new_tax_percentage) + (bill * new_tip_percentage)
  the_split = the_split / people
  return the_split

# ----------------------------------------------------------------------