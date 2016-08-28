from math import floor

def binSearch(a,ele):
	mid = len(a) // 2
	# base case : only 1 element in the array
	if mid == 0 and a[mid] != ele:
		return "Element not found"
	if a[mid] == ele:
		return "Element found"
	elif a[mid] > ele: # element in the left sub-array
		return binSearch(a[:mid],ele)
	else:
		return binSearch(a[mid+1:],ele)
	
def modBinSearch(a,left,right,ele):
	mid = (left + right) // 2
	
	if right < left: # alternate condition that seems to work mid > right or mid < left
		return "Element not found"

	if a[mid] == ele:
		return "Element found at %d" %mid
	elif a[mid] > ele:
		return modBinSearch(a,left,mid-1,ele)
	else:
		return modBinSearch(a,mid+1,right,ele)

def iterBinSearch(a,ele):
	left = 0
	right = len(a)

	while left <= right:
		mid = (left+right) // 2
		if a[mid] == ele:
			return "Element found at %d" %mid
		elif a[mid] > ele:
			right = mid - 1
		else:
			left = mid + 1

	return "Element not found"

def selectionSort(a):
	if len(a) <= 1:
		return a
	for i in range(len(a)):
		minEleIdx = i
		for j in range(i+1,len(a)):
			if a[minEleIdx] > a[j]:
				minEleIdx = j

		# swap a[i] with minEle
		a[i],a[minEleIdx] = a[minEleIdx],a[i]

	return a

# The largest element bubbles down after each iteration
def bubbleSort(a):
	if len(a) <= 1:
		return a

	for i in range(0,len(a)):
		for j in range(0,len(a)-1-i):
			if a[j] > a[j+1]:
				a[j],a[j+1] = a[j+1],a[j]
	return a

def insertionSort(a):
	if len(a) <= 1:
		return a

	for i in range(1,len(a)):
		j = i- 1
		while j >= 0 and a[j] > a[j+1]:
			a[j],a[j+1] = a[j+1],a[j]
			j -= 1

	return a

def merge(a,b):
	# special cases:
	if len(a) == 0 or len(b) == 0: 
		return a + b
	elif a[-1] < b[0]: # all elements of a is less than b
		return a + b
	elif b[-1] < a[0]:
		return b + a
	else:
		aux = []
		l = r = 0
		while l < len(a) and r < len(b):
			if a[l] < b[r]:
				aux.append(a[l])
				l += 1
			else:
				aux.append(b[r])
				r += 1
		if l < len(a): # there are elements left in a
			aux += a[l:]
		elif r < len(b):
			aux += b[r:]

		return aux

def mergeSort(a,n):
	if len(a) <= 1:
		return a

	mid = len(a) // 2
	l = mergeSort(a[:mid],mid)
	r = mergeSort(a[mid:],len(a)-mid)
	return merge(l,r)

def __main__():
	a = [1,2,3,4,5,6,7,8]
	print(modBinSearch(a,0,7,-1))
	print(iterBinSearch(a,-1))

	b = [64, 90, 25, 12, 22, 11, 34]
	#print(selectionSort(b))
	print(mergeSort(b,len(b)))

if __name__ == "__main__":
	__main__()
