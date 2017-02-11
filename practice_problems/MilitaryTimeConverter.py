#!/bin/python3

import sys


time = input().strip()

l = time.split(':')

if 'PM' in l[2] and l[0] != '12':
    l[0] = str(int(l[0]) + 12)
    l[2] = l[2].replace('PM','')
else:
    if 'AM' in l[2] and l[0] != '12':
        l[2] = l[2].replace('AM','')

if l[0] == '12' and 'AM' in l[2]:
	l[0] = '00'
	l[2] = l[2].replace('AM','')
else:
	l[2] = l[2].replace('PM','')
		
print(':'.join(l))