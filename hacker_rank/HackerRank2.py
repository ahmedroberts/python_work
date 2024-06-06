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


if __name__ == '__main__':
    rawUiInput = input("Enter a Number from 1 - 100: ")
    n = int(rawUiInput.strip())
    if (n % 2 != 0) or (6 <= n <= 20):
        print("Weird")
    else:
        print('Not Weird')

#!/bin/python3
"""

"""
n = int(input())
if (n % 2 != 0) or (6 <= n <= 20):
    print("Weird")
else:
    print('Not Weird')


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)

(a//b)
(a/b)
# https://app.docusign.com/home

n = int(input())
for i in range(1, (n+1)):
    print(i, end='')

# Better

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)




# Leap Year Finder
def is_leap(year):
    leap = False
    
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# Day 4

class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        self.a = initialAge
        if self.a < 0:
            self.a = 0
            print('Age is not valid, setting age to 0.')
        
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.a < 13:
            print('You are young.')
        elif (13 <= self.a < 18):
            print('You are a teenager.')
        else:
            print('You are old.')
            
    def yearPasses(self):
        # Increment the age of the person in here
            self.a = self.a + 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

# Day 5 Loops

n = int(input().strip())

for i in range(1,11):
    print(n, "x", i,"=", (n*i))
