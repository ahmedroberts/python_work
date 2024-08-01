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
player1.set_name('Big Money One')
player1.set_play_money(12000, 15000)
player1.set_betting('Last Column', strat_one_column_high_limit, 1000)

player2 = Roulette_Player()
player2.set_name('Noob Two')
player2.set_play_money(5000, 7000)
player2.set_betting('Martingale', strat_martigale, 1500)

player3 = Roulette_Player()
player3.set_name('Bet Nerd 3')
player3.set_play_money(2500, 6000)
player3.set_betting('Parachute', strat_parachute, 2000)

def show_player(player):
  print(f'\n\t{"Curr Player":<10} : {player.name:<15}')
  print(f'{player.name} is playing the `{player.strategy_name}` strategy.')
  print(f'They started with a bank of ${player.starting_bank}', end=' ')
  if player.up_down >= 0:
    print(f'now up ${player.up_down}.')
  else:
    print(f'now down ${player.up_down}.')
  print('******************\n')
  
def simulate_player_turn(player, spin_result):
  print('start', player.total_spins, player.curr_bank)
  player.total_spins += 1
  curr_bet_amount = player.bet_strat[player.spins_since_hit]
  if spin_result == 9:
    print('Thats a hit on {spin_result}! => {curr_bet_amount}')
    player.curr_bank = player.curr_bank + curr_bet_amount + (curr_bet_amount * payout_dict[player.bet_type])
    print('start', player.total_spins, player.curr_bank)
  else:
    print('miss')
    player.spins_since_hit += 1
    print('start', player.total_spins, player.curr_bank)
  
  print('end', player.total_spins)
  
simulate_player_turn(player1, 9)
simulate_player_turn(player1, 19)
simulate_player_turn(player1, 9)
simulate_player_turn(player1, 29)
  
  
show_player(player3)
show_player(player2)
show_player(player1)

''' Start main program run '''

column_headers()
print(h_break1)
# Loop to run program
while spin < max_spins:
  # Simulate a spin
  result = simulate_spin()
  
  
  
  # Calculate Spin Results
  bet2 = get_bet(curr_strat, spin) if spin < len(curr_strat) else curr_strat[len(curr_strat)-1]
  bet3 = get_bet(alt_strat,  spin) if spin < len(curr_strat) else alt_strat[len(alt_strat)-1]
  spin += 1
  if ((spin -1) % 10 == 0) and ((spin - 1) != 0):
    print()
    column_headers()
    
  
  # Display Spin Results
  print(f'{spin:>2}. {result:>5}', end=' ')
  # - calculate next bet
  # print(f'{bet1:>5}', end=' ')
  print(f'{bet2:>7}', end=' ')
  print(f'{bet3:>7}')

print(f'\n{"*** All done. ***":^25}\n')