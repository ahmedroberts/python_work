# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

import random
from roulette_data import num_list

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
