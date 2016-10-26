## Doubly linked list

class DoubleNode:
	def __init__(self,value):
		self.next = None
		self.prev = None
		self.value = value
		
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		
	def push(self,node):
		#insert first node
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head.prev = node
			self.head = node
		
		print("Push operation success. Inserted %d" %node.value)
			
	def enqueue(self,node):
		curr = self.head
		if self.head == None:
			self.head = node
		else:
			while curr.next != None:
				curr = curr.next
		
			curr.next = node
			node.prev = curr
		
		print("Enqueue operation success. Inserted %d" %node.value)
		
			
	def printData(self):
		curr = self.head
		
		while curr != None:
			print(curr.value)
			curr = curr.next
			
dd = DoublyLinkedList()

for i in range(1,6):
    dd.push(DoubleNode(i))			
	
for i in range(20,26):
    dd.enqueue(DoubleNode(i))

dd.printData()	