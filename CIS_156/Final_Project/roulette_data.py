# Ahmed O. Roberts
# Programming Assignment
# Final Project - Roulette Strategy Explorer

''' Create list of roulette numbers '''
# American Roulette Zero and Double Zero
zeroes = [ 0,'00']
dozen1 = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]
dozen2 = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
dozen3 = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
# Full list of american roulette numbers
num_list = zeroes + dozen1 + dozen2 + dozen3
american_roulette_numbers = zeroes + dozen1 + dozen2 + dozen3

''' Create Roulette bet types w/ target always No. 9 '''

bet_type_dict = {
  "Straight Up": [9],
  "Split": [8, 9],
  "Basket": ['00', 2, 3],
  "Street": [7, 8, 9],
  "Corner": [8, 9, 11, 12],
  "Six Line": [7, 8, 9, 10, 11, 12],
  "3rd Column": [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
  "1st Dozen" : dozen1,
  "Odd": [1, 3, '...', 9,'...', 35],
  "Red": [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36],
  "1 to 18": [1, 2, '...', 9, '...', 18]
}

# Payout = (current bet * payout) + payout
payout_dict = {
  "Straight Up": 35,
  "Split": 17,
  "Basket": 11,
  "Street": 11,
  "Corner": 8,
  "Six Line": 5,
  "3rd Column": 2,
  "1st Dozen" : 2,
  "Odd": 1,
  "Red": 1,
  "1 to 18": 1
}

# strategic betting amounts
strat_one_column = [2, 4, 6, 8, 13, 20, 30, 50, 80, 130, 210, 340, 130, 20, 20, 20]
strat_one_column_high_limit = [50, 25, 50, 100, 150, 200, 300, 450, 700, 1100, 1600, 3000, 5000, 5000, 5000]
strat_martigale = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 0, 0, 0]
strat_parachute = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]

