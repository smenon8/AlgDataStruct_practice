# the dreaded heap data structure
class Heap:
	def __init__(self):
		self.heap_arr = []
		self.size = 0 # this should how many items the heap currently has

	def get_parent_index(self, child_index):
		return (child_index-1)//2

	def get_left_child_index(self, parent_index):
		idx = 2*parent_index+1
		return idx if idx < self.size else None

	def get_right_child_index(self, parent_index):
		idx =  2*parent_index+2
		return idx if idx < self.size else None

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
		root = self.heap_arr[0]
		self.heap_arr[0] = self.heap_arr[self.size-1]
		self.heap_arr.pop()
		self.size -= 1
		print(self.heap_arr)
		self.heap_down()

	def heap_down(self):
		top_ele_idx = 0
		while top_ele_idx < self.size - 1:
			left_child_idx = self.get_left_child_index(top_ele_idx)
			right_child_idx = self.get_right_child_index(top_ele_idx)
			if (left_child_idx and self.heap_arr[top_ele_idx] > self.heap_arr[left_child_idx]) or (right_child_idx and self.heap_arr[top_ele_idx] > self.heap_arr[right_child_idx] ): # meaning the heap is not in the right order
				swapped_child_idx = left_child_idx if self.heap_arr[left_child_idx] < self.heap_arr[right_child_idx] else right_child_idx
				self.heap_arr[top_ele_idx], self.heap_arr[swapped_child_idx] = self.heap_arr[swapped_child_idx], self.heap_arr[top_ele_idx]
				top_ele_idx = swapped_child_idx
			else:
				break

def __main__():
	myHeap = Heap()

	myHeap.heap_arr = [2,7,12,9,15,13,19,14]
	myHeap.size = 8
	myHeap.remove_root()

	print(myHeap.heap_arr)

if __name__ == "__main__":
	__main__()