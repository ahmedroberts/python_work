# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette

# This program simulates the outcome of certain american roulette betting strategies

import random

''' create list of roulette numbers '''
zeroes = [ 0,'00']
dozen1 = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
dozen2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
dozen3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
num_list = zeroes + dozen1 + dozen2 + dozen3

spin = 0

strat_one_column = [2, 4, 6, 8, 13, 20, 30, 50, 80, 130, 210, 340, 130, 20, 20, 20]
strat_one_column_high_limit = [50, 25, 50, 100, 150, 200, 300, 450, 700, 1100, 1600, 3000, 5000, 5000, 5000]

# simulate spin using random choice an number list
def simulate_spin():
  num = random.choice(num_list)
  return num

# def bet_amount(betting_system=0, spins_since_hit=0):
#   amount = 5
#   if (betting_system == 0) and (spins_since_hit == 0):
#     amount = 25
#   return amount

def get_bet(bet_strat, since_hit):
  bet = bet_strat[since_hit]
  return bet

# print('----------', strat_one_column[4], get_bet(strat_one_column_high_limit, 4))
# print('---------->>', get_bet(strat_one_column_high_limit, 0))

def column_headers():
  print(f'\n{"#":>2} |{"Num":^5}| {"Bet 1":^7} |{"Bet 2":^7}')
column_headers()
print('-' * 25)

# selected strategy
curr_strat = strat_one_column_high_limit
alt_strat = strat_one_column

# Loop to run program
while spin < 40:
  
  # ---------- print('Spin:', 0, spin)
  # bet1 = bet_amount()
  bet2 = get_bet(curr_strat, spin) if spin < len(curr_strat) else curr_strat[len(curr_strat)-1]
  bet3 = get_bet(alt_strat,  spin) if spin < len(curr_strat) else alt_strat[len(alt_strat)-1]
  spin += 1
  if ((spin -1) % 10 == 0) and ((spin - 1) != 0):
    print()
    column_headers()
    
  # - simulate a spin
  result = simulate_spin()
  print(f'{spin:>2}. {result:>5}', end=' ')
  # - calculate next bet
  # print(f'{bet1:>5}', end=' ')
  print(f'{bet2:>7}', end=' ')
  print(f'{bet3:>7}')

print('\nAll done.\n')