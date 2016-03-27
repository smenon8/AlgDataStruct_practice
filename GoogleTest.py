def solution(string):
	line = string.split("\n")
	sum = 0
	num_spaces = -1
	prev = 0
	for i in line:
		line_l = 1
		new_num_spaces = len(i) - len(i.strip(" "))
		if num_spaces > new_num_spaces:
			num_spaces = new_num_spaces
			prev = len(i.strip(" "))
			line_l += prev
		else: 
			if num_spaces == new_num_spaces and ('jpeg' in i or 'gif' in i or 'png' in i):
				line_l -= prev
				prev = len(i.strip(" "))
				line_l += prev
				sum += line_l
			else:
				if num_spaces < new_num_spaces:
					line_l -= prev

		print(sum)
		return sum