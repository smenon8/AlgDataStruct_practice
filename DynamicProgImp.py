# LCS using dynamic programming recursive method
def lcsRecursion(seq1,seq2,m,n):
	if m == 0 or n == 0:
		return 0
	else:
		if seq1[m-1] == seq2[n-1]:
			return 1 + lcsRecursion(seq1,seq2,m-1,n-1)
		else:
			return (max(lcsRecursion(seq1,seq2,m-1,n),lcsRecursion(seq1,seq2,m,n-1)))
			
seq1 = ['a','c','t','g','g','a','c','t','a']	
seq2 = ['g','c','t','g','g','a','c','t','a']		

print(lcsRecursion(seq1,seq2,len(seq1),len(seq2)))

def LCSIter(strA,strB):
	memoArr = [[None for j in range(len(strB)+1)] for i in range(len(strA)+1)]

	for i in range(len(strA)+1):
		memoArr[i][0] = 0

	for j in range(len(strB)+1):
		memoArr[0][j] = 0
	
	for i in range(1,len(strA)+1):
		for j in range(1,len(strB)+1):
			if strA[i-1] == strB[j-1]:
				memoArr[i][j] = 1+ memoArr[i-1][j-1]
			else:
				memoArr[i][j] = max(memoArr[i-1][j],memoArr[i][j-1])

	return memoArr[len(strA)][len(strB)]

print(LCSIter(seq1,seq2))


# Longest increasing subsequence, the iterative version.
# Logic - base case - what is LIS('a')? 
# Init a result array initialized to 1, then 
# for each element i, start from all indexes below i and check if they are lower than arr[i]
# Now check adding that element(j) in the sequence does any good? i.e. res[j] + 1 > res[i] 
def LISIter(arr):
    n = len(arr)
    result = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and result[j] + 1 > result[i]:
                result[i] = result[j] + 1
    return max(result)

print(LISIter([10, 22, 9, 33, 21, 50, 41, 60]))

def MaxSumIncrIter(arr):
    n = len(arr)
    result = [1] * n
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j] and result[j] + arr[i] > result[i]:
                result[i] = result[j] + arr[i]
    return max(result)

print(MaxSumIncrIter([1, 101, 2, 3, 100, 4, 5]))

# rows are your coins and columns is 0..V
def coinChngAllWaysIter(V,C):
	memo = [[0 for j in range(V+1)] for i in range(len(C)+1)]

	for i in range(len(C)+1):
		memo[i][0] = 1
	for j in range(1,V+1):
		memo[0][i] = 0

	# if value of coin is greater than the current value at hand, then simply copy from the top
	# otherwise, number of ways = ways having coin i (value = j - C[i]) + ways without coin i (value = j)
	for i in range(1,len(C)+1):
		for j in range(1,V+1):
			if C[i-1] <= j:
				memo[i][j] = memo[i][j-C[i-1]] + memo[i-1][j]
			else:
				memo[i][j] = memo[i-1][j]

	return memo[len(C)][V]

print(coinChngAllWaysIter(4,[1,2,3]))

def minWaysCoinChng(V,C):
	memoTab = [None] * (V+1)

	if V == 0:
		return 0
	else:
		memoTab[0]  = 0
		for i in range(1,V+1):
			memoTab[i] = float("inf")

		for i in range(1,V+1):
			for j in range(len(C)):
				if i >= C[j]:
					memoTab[i] = min(memoTab[i],memoTab[i-C[j]] + 1)
		return memoTab[V]

print(minWaysCoinChng(11,[9,6,5,1]))