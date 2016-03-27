import sys
# Problem 1.1
def isUniqueString(stringVar):
	if len(stringVar) > 256:
		return False

	charSet = [True] * 256

	for i in stringVar:
		if charSet[ord(i)]:
			charSet[ord(i)] = False
		else:
			return False

	return True

# Problem 1.3 or check if the given two strings are anagrams of each other
def isFirstPermSecond(strA,strB):
	if len(strA) != len(strB):
		return False
	charMapA = {}
	charMapB = {}
	for i in range(len(strA)):
		charMapA[strA[i]] = charMapA.get(strA[i],0) + 1
		charMapB[strB[i]] = charMapB.get(strB[i],0) + 1

	for key in charMapA.keys():
		if key not in charMapB.keys():
			return False

		if charMapA[key] != charMapB[key]:
			return False

	return True

# Problem 1.5
def compressString(strVar):
	compressed = []
	prev = strVar[0]
	count = 1

	for i in range(1,len(strVar)):
		if strVar[i] == prev: # find a match
			count += 1
		else:
			compressed.append(prev + str(count))
			count = 1
			prev = strVar[i]

	compressed.append(prev + str(count))	# the last part was never getting appended	

	if len(compressed) >= len(strVar):
		return strVar

	return ''.join(compressed)


def getFirstNonRepeatedCharacter(strVar):
	charMap = {}
	for char in strVar:
		charMap[char] = charMap.get(char,0) + 1

	for char in strVar:
		if charMap[char] == 1:
			return char

	return None # if every character repeats


def getFirstRepeatedCharacter(strVar):
	charMap = {}
	for char in strVar:
		charMap[char] = charMap.get(char,0) + 1

	for char in strVar:
		if charMap[char] > 1:
			return char

	return None # if every character is unique

# check if the string given is purely a number
import re
def isStrNum(strVar):
	ans = re.findall(r'^\d\d+\d$',strVar)

	if len(ans) == 1:
		return True
	else:
		return False

def findAndReplace(strVar,find,replace):
	strVar = list(strVar)

	for i in range(len(strVar)):
		if strVar[i] == find:
			strVar[i] = replace

	return ''.join(strVar)

# finding all permutations of a string
def findingPerm(word):
	if len(word) == 0:
		return []
	else:
		if len(word) == 1:
			return [word]
		else:
			result = []
			for i in range(len(word)):
				curr = word[i]
				rem = word[:i] + word[i+1:]
				for j in findingPerm(rem):
					result.append(curr+j)
			return result

# check if a given string is a palindrome or not
def isPalindrome(word):
	for i in range(len(word)//2):
		if word[i] != word[len(word)-1-i]:
			return False
	return True

def cleanup():
	print("Testing the clean up function")

def mergeSortedArrWithAux(arr1,arr2):
	headA = headB = 0
	result = []
	while headA < len(arr1) and headB < len(arr2): 		
		if arr1[headA] < arr2[headB]:
			result.append(arr1[headA])
			headA += 1
		else:
			result.append(arr2[headB])
			headB += 1
	if headA < len(arr1):
		result.extend(arr1[headA:])
	else:
		result.extend(arr2[headB:])  

	return result

def mergeSortedArrWOAux(arr1,arr2):
	#arr1 is the bigger array

	j = len(arr1)-1

	# shift all the None spaces to the left end using two pointers
	for i in range(len(arr1)-1,-1,-1):
		if arr1[i] != None:
			arr1[j] = arr1[i]
			j -= 1

	arr1Start = len(arr1) - len(arr2) -1
	arr2Start = 0

	# Logic for merging the n size array and the m+n array
	i = 0
	while arr1Start < len(arr1) and arr2Start < len(arr2):
		if arr1[arr1Start] < arr2[arr2Start]:
			arr1[i] = arr1[arr1Start]
			arr1Start += 1
		else:
			arr2[i] = arr2[arr2Start]
			arr2Start += 1
		i += 1

	# if any elements remain, append that to the end of the array
	while arr2Start < len(arr2):
		arr1[i] = arr2[arr2Start]
		i += 1
		arr2Start += 1

def detFullHousePoker(handArr):
	# A is 0, J is 10, Q is 11 and K is 12
	countArr = [0]*13

	for card in handArr:
		countArr[card] += 1

	threePair = False
	twoPair = False
	for i in countArr:
		if i == 3:
			threePair = True
		if i == 2:
			twoPair = True

	if threePair and twoPair:
		print("Full House!")
	else:
		print("You lose!")


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

cardsInHand = [1,1,12,12,12]
detFullHousePoker(cardsInHand)

a = [None,1,None,2,3,None,4]
b = [6,7,8]
print("Merging two sorted arrays without use of Auxillary space")
mergeSortedArrWOAux(a,b)
print(a)

print("Merging two sorted arrays with use of Auxillary space")
res = mergeSortedArrWithAux([1,3,5,7,9],[2,4,6,8,10,12,14,16,18])
print(res)
#sys.stdout = open("output.dat",'w')

sys.exitfunc = cleanup
sys.stdout = sys.__stdout__


print("isPalindrome('java') : " + str(isPalindrome('java')))

print("findingPerm('abc') : ")
print(findingPerm('abc'))

print("getFirstNonRepeatedCharacter('aafffagayhjayghj') : " + str(getFirstNonRepeatedCharacter('aafffagayhjayghj')))

print("getFirstRepeatedCharacter('xafffagayhjayghj') : " + str(getFirstRepeatedCharacter('xafffagayhjayghj')))

print("compressString('aaaaabbbadadadbbbbbccccaaaabbbbb') : " + compressString('aaaaabbbadadadbbbbbccccaaaabbbbb'))

print("isUniqueString('abcdaefgh') : " + str(isUniqueString('abcdaefgh')))

print("isFirstPermSecond('abcd','daac') : " + str(isFirstPermSecond('abcd','dabc')))

print(findAndReplace("Python is the best programming language ever"," ","%20"))

sys.stdout.close()
sys.exit()