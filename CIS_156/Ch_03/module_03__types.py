# Ahmed Roberts The 9th Raikage 
# June 2024 - Estrella Mountain CC
# CIS156 Python Progamming - Level 1

code_break = '#-----------------------------------------------------------------------'
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Strings
greeting = 'Ahmed is the 9th Raikage!'
passcode = '(th*R^1k^g#!'

print(f'\"{greeting}\" is {len(greeting)} characters long.')
print(f'\"{passcode}\" is {len(passcode)} characters long.')
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Lists
supers = ['Black Panther', 'Icon', 'Blue Marvel']
print(supers)

supers.append('Storm')
supers.append('Aokiji')
supers.append('Rocket')

print(f'After appending:\n\t{supers}')
supers.pop(4)
print(f'After pop(4):\n\t{supers}')
supers.remove('Blue Marvel')
print(f'After remove(\'Blue Marvel\'):\n\t{supers}')
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Reads four values from input into data_list
data_list = [int(input('enter int: ')), int(input('enter int: ')), 
             int(input('enter int: ')), int(input('enter int: '))]
len_value = len(data_list)
min_value = min(data_list)
sum_value = sum(data_list)

print(f'List length: {len_value}')
print(f'Min: {min_value}')
print(f'List sum: {sum_value}')
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Sets
my_favorites = {'jackal', 'tiger', 'wolf'}
your_favorites = {input('enter predator: '), 
                  input('enter predator: '), input('enter predator: ')}
our_favorites = my_favorites.intersection(your_favorites)

print(f'My favorite animals: {sorted(my_favorites)}')
print(f'Your favorite animals: {sorted(your_favorites)}')
print(f'Our favorite animals: {sorted(our_favorites)}')
print(f'\n{code_break}\n')

#-----------------------------------------------------------------------
# Dictionaries
superhero_ids = {
  'Blue Marvel':'Tchalla',
  'Icon':'Augustus Freeman IV',
  'Black Panther':"T'Challa, son of T'Chaka"
  }

for k, v in superhero_ids.items():
  print(f'{k} is really {v}!😮')
  
prices = {}  # Create empty dictionary
prices['banana'] = 1.49  # Add new entry
print(prices)

prices['banana'] = 1.69  # Modify entry
print(prices)

del prices['banana']  # Remove entry
print(prices)
#-----------------------------------------------------------------------
print(f'\n{code_break}\n')