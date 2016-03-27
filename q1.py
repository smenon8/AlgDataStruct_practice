def processArray(array):
	flag = False
	for i in range(0,len(array)):
		if i>0 and i%2 == 0:
			array[i] += array[i-1]
			flag = True
		
		if i>0 and i%3 == 0 and (i+1)<len(array):
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp
			flag = True
			
		if i>0 and i%5 == 0:
			array[i] = array[i] * 2
			flag = True
			
		if (i>0 and i%7==0) or not flag:
			array[i] = array[i] - 1
			
	return array
			