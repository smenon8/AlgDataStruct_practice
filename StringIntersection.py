def StringIntersect(str1,str2):
	intr = []
	for i in str1:
		if i in str2 and i not in intr:
			intr.append(i)
	
	d = {}
	for i in intr:
		d[i] = min(str1.count(i),str2.count(i))
		
	output = []
	for i in d.keys():
		output.append(i*d[i])
	output.sort()
	return ''.join(output)
	


def CountBit(num):
	count = 0
	while num != 0:
		bit = num%2
		num //= 2
		if bit == 1:
			count += 1
	return count
	
def maxProd(numbers):
	m1 = -1
	m2 = -1
	
	for i in range(len(numbers)):
		if numbers[i] > m2:
			m2 = numbers[i]
			ind2 = i
	
	for j in l[0:ind2]: # the first factor is strictly smaller and occurs before the second number
		if j > m1:
			m1 = j
	
	return m1*m2