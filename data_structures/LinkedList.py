# linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,node):
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def enqueue(self,node):
		if self.head == None:
			self.head = node
		else:
			post = self.head
			while post.next != None:
				post = post.next
			post.next = node

	def printData(self):
		point = self.head
		while point != None:
			print(point.data)
			point = point.next

	def insertAtLoc(self,prevNode,node):
		node.next = prevNode.next
		prevNode.next = node

	def deleteNode(self,key):
		curr = self.head
		if curr.data == key:
			self.head = curr.next
			return
		while(curr.next.data != key):
			curr = curr.next
		curr.next = curr.next.next

	def deleteByPosition(self,position):
		# assuming position goes by 1st, 2nd etc and LL will be indexed from 0
		curr = self.head
		#delete head
		if position == 1:
			self.head = curr.next
			return

		for i in range(2,position-1):
			curr = curr.next

		curr.next = curr.next.next

	def swapNodes(self,key1,key2):
		prev1 = self.head
		curr1 = self.head
		prev2 = self.head
		curr2 = self.head

		while prev1.next.data != key1:
			prev1 = prev1.next
		curr1 = prev1.next

		while prev2.next.data != key2:
			prev2 = prev2.next
		curr2 = prev2.next

		prev1.next = curr2
		prev2.next = curr1
		temp = curr2.next
		curr2.next = curr1.next
		curr1.next = temp
		
	def reverseLinkedList(self):
		curr = self.head
		prev = None
		
		while curr is not None:
			temp = curr.next
			curr.next = prev
			prev = curr
			curr = temp
		self.head = prev
		
def createFreshLL():		
	ll = LinkedList()
	
	for i in range(10,20):
		n = Node(i)
		
		ll.push(n)
		
	
	for i in range(20,30):
		n = Node(i)
		
		ll.enqueue(n)
		
	ll.insertAtLoc(ll.head.next.next,Node(100))
	
	ll.printData()
	
	return ll
	#ll.reverseLinkedList()
	
	#ll.printData()	
	
def oddEvenList(ll):
	curr = ll.head
	i = 0
	while curr is not None:
		i = i+1
		if i == 1: # first time you see an odd node
			odd = curr
			curr = curr.next
		else:
			if i == 2: # first time you see an even node
				even = curr
				evenHead = curr
				curr = curr.next
			else:
				print(i)
				if i % 2 == 1: #odd node
					odd.next = curr
					odd = curr
					curr = curr.next
				else: #even node
					even.next = curr
					even = curr
					curr = curr.next			
		
	odd.next = evenHead
	even.next = None
	
def detectAndRemoveCycles(loopy):
	# detect cycle
	slow = loopy.head
	fast = loopy.head
	
	loopExist = False
	stopCount = 1
	while slow != None or fast != None:
		slow = slow.next
		fast = fast.next.next
		
		if slow == fast:
			loopExist = True
			break
		
		# stop count added in place to stop infinite loops
		stopCount += 1
		
		if stopCount == 100:
			print("Running into infinte loop %d" %stopCount)
			return
			
	if not loopExist:
		return
	
	
	# count the number of elements in the loop
	ptr = fast.next
	count = 1
	while ptr != fast:
		count += 1
		ptr = ptr.next
		
	print("Number of elements in the loop is %d" %count)
	
	ptr = loopy.head
	for i in range(0,count):
		ptr = ptr.next
		
	ptr.next = None
	
	loopy.printData()	

ll = createFreshLL()

ll.reverseLinkedList()
ll.printData()