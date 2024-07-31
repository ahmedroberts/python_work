# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette

# This program simulates the outcome of certain american roulette betting strategies

import random

''' create list of roulette numbers '''
zeroes = [0, '00']
dozen1 = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
dozen2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
dozen3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
num_list = zeroes + dozen1 + dozen2 + dozen3

spin = 0

# simulate spin using random choice an number list
def simulate_spin():
  num = random.choice(num_list)
  return num

def bet_amount(betting_system=0, spins_since_hit=0):
  amount = 5
  if (betting_system == 0) and (spins_since_hit == 0):
    amount = 25
  return amount

print(f'\n{"#":>2} |{"Num":^5}|{"Bet":>5}')
print('-' * 25)
while spin < 25:
  spin += 1
  if ((spin -1) % 10 == 0) and ((spin - 1) != 0):
    print() 
  # - simulate a spin
  result = simulate_spin()
  print(f'{spin:>2}. {result:^5}', end=' ')
  # - calculate next bet
  print(f'{bet_amount():>5}')

print('\nAll done.\n')