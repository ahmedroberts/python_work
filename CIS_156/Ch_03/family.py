# Ahmed O. Roberts | June 10, 2025
# CIS 156 | Python Programming | Level 1
# Module 03 Programming Assignment
# Part B

# Create Milestone family dictionary
first_family_dict = {
  'Augustus': 84,
  'Virgil': 16,
  'Raquel': 19,
  'Curtis': 43,
  'Hannibal': 27
}

# Print dictionary
print(first_family_dict)

# Disply second item
key_two = 'Virgil'
second_person_age = first_family_dict.get(key_two)
print(f'{key_two} is {second_person_age} years old.')

# Add Tim: 23
first_family_dict['Tim'] = 23

# Print updated dictionary
print(first_family_dict)

# Lookup by key:name and print item
entered_key = input('Enter the name to lookup: ')
entered_person_age = first_family_dict.get(entered_key)
print(f'{entered_key} is {entered_person_age} years old.')
