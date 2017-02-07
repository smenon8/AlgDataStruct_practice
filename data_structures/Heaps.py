# the dreaded heap data structure
class Heap:
	def __init__(self):
		self.heap_arr = []
		self.size = 0 # this should how many items the heap currently has

	def get_parent_index(self, child_index):
		return (child_index-1)//2

	def get_left_child_index(self, parent_index):
		return 2*parent_index+1

	def get_right_child_index(self, parent_index):
		return 2*parent_index+2

	def insert_new_element(self, new_ele):
		self.heap_arr.append(new_ele)
		self.size += 1
		self.heap_up()

	def heap_up(self):
		last_ele_index = self.size - 1

		while last_ele_index >= 0:
			parent_index = self.get_parent_index(last_ele_index)

			if self.heap_arr[parent_index] > self.heap_arr[last_ele_index]: # this means that the min-heap property is not maintained
				self.heap_arr[parent_index], self.heap_arr[last_ele_index] = self.heap_arr[last_ele_index], self.heap_arr[parent_index] # swap the elements
				last_ele_index = parent_index
			else: # the heap property is maintained, no need to check for further parents
				break

	def remove_root(self):
		pass

	def heap_down(self):
		pass

def __main__():
	myHeap = Heap()

	myHeap.heap_arr = [2,7,12,9,15,13,19,14]
	myHeap.size = 8
	myHeap.insert_new_element(3)

	print(myHeap.heap_arr)

if __name__ == "__main__":
	__main__()