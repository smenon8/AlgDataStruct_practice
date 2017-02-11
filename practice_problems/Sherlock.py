#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    flag = False
    if n%3 == 0:
        print('5'*n)
        flag = True
    else:
        rem = n
        while rem >= 3:
            if rem%3 == 0:
                print('5'*rem+'3'*(n-rem))
                flag = True
                break
            else:
                rem -= 5
    
    if flag == False:
        if n%5 == 0:
            print('3'*n)
            flag = True
        else:
            print('-1')