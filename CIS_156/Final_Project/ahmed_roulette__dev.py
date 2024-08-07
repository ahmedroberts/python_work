# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

# This program simulates the outcome of certain american roulette betting strategies

import random
from roulette_classes import Roulette_Player
from roulette_data import bet_dict, payout_dict
from roulette_func import simulate_spin, get_bet, column_headers


''' Global Variables '''

spin = 0
max_spins = 29
h_break1 = '-' * 50 # horizontal break

type_bet = "Six Line"
print(f'\n {"My Payout":^20} --> {bet_dict["Six Line"]} => {payout_dict["Six Line"]}')
print(f'\n {"My Payout":^20} --> {bet_dict[type_bet]} => {payout_dict[type_bet]}')

# strategic betting amounts
strat_one_column = [2, 4, 6, 8, 13, 20, 30, 50, 80, 130, 210, 340, 130, 20, 20, 20]
strat_one_column_high_limit = [50, 25, 50, 100, 150, 200, 300, 450, 700, 1100, 1600, 3000, 5000, 5000, 5000]
strat_martigale = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 0, 0, 0]
strat_parachute = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]

# selected strategy
curr_strat = strat_one_column_high_limit
alt_strat  = strat_one_column

player1 = Roulette_Player()
player1.set_name('Raikage')
player1.set_play_money(5000, 5500)
player1.set_betting(strat_one_column_high_limit, 1000)

print('\n\n', player1.name, player1.starting_bank, player1.bet_strat, player1.goal, '\n')

''' Start main program run '''

column_headers()
print(h_break1)
# Loop to run program
while spin < max_spins:
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

print(f'\n{"*** All done. ***":^25}\n')