# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

# This program simulates the outcome of certain american roulette betting strategies

import roulette_func as funcs
import roulette_data as r_data
from roulette_classes import Roulette_Player

''' Global Variables '''
spin = 0
max_spins = 29
h_break1 = '-' * 50 # horizontal break

''' Create Player Instances'''
player1 = Roulette_Player()
player1.set_name('Big Money One')
player1.set_play_money(12000, 15000)
player1.set_betting('Last Column', r_data.strat_one_column_high_limit, 1000)

player2 = Roulette_Player()
player2.set_name('Noob Two')
player2.set_play_money(5000, 7000)
player2.set_betting('Martingale', r_data.strat_martigale, 1500)

player3 = Roulette_Player()
player3.set_name('Bet Nerd 3')
player3.set_play_money(2500, 6000)
player3.set_betting('Parachute', r_data.strat_parachute, 2000)

all_players = [player1, player2, player3]
  
''' Start main program ui section '''

try:
  num_test_spins = int(input('How many spins shall we try?: '))
except:
  print('Apologies, that did not work.')

# All Spins in the test
all_test_spins = []

print(h_break1)
# Loop to run program
for spin in range(num_test_spins):
  # Simulate a spin
  spin_result = funcs.simulate_spin()
  all_test_spins.append(spin_result)
  print(f'{spin}. {spin_result}')
  
# Now we have all spins and all plyers
print("All Spins: ", end='')
print(all_test_spins)
print(f'\n{h_break1}')

print('\n\n\n~~~~~~~~~~~~~~~~~~ Start: All Players ~~~~~~~~~~~~~~~~~~\n')
for player in all_players:
  print(f'\n{player.name} | {player.strategy_name}')
  for spin in all_test_spins:
    funcs.simulate_player_turn(player, spin)
print('\n~~~~~~~~~~~~~~~~~~ End: All Players ~~~~~~~~~~~~~~~~~~\n\n\n')

print('Ready Player One | (3rd Column Strat) Test')   
for spin in all_test_spins:
  funcs.simulate_player_turn(player1, spin)


print(f'\n{"*** All done. ***":^25}\n')