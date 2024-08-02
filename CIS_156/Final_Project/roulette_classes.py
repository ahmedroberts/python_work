# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

''' Classes '''
# Basic Player Class
class Player:  
  def __init__(self):
    self.name = 'unkown'
    self.starting_bank = 0
    self.curr_bank = 0
    self.goal = 0
    
  def set_name(self, namae):
    self.name = namae
    
  def set_play_money(self, ikura, negai):
    self.starting_bank = ikura
    self.curr_bank = self.starting_bank
    self.goal = negai
    
# Roulette_Player class derived from Player class
class Roulette_Player(Player):
  def __init__(self):
    Player.__init__(self)
    self.strategy_name = 'unknown'
    self.bet_strat = []
    self.bet_type = 'unkown'
    self.cutoff_amount = 0
    self.total_spins = 0
    self.spins_since_hit = 0
    
  def set_betting(self, namae, senryaku, teishi):
    self.strategy_name = namae
    self.bet_strat = senryaku
    self.cutoff_amout = teishi
    
    # Set Type of bet based on Strategy Name
    if self.strategy_name == 'Last Column':
      self.bet_type = "3rd Column"
    elif self.strategy_name == 'Martingale':
      self.bet_type = 'Red'
    elif self.strategy_name == 'Parachute':
      self.bet_type = 'Straight Up'
    else:
      self.bet_type = 'Odd'
