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

print(full_name)
print(len(full_name))
print(first_name[0])
print(last_name[0])
print(last_name[-2])