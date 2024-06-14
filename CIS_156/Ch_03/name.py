# Ahmed O. Roberts | June 10, 2025
# CIS 156 | Python Programming | Level 1
# Module 03 Programming Assignment
# Part A

# Given a First and Last Name Input, This program outputs:
# - full name
# - full name length
# - first letters of first and last names
# - 2nd to last letter of last name

first_name = input('\nPlease enter your first name:\n')
last_name = input('\nPlease enter your last name:\n')
full_name = first_name + ' ' + last_name

# Print full name
print(full_name)

# Print length of full name
print(f'The length of the full name is `{len(full_name)}`')

# Print first initial of first name
print(f'The first letter of the first name is `{first_name[0]}.`')

# Print first initial of last name
print(f'The first letter of the last name is `{last_name[0]}.`')

# print 2nd to last letter of the last name
print(f'The second to last letter of the first name is `{last_name[-2]}.`')
