# Strings Practice

## Slicing it Up
full_string = 'Ahmed is the 9th Raikage!'

sliced_string = full_string[3:9]
first3 = full_string[0:3]
last2 = full_string[-2:]
exclude_index_2 = full_string[:1] + full_string[3:]
''' 
Integer skip_num is read from input. 
Assign variable sub_string with every skip_num element of full_string's last half. 
'''
skip_num = 2
sub_string = full_string[len(full_string)//2::skip_num]

print(f'sliced_string: {sliced_string}')
print(f'first3: {first3}')
print(f'last2: {last2}')
print(f'exclude_index_2: {exclude_index_2}')
print(f'sub_string: {sub_string}')

def code_breaker():
  print('\n# --------------------------------------------------------\n')
 
code_breaker()
# -----------------------------------------------------------------------'

## Advanced formatting
print(f'{"Player Name":16}{"Goals":8}')
print('-' * 24)
print(f'{"Sadio Mane":16}{"22":8}')
print(f'{"Gabriel Jesus":16}{"7":8}')

code_breaker()
# -----------------------------------------------------------------------'

## Food Stuff
food_name = 'oreo cookies'
food_count = 33

print(f'{food_name:>>20}')
print(f'{food_count:<^20}')

code_breaker()
# -----------------------------------------------------------------------'

employees = input().split()
states = input().split()
separator_char = input()

print(f'{"Employees":^21}|{"States":^21}')
print(f'{separator_char * 42}')
print(f'{employees[0]:^21}|{states[0]:^21}')
print(f'{employees[1]:^21}|{states[1]:^21}')
print(f'{employees[2]:^21}|{states[2]:^21}')
