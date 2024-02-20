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

# https://www.geeksforgeeks.org/print-colors-python-terminal/
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))


# Raikage Print
COLOR_RED = "\033[91m {}\033[00m"
COLOR_GREEN = "\033[92m {}\033[00m"
COLOR_YELLOW = "\033[93m {}\033[00m"
COLOR_LIGHT_PURPLE = "\033[94m {}\033[00m"
COLOR_PURPLE = "\033[95m {}\033[00m"
COLOR_CYAN = "\033[96m {}\033[00m"
COLOR_LIGHT_GRAY = "\033[97m {}\033[00m"
COLOR_BLACK = "\033[98m {}\033[00m"
def prColor(fg_text_color, text_content):
    print(fg_text_color.format(text_content))
    
__raikage_dunder__ = "King Ahmed - The 9th Raikage"
    
prColor(COLOR_RED, __raikage_dunder__)
prColor(COLOR_GREEN, __raikage_dunder__)
prColor(COLOR_YELLOW, __raikage_dunder__)
prColor(COLOR_LIGHT_PURPLE, __raikage_dunder__)
prColor(COLOR_PURPLE, __raikage_dunder__)
prColor(COLOR_CYAN, __raikage_dunder__)
prColor(COLOR_LIGHT_GRAY, __raikage_dunder__)
prColor(COLOR_BLACK, __raikage_dunder__)
'''
Color Print Examples 
https://www.studytonight.com/python-howtos/how-to-print-colored-text-in-python
prCyan("Hello World, ")
prYellow("It's")
prGreen("Geeks")
prRed("For")
prGreen("Geeks")
'''

# Create Constants for bet
RED, BLACK = [], []
ODD, EVEN = [], []
FIRST12, SECOND12, THIRD12 = [], [], []
FIRSTCOL, SECONDCOL, THIRDCOL = [], [], []
ONETO18, NINETEENTO36 = [], []
ZERO, DBLZERO = "0", "00"

red_number = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
black_number = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
odd_number = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
odd_number = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
first_col  = [1,4,7,10,13,16,19,22,25,28,31,34]
second_col = [2,5,8,11,14,17,20,23,26,29,32,35]
third_col  = [3,6,9,12,15,18,21,24,27,30,33,36]

RED = red_number
print(f"Red Numbers: {RED}")

'''
for i in range(1, 37):
    print(f"{i} modulo 3 = {i % 3}")
'''

# Print Spin Results | Test
prYellow("\n\n*******************\tSpin Results\t*******************\n")
for item in range(1, 9):
    # Red | Black
    spin_msg = f"\t# {item} ~"
    if item in red_number:
        spin_msg += " red |"
    else:
        spin_msg += " black |"
    
    # Odd | Even
    if item in odd_number:
        spin_msg += " odd"
    else:
        spin_msg += " even"
        
    # 1st, 2nd, or 3rd Column
    if item in first_col:
        spin_msg += " | column 1"
    elif item in second_col:
        spin_msg += " | column 2"
    else:
        spin_msg += " | column 3"
        
    # Display Results
    if item in black_number:
        prCyan(spin_msg)
    else:
        prRed(spin_msg)
prGreen("\n*******************\t*************\t*******************\n\n")