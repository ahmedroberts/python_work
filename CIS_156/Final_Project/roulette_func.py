# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

import random
from roulette_data import num_list, bet_dict, payout_dict

''' Functions '''
# simulate spin using random choice and number list
def simulate_spin():
  num = random.choice(num_list)
  return num

def get_bet(bet_strat, since_hit):
  bet = bet_strat[since_hit]
  return bet


def column_headers():
  print(f'\n{"#":>2} |{"Num":^5}| {"Bet 1":^7} |{"Bet 2":^7}')

def show_player(player):
  print(f'\n\t{"Curr Player":<10} : {player.name:<15}')
  print(f'{player.name} is playing the `{player.strategy_name}` strategy.')
  print(f'They started with a bank of ${player.starting_bank}', end=' ')
  if player.up_down >= 0:
    print(f'now up ${player.up_down}.')
  else:
    print(f'now down ${player.up_down}.')
  print('******************\n')
  
def show_player_old(player):
  print(f'\n\t{"Curr Player":<10} : {player.name:<15}')
  print(f'{player.name} is playing the `{player.strategy_name}` strategy.')
  print(f'They started with a bank of ${player.starting_bank}', end=' ')
  if player.up_down >= 0:
    print(f'now up ${player.up_down}.')
  else:
    print(f'now down ${player.up_down}.')
  print('******************\n')
  
def check_hit(bango, gurupu):
  isHit = False
  if bango in gurupu:
    isHit = True
  return isHit
  
def simulate_player_turn(player, spin_result):
  print('start', player.total_spins, player.curr_bank)
  player.total_spins += 1
  player.total_spins += 1
  curr_bet_amount = player.bet_strat[player.spins_since_hit]
  # check hit or miss
  if check_hit(spin_result, bet_dict["3rd Column"]):
    print(f'Thats a hit on {spin_result}! => {curr_bet_amount}')
    player.spins_since_hit = 0
    player.curr_bank = player.curr_bank + curr_bet_amount + (curr_bet_amount * payout_dict[player.bet_type])
    print('start', player.total_spins, "new bank ==>", player.curr_bank)
  else:
    print('miss')
    player.spins_since_hit += 1
    print('start', player.total_spins, player.curr_bank)
  
  print('end', player.total_spins)
  