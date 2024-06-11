# Ahmed O. Roberts | June 10, 2025
# CIS 156 | Python Programming | Level 1
# Module 03 Programming Assignment
# Part A

first_family_dict = {
  'Augustus Freeman': 84,
  'Virgil Hawkins': 16,
  'Raquel Ervin': 19,
  'Curtis Metcalf': 43,
  'Hannibal White': 23
}

print('\n')
print(first_family_dict)
key_two = 'Virgil Hawkins'
second_person_age = first_family_dict.get(key_two)
print(f'{key_two} is {second_person_age} years old.')
first_family_dict['Tim'] = 23
print(first_family_dict)

entered_key = input('Enter a person:\n')
entered_person_age = first_family_dict.get(entered_key)
print(f'{entered_key} is {entered_person_age} years old.')
