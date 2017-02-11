# static linked list

class StaticNode:
	def __init__(self,value):
		self.next = -1
		self.value = value
	
class StaticLinkedList:
	def __init__(self,numNodes):
		self.head = -2
		self.array = [Node(-1)]*numNodes
	def push(self,node):
		if self.head == -2:
			self.head = 0
			node.next = 1
		else:
			curr = head
			while self.array[curr].next != -1:
				curr = self.array[curr].next + 1
			self.array[curr].next = curr + 1