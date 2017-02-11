#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.sort()
while(len(arr) > 0):
	print(len(arr))
	first = arr[0]
	i = 0
	for item in arr:
		if first == item:
			i += 1
		else:
			arr[arr.index(item)] = item - first
	del arr[:i]