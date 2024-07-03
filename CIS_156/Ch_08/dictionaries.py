'''
Dictionaries
A dictionary is another type of container object that is different from sequences such as strings, tuples, and lists. 
Dictionaries contain references to objects as key-value pairs — each key in the dictionary is associated with a value, 
much like each word in an English language dictionary is associated with a definition. 
As of Python 3.7, dictionary elements maintain their insertion order. 
The dict type implements a dictionary in Python.
'''

dict1 = {'Jose': 'A+', 'Gino': 'C-'}
dict2 = dict(Bobby='805-555-2232', Johnny='951-555-0055')
dict3 = dict([('Bobby', '805-555-2232'), ('Johnny', '951-555-0055')])

print('\n', dict1, '\n', dict2, '\n', dict3, '\n')

color_dict = {'red': 220, 'green': 20, 'blue': 60}

key_read = 'note'
value_read = 'my favorite color'

color_dict[key_read] = value_read

print(f'red: {color_dict["red"]}')
print(f'green: {color_dict["green"]}')
print(f'blue: {color_dict["blue"]}')
print(f'{key_read}: {color_dict[key_read]}')

def code_breaker():
  print('\n################################################\n')

code_breaker() ################################################



code_breaker() ################################################