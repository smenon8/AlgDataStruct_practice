# Divide and Conquer Algorithm for finding the maximum sub array sum
def maxSubArraySum(arr,h,t):
	if h == t:
		return arr[h]
	
	m = (h+t)//2
	
	# 1. find max in left subarray
	leftSum = maxSubArraySum(arr,h,m)
	
	# 2. find max in right subarray
	rightSum = maxSubArraySum(arr,m+1,t)

	# 3. find max in mid-point crossing
	midPointSum = midPointCrossSum(arr,h,m,t)

	return max(leftSum,rightSum,midPointSum)

def midPointCrossSum(arr,h,m,t):
	# Adding the left sub-array from the mid-point to head till the sum is non-decreasing
	sum =  0
	leftSum = arr[m]
	for i in range(m-1,h-1,-1):
		sum += arr[i]
		if sum > leftSum:
			leftSum = sum
	
	# Adding the right sub-array from the mid-point to tail till the sum is non-decreasing
	sum = 0
	rightSum = arr[m+1]
	for i in range(m+2,t+1):
		sum += arr[i]
		if sum > rightSum:
			rightSum = sum


	return leftSum+rightSum

arr = [-2,-5,6,-2,-3,1,5,-6]
print("Maximum Sub Array Sum")
print(maxSubArraySum(arr,0,len(arr)-1))
print()

# Similar problem: Given a sum find the pair of numbers which add upto the sum
def twoSumProblemSort(arr,n):
	arr.sort()

	head = 0
	tail = len(arr)-1
	print(arr)
	while head <= tail:
		s = arr[head] + arr[tail]
		if s == n:
			return arr[head],arr[tail]
		elif s < n:
			head += 1
		else:
			tail -= 1
	
	return False

arr = [6,8,2,3,10,11]
print("Two sum problem")
print(twoSumProblemSort(arr,10))
print()


'''
1. Highly depends on the pivot element i.e. the middle element. 
2. If the middle element is smaller than both its neighbours, it will tend to finding the element in the left sub half
3. Otherwise right half's left part will get pre-dominance.

'''
def findPeakEle(arr,low,high,n):
	mid = (low+high) // 2

	# Handling the boundary cases
	if mid == 0 or mid == n-1: # reached the first or the last element - boundary case
		return arr[mid],mid
	else:
		if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]: # definition of peak element
			return arr[mid],mid
		else:
			if arr[mid] < arr[mid-1]: # peak element will lie to the left
				return findPeakEle(arr,low,mid-1,n)
			else:
				if arr[mid] < arr[mid+1]: # peak element will lie to the right
					return findPeakEle(arr,mid+1,high,n)


arr = [2,20,19,21,23,90,67]
n = len(arr)
print("Find peak element")
print(findPeakEle(arr,0,n-1,n))		
print()