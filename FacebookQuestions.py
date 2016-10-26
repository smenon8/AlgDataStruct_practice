## Dividing two numbers without actually having to divide it - time complexity
def divide(nr,dr):
	dividend = 0
	while nr >= dr:
		nr -= dr
		dividend += 1

	return dividend

#print(divide(21,3))

## Given a tree, where the parent has any number of nodes and each node has a number, return the average of all the nodes on each level in an array. 


## Given a sum, find out which numbers in the array add up to the sum
def twoSumProbHashMapMeth(arr,sum):
	valMap = {}

	for ele in arr:
		valMap[ele] = sum - ele

	for ele in valMap.keys():
		if valMap[ele] in valMap.keys():
			print(ele)
			
def twoSumProbSortMeth(arr,sum):
	arr.sort()

	head = 0
	tail = len(arr) - 1

	while head <= tail:
		ans = arr[head] + arr[tail]
		if ans < sum:
			head += 1
		elif ans > sum:
			tail -= 1
		else:
			head += 1
			tail -= 1
			print(arr[head],arr[tail])

arr = [1,2,3,4,5,6,7,8,9,11,14,56]
twoSumProbHashMapMeth(arr,20)
twoSumProbSortMeth(arr,20)

## Given an integer x and an array y, create a function that returns true if x exists as a sum of any contiguous elements in y. 
def contiguousSum(arrY,intX):
	for i in range(0,len(arrY)-1):
		if arrY[i] + arrY[i+1] == intX:
			return True

	return False

print(contiguousSum(arr,8))
print()

## Write a program that takes an input an array of positive numbers and shifts all the zeros (0s) to the right.
def shiftZeroToRight(arr,start,end):
	zeroPtr = start
	nonZeroPtr = end - 1
	
	if start >= end or start == len(arr) - 1:
		return

	print("*******")
	print(arr[zeroPtr:nonZeroPtr])

	while arr[zeroPtr] != 0:
		zeroPtr += 1
	
	while arr[nonZeroPtr] == 0:
		nonZeroPtr -= 1

	# Swap zero pointer and non-zero pointer
	temp = arr[zeroPtr]
	arr[zeroPtr] = arr[nonZeroPtr]
	arr[nonZeroPtr] = 0
	print(arr[zeroPtr],arr[nonZeroPtr])
	shiftZeroToRight(arr,zeroPtr+1,nonZeroPtr)

def shiftZeroToRightIter(arr):
	countNonZero = 0

	for i in range(len(arr)):
		if arr[i] != 0:
			arr[countNonZero] = arr[i]
			countNonZero += 1

	while countNonZero < len(arr):
		arr[countNonZero] = 0
		countNonZero += 1

myArr = [1,0,0,8,0,0,0,7,0,0,0,0,19,8,9,0]
print(len(myArr))
shiftZeroToRightIter(myArr)
print(myArr)

## Given a number n, find the largest number just smaller than   n that can be formed using the same digits as n. 
def nextSmallest(num):
	bucket = [0]*10

	numS = str(num)
	for i in range(len(numS)-1,-1,-1):
		digit = int(numS[i])

		bucket[digit] += 1

		for j in range(len(numS)-1,digit,-1):
			if bucket[j] != 0:
				indexReplace = j
				break
