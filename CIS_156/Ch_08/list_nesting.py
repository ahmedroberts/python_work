# ######################################## #
print()
'''
Each iteration row is assigned the next list element from currency. 
Each item in a row is printed in the inner loop.
'''

currency = [

        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()

# ######################################## #
print()

# color1 = input().split()
# color2 = input().split()
# color3 = input().split()
color1 = 'maroon'
color2 = 'magenta'
color3 = 'purple'

''' Your code goes here '''
three_colors = [color1, color2, color3]

print(three_colors[0])
print(three_colors[1])
print(three_colors[2])

# ######################################## #
print()
row1 = ['X', 'O', 'X']
row2 = ['X', 'O', 'O']
row3 = ['X', 'X', 'O']
game_board = [
  row1,
  row2,
  row3
]

print(game_board[0])
print(game_board[1])
print(game_board[2])

column1 = False
column0 = (game_board[0][0] == 'X' and game_board[1][0] == 'X' and game_board[2][0] == 'X')
column1 = (game_board[0][1] == 'X' and game_board[1][1] == 'X' and game_board[2][1] == 'X')
column2 = (game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X')
print('Column 1: ', column1)
print('00: ', game_board[0][0])
print('10: ', game_board[1][0])
print('20: ', game_board[2][0])

if column1:
  print('Player x wins at column 1.')
else:
  print('Player x does not win at column 1.')


# ######################################## #
print()

grid_size = int(input('Enter grid size: '))

pattern_grid = []
for i in range(grid_size):
    row = []
    for j in range(grid_size):
        row.append(0)
    pattern_grid.append(row)

''' Your code goes here '''
for i in range(grid_size):
  for j in range(grid_size):
    pattern_grid[i][j] = int(i) + int(j)
''' end my code '''

for row in pattern_grid:
    for cell in row:
        print(cell, end=' ')
    print()