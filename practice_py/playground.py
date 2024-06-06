# Dec 18, 2021

"""
ln = int(input())
ss1 = str(input())
ss2 = str(input())
"""

ln = 2
ss1 = "Black Panther"
ss2 = "Blue Marvel"
print('\n************\n', ln, '\n', ss1, '\n', ss2, '\n************\n')


for x in range(int(input())):
    ss = input('Waiting for input...: ')
    print('So...', ss)
    z = 0
    sodd  = ''
    seven = ''
    while z < len(ss):
        if z % 2 ==0:
            sodd = sodd + ss[z]
        else:
            seven = seven + ss[z]
        z = z + 1
    print(sodd, seven)
    print('\n**********************\n')
