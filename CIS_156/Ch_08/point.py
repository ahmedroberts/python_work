dict1 = {}

dict1['a'] = 4

dict1['b'] = 5

dict1['c'] = 2

dict1['d'] = 1

dict1['e'] = 3  

mylist = list(dict1.values())

sorted_mylist = sorted(mylist)

for x in sorted_mylist:
  print(x, end=' ')