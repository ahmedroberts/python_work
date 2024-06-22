import math
def calc_pizza_area(pizza_diameter):
   pizza_radius = pizza_diameter / 2.0
   pizza_area = math.pi * pizza_radius * pizza_radius
   return pizza_area

print(f'12.0 inch pizza is {calc_pizza_area(12.0):.3f} square inches')
print(f'16.0 inch pizza is {calc_pizza_area(16.0):.3f} square inches')


# ---------------------------------------------------------------------------------
print('\n# ---------------------------------------------------------------------------------\n')

def compute(val1, val2):
   result = 0
   for i in range(val1):
      result -= val2 * 2
   
   return result

computed_value = compute(2, 4)
print(computed_value)
print('\n# ---------------------------------------------------------------------------------\n')

def print_selected_numbers(count):
   for i in range(count):
      number = int(input())
      if (number % 4) == 0:
         print(number)

num_count = 2
print_selected_numbers(num_count)
print('\n# ---------------------------------------------------------------------------------\n')

def print_popcorn_time(bag_ounces):
   if bag_ounces < 3:
      message = 'Too small'
   elif bag_ounces > 10:
      message = 'Too large'
   else:
      message = f'{bag_ounces * 6} seconds'
   
   return print(message)

# bag_ounces = int(input())
print_popcorn_time(9)
# print_popcorn_time(bag_ounces)
print('\n# ---------------------------------------------------------------------------------\n')

def find_priority(num_project_tasks):
   if num_project_tasks >= 75:
      priority = 3
   elif num_project_tasks > 25:
      priority = 2
   else:
      priority = 1
   
   return priority

print(f'Testing 80: {find_priority(80)}')
print('\n# ---------------------------------------------------------------------------------\n')

def print_values(num_a, num_b):
   for n in range(num_a, num_b + 1): 
      print(n, end=' ')
   
print_values(9, 15)