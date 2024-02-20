# Ahmed Roberts 
# Roulette Tracking 3 Systems
# 1. Martingale
# 2. Parachute
# 3. Ahmed's Can't Lose

'''
Roulette has 38 outcomes 1/38 = 

http://www.fastodds.com/game-odds/roulette.htm
Roulette, like craps, is an independent variable game where luck determines the winners. 
An air of sophistication graces the table and the possibility of winning up to 35 times your bet 
creates an enticing lure for many players. The odds in roulette are easy to calculate. 
The wheel is divided into either 37 or 38 slots, depending on whether you are playing the European 
version (single zero), or the American version which has an extra space in the double zero. 
The zero space(s) represent the house edge. If there were none, it would be an even money game. 
The house advantage in single zero roulette is 2.7% and for the double zero game it is 5.26%.


'''
RED, BLACK = [], []
ODD, EVEN = [], []
FIRST12, SECOND12, THIRD12 = [], [], []
FIRSTCOL, SECONDCOL, THIRDCOL = [], [], []
ONETO18, NINETEENTO36 = [], []
ZERO, DBLZERO = "0", "00"

red_number = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
blk_number = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
odd_number = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
odd_number = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
first_col  = [1,4,7,10,13,16,19,22,25,28,31,34]
second_col = [2,5,8,11,14,17,20,23,26,29,32,35]
third_col  = [3,6,9,12,15,18,21,24,27,30,33,36]

'''
for i in range(1, 37):
    print(f"{i} modulo 3 = {i % 3}")
'''

for item in range(1, 37):
    spin_msg = f"\t# {item} ~"
    if item in red_number:
        spin_msg += " red |"
    else:
        spin_msg += " black |"
        
    if item in odd_number:
        spin_msg += " odd"
    else:
        spin_msg += " even"
    print(spin_msg)