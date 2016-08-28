# python-3
# Author : Sreejith Menon
# Singly Linked List API

class Node:
	def __init__(self,value):
		self.next = None
		self.value = value

	def __str__(self):
		return str(self.value)

class List:
	def __init__(self,tailExist = False):
		self.head = None
		self.tailExist = tailExist
		if self.tailExist:
			self.tail = None

	def __str__(self):
		return str(self.__dict__)

	# Run time complexity: O(1)
	def pushFront(self,ele):
		if self.head == None: # No element yet in the list 
			self.head = ele
		else: # There is atleast 1 element
			ele.next = self.head
			self.head = ele

	# Run time complexity: O(1)
	def popFront(self):
		if self.head == None:
			return "List Empty"
		else:
			popNode = self.head
			self.head = popNode.next
			return popNode 

	# Run time complexity : O(n)
	def walkList(self):
		if self.head == None:
			print("List Empty")
		else:
			curr = self.head
			while curr != None:
				print(curr,end = " ")
				curr = curr.next
			print()

	# Run time complexity: O(1)
	def isListEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	# Run time complexity: O(n)
	# Best case: element is the head element : O(1)
	# Worst case: element is the tail element: O(n)
	def searchEle(self,value):
		if self.head == None:
			print("List Empty")
			return None
		else:
			curr = self.head
			while curr != None:
				if curr.value == value:
					return True
				curr = curr.next
			return False

	# Run time complexity: O(n) - without tail
	def pushBack(self,ele):
		if self.head == None: # empty list
			self.head = ele
		else:
			curr = self.head
			while curr.next != None:
				curr = curr.next
			curr.next = ele

	# Run time complexity: O(n) - without tail
	def popBack(self):
		if self.head == None:
			return "List Empty"
		else:
			prevNode = self.head
			while prevNode.next.next != None:
				prevNode = prevNode.next
			popNode = prevNode.next
			prevNode.next = None
			return popNode

	def eraseEle(self,value):
		if self.head == None:
			return "List Empty"
		else:
			if self.searchEle(value):
				curr = self.head
				prev = self.head
				if curr.value == value: # head is to be deleted
					return self.popFront()
				else:
					while curr.value != value and curr != None:
						prev = curr
						curr = curr.next
					prev.next = curr.next
					return curr
			else:
				return "Element not found"

	def insertAtN(self,ele,n):
		if self.head == None:
			self.head = ele
		else:
			currPos = 0
			curr = self.head
			prev = self.head

			while curr != None and currPos < n:
				prev = curr
				curr = curr.next
				currPos += 1

			ele.next = curr
			prev.next = ele

	def printReverse(self):
		if self.head == None:
        	return 
    	else:
        	ReversePrint(self.head.next)
        	print(head.data)


l = List()
print(l.isListEmpty())
l.pushFront(Node(5))
l.walkList()
l.popFront()
l.walkList()
l.pushFront(Node(6))
l.pushFront(Node(7))
l.pushFront(Node(8))
l.pushFront(Node(9))
l.pushFront(Node(1))
print(l.isListEmpty())
l.walkList()
print(l.popFront())
l.walkList()
print(l.searchEle(5))
print(l.searchEle(19))
print("-*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*-")
l = List(True)
print(l.isListEmpty())
l.pushFront(Node(5))
l.pushFront(Node(6))
l.pushFront(Node(7))
l.pushFront(Node(8))
l.pushFront(Node(9))
l.pushFront(Node(1))
l.walkList()
l.pushBack(Node(99))
l.pushBack(Node(98))
l.walkList()
print(l.popBack())
l.walkList()
print(l.eraseEle(7))
l.walkList()
print(l.eraseEle(1))
l.walkList()
print(l.eraseEle(99))
l.walkList()
print("-*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*-")
l = List()
l.insertAtN(Node(3),0)
l.walkList()
l.insertAtN(Node(5),1)
l.walkList()
l.insertAtN(Node(4),2)
l.walkList()
l.insertAtN(Node(2),4)
l.walkList()
l.insertAtN(Node(10),1)
l.walkList()
