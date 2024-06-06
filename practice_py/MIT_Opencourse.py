# Hacker Rank2
#!/bin/python

"""

Print Weird if the number is weird. Otherwise, print Not Weird.
"""

import math
import os
import random
import re
import sys

# Weird -- Not Weird
if __name__ == '__main__':
    uiInput = input("Enter a Number from 1 - 100: ")
    n = int(uiInput)
    if (n % 2 != 0) or (6 <= n <= 20):
        print("Weird")
    else:
        print('Not Weird')

if __name__ == '__main__':
    uiInput = input("Enter a Number from 1 - 100: ")
    n = int(uiInput.strip())
    if (n % 2 != 0) or (6 <= n <= 20):
        print("Weird")
    else:
        print('Not Weird')

#!/bin/python3

# Find Weird?!

n = int(input("So is it weird?"))
if (n % 2 != 0) or (6 <= n <= 20):
    print("Weird")
else:
    print('Not Weird')

if __name__ == '__main__':
    a = int(input("a? "))
    b = int(input("b? "))
    print(a+b)
    print(a-b)
    print(a*b)

(a//b)
(a/b)


n = int(input("i? "))
for i in range(1, (n+1)):
    print(i, end='')



class SuperMetas (object):
    def __init__ (self, codenamme, realname):
        self.codename = codenamme
        self.realname = realname
    def reveal (self):
        print(self.realname, "code name:", self.codename)

BM = SuperMetas ("Blue Marvel", "Adam Brashear")
BP = SuperMetas ("Black Panter", "T'Challa King")

BM.reveal()
BP.reveal()

class Coordinate (object):
    def __init__ (self, qt, jz):
        self.x = qt
        self.y = jz
    def distance (self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5

c = Coordinate(3,4)
zero = Coordinate(0,0)

print(c.distance(zero))
print(c.x)
print(zero.x)
    
"""
My First Python classes ever!! 12-12-2021

"""
class SuperMetas (object):
    def __init__ (self, codenamme, realname):
        self.codename = codenamme
        self.realname = realname
    def reveal (self):
        print(self.realname, "code name:", self.codename)

BM = SuperMetas ("Blue Marvel", "Adam Brashear")
BP = SuperMetas ("Black Panter", "T'Challa King")

BM.reveal()
BP.reveal()

class Coordinate (object):
    def __init__ (self, qt, jz):
        self.x = qt
        self.y = jz
    def distance (self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return(x_diff_sq + y_diff_sq)**0.5

c = Coordinate(3,4)
zero = Coordinate(0,0)

print(c.distance(zero))
print(c.x)
print(zero.x)
