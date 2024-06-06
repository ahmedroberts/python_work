#!/bin/python3

import math
import os
import random
import re
import sys

"""

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

"""
A = [1,2,3,4,5,]

def Reverse(myLst):
    return [x for x in reversed(myLst)]

B = Reverse(A)
for _ in B:
    print(_, end=" ")

n = len(A)
print("n:", n)
print('\n*******************\n')
while n > 0:
    print(A[n-1], end=" ")
    n = n-1
    
