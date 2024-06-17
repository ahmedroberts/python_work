# Ahmed Roberts
# Chapter 5 Solution Demo

# This program prints a table showing equivalent distances in miles and feet
# -- every 10 lines print a space

for miles in range(1, 51):
  feet = 5280 * miles
  print(miles, 'miles =\t', feet, 'feet')
  if (miles % 10 == 0):
    print()