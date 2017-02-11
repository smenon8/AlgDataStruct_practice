## function to reverse the given string/char array in place,
## there is no need for a return statement because we are making change directly to the passed list
def reverseString(strArr):
	for i in range(len(strArr)//2):
		temp = strArr[i]
		strArr[i] = strArr[len(strArr)-1-i]
		strArr[len(strArr)-1-i] = temp


strArr = list('a1b2c3d4e5')
print("Before conversion : " + ''.join(strArr) )
reverseString(strArr)
print("After conversion : " + ''.join(strArr) )
print()
# ************************************************************************************************************************

# function to reverse the words, 
# hello world --> world hello
def reverseSentence(wordArr):
	reverseString(wordArr)

wordArr = "hello world the standard first statement in any language".split()
print("Before conversion : " + ' '.join(wordArr) )
reverseSentence(wordArr)
print("After conversion : " + ' '.join(wordArr) )
print()
# ************************************************************************************************************************

# function to reverse order of every word in a sentence 
# also reverse each word in the sentence
def reverseSentenceAndReverseEachWord(wordArr):
	reverseSentence(wordArr)

	for i in range(0,len(wordArr)) :
		wordArr[i] = list(wordArr[i])
		reverseString(wordArr[i])
		wordArr[i] = ''.join(wordArr[i])

wordArr = "hello world the standard first statement in any language".split()
print("Before conversion : " + ' '.join(wordArr) )
reverseSentenceAndReverseEachWord(wordArr)
print("After conversion : " + ' '.join(wordArr) )
print()
# ************************************************************************************************************************

## checking if the given two strings are anagrams of each other
def isAnagramMeth1(strA,strB):
	charMapA = {}
	charMapB = {}

	if len(strA) != len(strB):
		return False

	for i in range(len(strA)):
		charMapA[strA[i]] = charMapA.get(strA[i],0) + 1
		charMapB[strB[i]] = charMapB.get(strB[i],0) + 1

	for key in charMapA.keys():
		if key not in charMapB.keys() or charMapA[key] != charMapB[key]: #makes it O(n^2)
			return False

	return True
print("Is Anagram method 1 using dictionary - most efficient - both space and time")
print(isAnagramMeth1('java','axaj'))
print()

def isAnagramMeth2(strA,strB):
	charCountA = [0]*26 #if strings are only restricted to a single case characters
	charCountB = [0]*26

	if len(strA) != len(strB):
		return False

	for i in range(0,len(strA)):
		indA = ord(strA[i]) - ord('a')
		charCountA[indA] += 1

		indB = ord(strB[i]) - ord('a')
		charCountB[indB] += 1

	for i in range(0,len(charCountA)):
		if charCountA[i] != charCountB[i]:
			return False

	return True

print("Is Anagram method 2 using only lower case letter assumption - efficient - time")
print(isAnagramMeth2('a','b'))	
print()

def isAnagramMeth3(strA,strB):
	charCountA = [0]*256 #if strings are only restricted to ASCII letters
	charCountB = [0]*256

	if len(strA) != len(strB):
		return False

	for i in range(0,len(strA)):
		indA = ord(strA[i]) 
		charCountA[indA] += 1

		indB = ord(strB[i])
		charCountB[indB] += 1

	for i in range(0,len(charCountA)):
		if charCountA[i] != charCountB[i]:
			return False

	return True

print("Is Anagram method 3 using ASCII assumption - efficient - time")
print(isAnagramMeth3('abcdef','fbedca'))
print()
# ************************************************************************************************************************

def findAllPerms(master):
	if len(master) == 0:
		return []

	if len(master) == 1:
		return [master]

	result = []
	for i in range(len(master)):
		curr = master[i]
		remaining = master[:i] + master[i+1:]

		for remPerm in findAllPerms(remaining):
			result.append(curr+remPerm)
	
	return result



print(findAllPerms('abc'))
print()

# ************************************************************************************************************************
# check if given string is a substring of a master string
# Method 1 - assumption of ASCII
def isSubstrMeth1(master,substr):
	charMapMaster = [0]*256
	charMapSub = [0]*256

	if len(master) < len(substr):
		return False
	else:
		for i in range(len(master)):
			ind = ord(master[i])
			charMapMaster[ind] += 1
		for i in range(len(substr)):
			ind = ord(substr[i])
			charMapSub[ind] += 1

		for k in range(256):
			if charMapMaster[k] < charMapSub[k]:
				return False
		return True
print("Check if substring method 1 using ASCII assumption")
print(isSubstrMeth1('hello','xelo'))
print()

# Method 2 - using dictionary
def isSubstrMeth2(master,substr):
	charMapMaster ={}
	charMapSub = {}

	if len(master) < len(substr):
		return False
	else:
		for i in range(len(master)):
			charMapMaster[master[i]] = charMapMaster.get(master[i],0) + 1
		for i in range(len(substr)):
			charMapSub[substr[i]] = charMapSub.get(substr[i],0) + 1
		for key in charMapSub.keys():
			if key not in charMapMaster or charMapSub[key] > charMapMaster[key]: # makes it O(n^2)
				return False
		return True

print("Check if substring using character maps")
print(isSubstrMeth2('hello','elo'))
print()

# ************************************************************************************************************************
def isPalindrome(strng):
	for i in range(len(strng)):
		if strng[i] != strng[len(strng)-1-i]:
			return False
	return True

print("Check if a given string is a palindrome or not")
print(isPalindrome('axxxxxxsssdsdsfdfdsa'))
print()

# ************************************************************************************************************************
# Return a single digit number as a sum 12345 - 15 - 6
def addAllDigits(num):
	#print("Number called with %d" %num)
	if num < 10:
		return num
	else:
		num = str(num)
		sum = 0
		for i in num:
			sum += int(i)
		sum = addAllDigits(sum)
		return sum


print("Add all digits in a number")
print(addAllDigits(1357891))
print()

def addAllDigitsMeth2(num):
	if num < 10:
		return num

	sum = 0
	while num > 10:
		temp = num % 10
		num = num // 10
		sum += temp

	ans = addAllDigits(sum)
	return ans

print("Add all digits in a number")
print(addAllDigits(1357891))
print()

# ************************************************************************************************************************
def ExcelSheetColNum(col):
	if len(col) == 1:
		return ord(col) + 1 - ord('A')
	else:
		return ExcelSheetColNum(col[:len(col)-1]) * 26 + (ord(col[len(col)-1]) + 1 - ord('A'))	

print("Map excel sheet column names to corresponding digits")
print(ExcelSheetColNum('AZA'))

class Stack:
	def __init__(self):
		self.stack = [0]*1000
		self.head = -1
		self.max = float('-inf')

	def push(self,value):
		self.head += 1
		self.stack[self.head] = value
		if value > self.max:
			self.max = value

	def pop(self):
		value = self.stack[self.head]
		self.head -= 1
		return value

	def retMax(self):
		return self.max


s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.retMax())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

# ************************************************************************************************************************
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
# ************************************************************************************************************************















