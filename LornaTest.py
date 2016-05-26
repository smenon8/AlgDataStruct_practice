def findMaxNumberAlphabeticallyIncreasingSubstring(exStr):
	if len(exStr) == 0:
		return 0
	elif len(exStr) == 1:
		return 1
	curr = 0
	count = 1
	substrLenArr = []
	
	while curr < len(exStr) - 1:
		if ord(exStr[curr]) < ord(exStr[curr+1]):
			count += 1
			#print(exStr[curr],count)
		else:
			if count != 1:
				substrLenArr.append(count)
			count = 1
		print(substrLenArr)
		curr += 1
	
	if count != 1:
		substrLenArr.append(count)
	print(substrLenArr)

	
	count = 1
	maxEle = substrLenArr[0]

	for i in range(1,len(substrLenArr)):
		if substrLenArr[i] > maxEle:
			count += 1
			maxEle = substrLenArr[i]

	return count

import re

def isMergeable(input,part1,part2):
	if len(part1) + len(part2) != len(input):
		return -1

	part1Dict = {}
	part2Dict = {}
	inputDict = {}

	for char in input:
		inputDict[char] = inputDict.get(char,0) + 1

	for char in part1:
		part1Dict[char] = part1Dict.get(char,0) + 1

	for char in part2:
		part2Dict[char] = part2Dict.get(char,0) + 1

	for key in inputDict.keys():
		#if inputDict[key] != part1Dict.get(key,0) or inputDict[key] != part2Dict.get(key,0):
		if key not in part1Dict.keys() and  key not in part2Dict.keys():
			return -1

		if inputDict[key] != part1Dict.get(key,0) + part2Dict.get(key,0):
			return -1

	# find all occurences of each character
	for i in range(len(part1)):
		pos = [m.start() for m in re.finditer(part1[i], input)]
		for j in range(i,len(part1)):
			for k in pos:
				if input.index(part1[j]) < k:
					flag = True
				if not flag:
					return -1
			# if input.index(part1[i]) > input.index(part1[j]):
			# 	return -1

	for i in range(len(part2)):
		pos = [m.start() for m in re.finditer(part2[i], input)]
		for j in range(i,len(part2)):
			for k in pos:
				if input.index(part2[j]) < k:
					flag = True
				if not flag:
					return -1
			# if input.index(part2[i]) > input.index(part2[j]):
			# 	return -1

	return 1


print(isMergeable('helloworld','hewodr','llol'))
print(isMergeable('zappos','zps','apo'))
print(isMergeable('analog','alg','ano'))
print(isMergeable('aaaba','aba','aa'))