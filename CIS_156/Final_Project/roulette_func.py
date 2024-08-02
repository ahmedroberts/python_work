# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

''' Import modules '''
import random
import roulette_data as r_data

''' Declare Global Variables '''
bet_types= r_data.bet_type_dict
payouts = r_data.payout_dict

''' Functions '''
# simulate spin using random choice and number list
def simulate_spin():
  num = random.choice(r_data.american_roulette_numbers)
  return num

def get_bet(bet_strat, since_hit):
  bet = bet_strat[since_hit]
  return bet

def column_headers():
  print(f'\n{"#":>2} |{"Num":^5}| {"Bet 1":^7} |{"Bet 2":^7}')

def show_player_old(player):
  print(f'\n\t{"Curr Player":<10} : {player.name:<15}')
  print(f'{player.name} is playing the `{player.strategy_name}` strategy.')
  print(f'They started with a bank of ${player.starting_bank}', end=' ')
  # if player.up_down >= 0:
  #   print(f'now up ${player.up_down}.')
  # else:
  #   print(f'now down ${player.up_down}.')
  # print('******************\n')
  
def show_player(player):
  print(f'\n\t{"Curr Player":<10} : {player.name:<15}')
  print(f'{player.name} is playing the `{player.strategy_name}` strategy.')
  print(f'Starting bank ${player.starting_bank:,d}', end=' ')
  print(f'w/ goal of {player.goal:,d}.')

def show_up_down(player):
  curr_profit = player.curr_bank - player.starting_bank
  if curr_profit > 0:
    print(f'{player.name} now up ${curr_profit:,d}.\n=> Bank: {player.curr_bank:,d}' )
  elif curr_profit < 0:
    print(f'{player.name} now down ${(-1*curr_profit):,d}.\n=> Bank: {player.curr_bank:,d}')
  else:
    print(f'{player.name} is currently even.\n=> Bank: {player.curr_bank:,d}')
  
def check_hit(bango, gurupu):
  isHit = False
  if bango in gurupu:
    isHit = True
  return isHit
  
def simulate_player_turn_old(player, spin_result):
  print('start', player.total_spins, player.curr_bank)
  player.total_spins += 1
  player.total_spins += 1
  curr_bet_amount = player.bet_strat[player.spins_since_hit]
  # check hit or miss
  if check_hit(spin_result, bet_types["3rd Column"]):
    print(f'Thats a hit on {spin_result}! => {curr_bet_amount}')
    player.spins_since_hit = 0
    player.curr_bank = player.curr_bank + curr_bet_amount + (curr_bet_amount * payouts[player.bet_type])
    print('start', player.total_spins, "new bank ==>", player.curr_bank)
  else:
    print('miss')
    player.spins_since_hit += 1
    print('start', player.total_spins, player.curr_bank)
    
def simulate_player_turn(player, spin_result):
  # print('start', player.total_spins, player.curr_bank)
  player.total_spins += 1
  hit_or_miss = False
  curr_bet_amount = player.bet_strat[player.spins_since_hit]
  hit_payout = curr_bet_amount + (curr_bet_amount * payouts[player.bet_type])
  # check hit or miss
  if check_hit(spin_result, bet_types["3rd Column"]):
    # print(f'Thats a hit on {spin_result}! => {curr_bet_amount}')
    hit_or_miss = True
    player.spins_since_hit = 0
    player.curr_bank = player.curr_bank + hit_payout
    # print('start', player.total_spins, "new bank ==>", player.curr_bank)
  else:
    # print('miss')
    player.spins_since_hit += 1
    player.curr_bank = player.curr_bank - curr_bet_amount
    # print('start', player.total_spins, player.curr_bank)
  
  print(f'{player.total_spins:>2}.', end=' ')
  print(f'Bet: {curr_bet_amount:^4}', end=' ')
  print(f'{spin_result:>2}', end='')
  # print(f'{"* Hit!" if hit_or_miss else "  Miss"}', end=' ')
  # print(f' Miss: {player.spins_since_hit} {player.curr_bank:,d}')
  if hit_or_miss:
    print(f' Hit!: * {player.curr_bank:,d}')
    print(f'{"Payout: ":>24} {hit_payout:,d}\n')
  else:
    print(f' Miss: {player.spins_since_hit} {player.curr_bank:,d}')
  