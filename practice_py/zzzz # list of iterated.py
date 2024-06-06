# list of iterated

from itertools import permutations
"""
tt = [7,8,9]
zz = list(permutations(tt))
print('')
print('-------------------------')
print('')
print(zz)
print('')
print('-------------------------')

print('')
print('-------------------------')
print('')
for combo in zz:
    print( sum(combo), end=', ' )
    print('')
print('')
print('-------------------------')
print('')
xxx = list(permutations(xx))
print(xxx)
"""
# Sample Data
x = 1
y = 2
z = 3
n = 2

i = 0
j = 0
k = 0
BigCombo = []

xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

i = x
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

j = y
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx


k = z
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

i = 0
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

j = 0
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

i = x
xx = [i,j,k]
Combos = [zz for zz in xx]
print(Combos)
xxx = list(permutations(Combos))
print('Combos:', xxx)
BigCombo = BigCombo + xxx

#-----------------------------

xx = [i,j,k]
Combos = [zz for zz in xx]

print('\n\n-~ Combos ~-')
print('-------------------------\n')
print(BigCombo)
print('\n-------------------------\m')

BigCombo = list(dict.fromkeys(BigCombo))

print('\n\n-~ Big Combos != n ~-')
print('-------------------------\n')
print(BigCombo)
print('\n-------------------------\m')

boss = []
assezz = []
ass = []
for tt in BigCombo:
    for d in tt:
        ass.append(d)
    assezz.append(ass)
    ass.clear

    print(' -- ',tt)
    boss.append(tt)

print('Boss:',boss)
print(assezz)
#fC = [for thing in BigCombo if (sum(thing)) != n ]
#print(fC)
