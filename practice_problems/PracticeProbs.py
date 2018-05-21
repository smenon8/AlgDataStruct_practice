# vector distance calculator:
def calc_dist_nearest_zero(vct):
	curr_zero = -1
	curr = 0
	dist = [float('inf')]*len(vct)
	while curr < len(vct):
		if vct[curr] == 0:
			curr_zero = curr
			dist[curr_zero] = 0
			curr = curr -1
			while abs(curr - curr_zero) < dist[curr] and curr >= 0:
				dist[curr] = abs(curr - curr_zero)
				curr -= 1
			curr = curr_zero + 1
		else:
			if curr_zero != -1:
				dist[curr] = abs(curr - curr_zero)
			curr += 1

	return dist

def check_isomorphic(str1, str2):
	d = {}

	for i in range(len(str1)):
		if str1[i] in d.keys():
			if d[str1[i]] != str2[i]:
				return False
		else:
			d[str1[i]] = str2[i]

	return True


def huffman_encoding(msg):
    # base case
    if len(msg) == 0:
        return
    prev = None
    enc_msg = []
    count = 1
    for chr in msg:
        if chr == prev:
            count += 1
        else:
            if prev != None:
                enc_msg += [prev, str(count)]
            prev = chr
            count = 1
    enc_msg += [chr, str(count)]
    return ''.join(enc_msg)


def long_non_rep_substr(str):
	dict = {str[0] : 0}
	max_till_now = 1

	for i in range(1,len(str)):
		if dict.get(str[i], None) == None:
			dict[str[i]] = i
			if len(dict.keys()) > max_till_now:
				max_till_now = len(dict.keys())
		else:
			dict = {str[i] : i}
	return max_till_now


def num_primes(n):
	if n < 2:
		return 0
	else:
		visit = [1]*(n+1)

		visit[0] = visit[1] = 0

		for i in range(2,n+1):
			for j in range(i, n+1):
				if i*j <= n:
					visit[i*j] = 0
		return sum(visit)


## Newpassword@yah00

def power_set(inp_set):
	result = [[]]

	for ele in inp_set:
		newSubSets = [subset + [ele] for subset in result]
		result.extend(newSubSets)

	return result 


def power_set2(inp_set, new_set):
	if inp_set == []:
		return [new_set]
	else:
		result = []
		for ele in power_set2(inp_set[1:],new_set + [inp_set[0]]):
			result.append(ele)

		for ele in power_set2(inp_set[1:], new_set):
			result.append(ele)

		return result

def power_set3(inp_set):
	pwr_set_size = 2 ** len(inp_set)
	pwr_set = [[]]

	for i in range(pwr_set_size):
		new_set = []
		for j in range(len(inp_set)):
			if i & (1 << j) : # this is to check if the jth bit is set or not, 2**j will just have 1 bit set at the jth location
				new_set.extend([inp_set[j]])

		pwr_set.append(new_set)
	
	return pwr_set

def zeros_to_end(arr):
	nz_ptr = 0

	for i in range(len(arr)):
		if arr[i] != 0: 
			arr[nz_ptr] = arr[i] # shift all the non-zero element to the front simply
			nz_ptr += 1

	for i in range(nz_ptr, len(arr)): # the nz_ptr is at the last non-zero number, now start filling zeros from there
		arr[i] = 0

	return arr

def zeros_to_end_2(arr):
	head = 0
	tail = len(arr) - 1

	while head < tail:
		if arr[head] == 0:
			while arr[tail] == 0 and head < tail:
				tail -= 1
			if head >= tail:
				break
			arr[head] = arr[tail]
			tail -= 1
		head += 1

	for i in range(tail, len(arr)):
		arr[i] = 0

	return arr


def find_missing_num(arr, N):
	xor1 = arr[0]
	for i in range(1, len(arr)):
		xor1 = xor1 ^ arr[i]

	xor2 = 1
	for i in range(2, N+1):
		xor2 = xor2 ^ i

	return xor1 ^ xor2

'''
logic : if 2 numbers are missing, the average of the number is going to be the key to finding those numbers
 	of the two numbers one of the number is always going to be smaller than and other number is going to be greater than the avg
 '''
def find_2_missing_num(arr, n):
	nat_sum_n = n*(n+1)/2
	arr_sum = sum(arr)

	sum_missing = nat_sum_n - arr_sum
	avg_missing = sum_missing // 2

	nat_sum_1_avg = avg_missing * (avg_missing+1)/2
	nat_sum_avg_n = nat_sum_n - nat_sum_1_avg

	sum_arr_to_avg = sum_arr_from_avg = 0
	for i in arr:
		if i <= avg_missing:
			sum_arr_to_avg += i

		if i > avg_missing:
			sum_arr_from_avg += i

	return (nat_sum_1_avg- sum_arr_to_avg, nat_sum_avg_n - sum_arr_from_avg)


def two_pair_sum(arr, n):
	dct = {n - arr[i] : arr[i] for i in range(len(arr))}
	results = []
	for i in range(len(arr)):
		if arr[i] in dct.keys():
			results.append((arr[i], dct[arr[i]]))

	return results

def find_num_paths(arr_2D, i, j):
	# i,j is the start point and you have to travel all the way back to 0,0
	if i == j and i == 0:
		return 1

	if i < 0 or j < 0 or arr_2D[i][j] == 0: # out of range or no path from that point
		return 0

	if arr_2D[i][j] == 1:
		return find_num_paths(arr_2D, i, j-1) + find_num_paths(arr_2D, i-1, j) + find_num_paths(arr_2D, i-1, j-1) 

'''
Given a sorted array of integers, using the same array, shuffle the integers to have unique elements and return the index. 

Sample input : [3, 3, 4, 5, 5, 6, 7, 7, 7] 
Sample output : [3, 4, 5, 6, 7, X, X, X, X] 
In this case, it returns an index of 4. 
The elements in the array after that index is negligible (don't care what value it is).

'''
def max_index_uniq_arr(arr):
	# using the concept of lazy index
	j = 0
	for i in range(1,len(arr)):
		if arr[i] != arr[i-1]:
			j += 1

	return j

def longest_run(strng):
	start = end = l_start = l_end = 0
	for i in range(1,len(strng)):
		if strng[i-1] == strng[i]:
			end = i
			if end - start > l_end - l_start:
				l_start = start
				l_end = end
		else:
			start = end = i

	return ''.join(strng[l_start:l_end+1])

def get_max_index(arr):
	max_idx = 0
	for i in range(1, len(arr)):
		if arr[max_idx] < arr[i]:
			max_idx = i

	return max_idx

def top_k_ele(arr, k):
	temp = arr[:k]
	for i in range(k):
		max_idx = get_max_index(temp)

		for j in range(k, len(arr)):
			if temp[max_idx] > arr[j]:
				temp[max_idx] = arr[j]
				print(temp)
				break
	return temp

'''
Logic : Until the second number becomes negative keep doubling the first number and halving the second number.
If the second number becomes odd - then simply add the result with first number
'''
def russian_peasant(a, b): # returns a*b, assumes that a and b are both positive
	result = 0

	while b > 0:
		if b & 1:
			result += a

		a  = a << 1
		b = b >> 1

	return result

'''
Logic:
	Logic is smae as counting number of sqaures. Count the number of squares in half the grid and multiply by 2
	If the halved quantity(smaller) is odd then the answer is exactly twice, if odd then you have to add an additional bigger
'''
def _product(smaller, bigger):
	if smaller == 0: 
		return 0
	if smaller == 1:
		return bigger

	s = smaller >> 1 # dividing by 2, can also write smaller // 2
	half = _product(s, bigger) # count the number of squares in the half grid
	if smaller & 1: # smaller is odd
		return half + half + bigger
	else:
		return half + half


def product(a,b):
	smaller = a if a < b else b
	bigger = a if a > b else b

	return _product(smaller, bigger)

'''
Logic - Think in terms of histogram:
Find the tallest tower before the current price - h(i)
Span = i - h(i)

How to store h(i): stack - keep popping the stack until you find that spike, once you find it span = i - top_of_stack
Then push the i. 
Extremely smart! 
'''
def stock_span_eff(stock_prices):
	n = len(stock_prices)

	stack = [0]
	span = [1] * n

	for i in range(1, n):
		while len(stack) != 0 and stock_prices[stack[len(stack)-1]] <= stock_prices[i]:
			stack.pop()

		if len(stack) == 0:
			span[i] = i+1
		else:
			span[i] = i - stack[0]

		stack.append(i)

	return span


# For every element check the difference with the minimum element so far..! 
def stock_buy_once_sell_once(stock_prices):
	min_ele_so_far = stock_prices[0]
	max_diff = 0

	for i in range(1, len(stock_prices)):
		if stock_prices[i] - min_ele_so_far > max_diff:
			max_diff = stock_prices[i] - min_ele_so_far

		if min_ele_so_far > stock_prices[i]:
			min_ele_so_far = stock_prices[i]

	return max_diff

# the logic is to find the point where prices are falling, you sell just before the prices fall. Then reset the entire system.
def stock_buy_mul_sell_mul(stock_prices):
	profit_so_far = lcl_min = 0
	buy_sell_tups = []

	curr = 1
	while curr < len(stock_prices):
		if stock_prices[curr] - stock_prices[lcl_min] > profit_so_far:
			profit_so_far = stock_prices[curr] - stock_prices[lcl_min] 
		else:
			if lcl_min != curr-1:
				buy_sell_tups.append((lcl_min, curr-1))
			lcl_min = curr
			profit_so_far = 0
		curr += 1

	if lcl_min < len(stock_prices) and lcl_min != len(stock_prices)-1:
		buy_sell_tups.append((lcl_min, len(stock_prices)-1))

	return buy_sell_tups

def moving_average_window(arr, m):
	if m > len(arr):
		return "Not defined"

	head = 0
	tail = m-1
	first_result = 0
	for i in range(head, tail+1):
		first_result += arr[i]

	result = [first_result]

	curr = 0
	while tail <= len(arr) -2:
		tail += 1
		next_item = result[curr] - arr[head] + arr[tail]
		result.append(next_item)
		head += 1
		curr += 1

	for i in range(len(result)):
		result[i] = result[i] / m

	return result


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, x1, y1, x2, y2):
		self.slope = (y2-y1)/(x2-x1)
		self.intercept = y1 - self.slope * y1
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2


def get_intersection(line1, line2):
	if line1.slope == line2.slope2: # parallel lines
		if line1.intercept == line2.intercept: # same line
			line_overlaps = check_line_overlap(line1, line2)
			if line_overlaps:
				return line_overlaps
			else:
				return "No common point between the two lines"
		else:
			return "Parallel lines"

	else: # non-parallel lines
		x = (line2.intercept - line1.intercept) / (line1.slope - line2.slope)
		y = line1.slope * x + line1.intercept

		P = Point(x, y)

		if point_in_line(p, l1) or point_in_line(p, l2):
			return p
		else:
			return "intersection point lies out of the segment range"


def point_in_line(p, line):
	smaller_x = min(line.x1, line.x2)
	bigger_x = max(line.x1, line.x2)
	smaller_y = min(line.y1, line.y2)
	bigger_y = max(line.y1, line.y2)

	if p.x > smaller_x and p.x < bigger_x and p.y > smaller_y and p.y < bigger_y:
		return True

	return False

def check_line_overlaps(line1, line2):
	if point_in_line(Point(line1.x1, line1.y1), line2):
		return Point(line1.x1, line1.y1)

	if point_in_line(Point(line1.x2, line1.y2), line2):
		return Point(line1.x2, line1.y2)

	if point_in_line(Point(line2.x1, line2.y1), line1):
		return Point(line2.x1, line2.y1)

	if point_in_line(Point(line2.x2, line2.y2), line1):
		return Point(line2.x2, line2.y2)

	return False


# the logic is to sort the two arraya to have a sense of what lies ahead of you. 
def min_difference_2_arrs(arr1, arr2):
	arr1.sort()
	arr2.sort()

	ptr1 = ptr2 = 0
	min_diff = float("inf")
	while ptr1 < len(arr1) and ptr2 < len(arr2):
		if min_diff > abs(arr1[ptr1] - arr2[ptr2]):
			min_diff = abs(arr1[ptr1] - arr2[ptr2])

		if arr1[ptr1] < arr2[ptr2]:
			ptr1 += 1
		else:
			ptr2 += 1

	return min_diff


print(power_set([1,2,3]))
print(power_set2([1,2,3], []))
print(power_set3([1,2,3]))

print(zeros_to_end([1,3,0,8,12,0,4,7,0,0,0,0,9,12,14,15,0,0]))

print(find_missing_num([1,2,4,5,6],6))


print("Find missing paths")
arr_2D = [[1,1],[1,1]]
print(find_num_paths(arr_2D, 1, 1))

arr = [3, 3, 4, 5, 5, 6, 7, 7, 7] 
print(max_index_uniq_arr(arr))