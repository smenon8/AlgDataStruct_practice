# HACKER RANK - https://www.hackerrank.com/challenges/2d-array/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def getTopWindow(a, i, j):
    return a[i][j] + a[i][j+1] + a[i][j+2]

def getMidWindow(a, i, j):
    return a[i+1][j+1]

def getBottomWindow(a, i, j):
    return getTopWindow(a, i+2,j)

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    sums = []
    for i in range(0,4):
        for j in range(0,4):
            sums.append(getTopWindow(arr, i, j) + getMidWindow(arr, i, j) + getBottomWindow(arr, i, j))
            
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

