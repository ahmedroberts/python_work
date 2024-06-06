# 
# HackerRank Day 8

"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phoneBook = {}
for x in range(n):
    entry = str(input())
    entry = entry.replace(' ',',')
    phoneBook.update(entry)
    
for x in range(n):
    if str(input()) == phoneBook.keys:
        print(phoneBook.values)
    else:
        print(Not found)
     
"""

n=3
phoneBook = {}
entries=[('Ahmed 65432112'), ('Anaya 78945612'), ('Donovan 12345678')]
trys = ['Ahmed', 'Viper', 'Donovan']
for entry in entries:
    #print(entry)
    zz = entry.split(' ')
    k = zz[0]
    v = zz[1]
    phoneBook[k] = v

for i in range(n):
    phoneBook[k[i]] = v[i]

for ele in trys:
    if ele in phoneBook:
        print(ele, phoneBook.get(ele), sep='=')
    else:
        print(ele, 'not found')

#print('k:', k)
#print('v:', v)

#print(type(phoneBook))
#print(phoneBook)

n=3
phoneBook = {}
k = []
v = []
entries=[('Ahmed 65432112'), ('Anaya 78945612'), ('Donovan 12345678')]
trys = ['Ahmed', 'Viper', 'Donovan']
for entry in entries:
    #print(entry)
    zz = entry.split(' ')
    k.append(zz[0])
    v.append(zz[1])

for i in range(n):
    phoneBook[k[i]] = v[i]

for ele in range(len(phoneBook)):
    if ele in phoneBook:
        print(ele, phoneBook.get(ele), sep='=')
    else:
        print(ele, 'not found')