# Ahmed O. Roberts
# Module 06 - Programming Assignment
# Part A

# This program determines the cost of yearly vehicle ownership.

print('\nFor the calculations enter monthly costs of the following items.\n')

payment = float(input('Monthly cost of loan payment: '))
insurance = float(input('Monthly cost of insurance premium: '))
gas = float(input('Monthly cost of gas: '))
oil_change = float(input('Monthly cost of oil changes: '))
tires = float(input('Monthly cost of tires: '))
maintenance = float(input('Monthly cost of general maintenance: '))

def annual_cost(payment, insurance, gas, oil_change, tires, maintenance):  
  costs = 0
  costs = 12 * (payment + insurance + gas + oil_change + tires + maintenance)
  return costs

total_annual_cost = annual_cost(payment, insurance, gas, oil_change, tires, maintenance)

print(f'\nToatal annual cost would be ${total_annual_cost:.2f}.\n')