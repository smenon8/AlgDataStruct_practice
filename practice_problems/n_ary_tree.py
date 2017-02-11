class NodeT:
	def __init__(self,key,numChild):
		self.key = key
		self.children = [None]*numChild

class n_aryTree:
	def __init__(self):
		self.root = None

class Queue:
	def __init__(self):
		self.queue = []
		self.head = self.tail = 0

	def enqueue(self,val):
		self.queue.append(val)
		self.tail += 1

	def dequeue(self):
		val = self.queue[self.head]
		self.head += 1
		return val

	def isEmpty(self):
		if self.head == self.tail:
			return True
		else:
			return False

	def length(self):
		return self.tail - self.head

def levelOrderTraversal(root):
	q = Queue()
	q.enqueue(root)
	if root == None:
		return None
	while q.head != q.tail:
		root = q.dequeue()
		print(root.key)
	
		for i in root.children:
			if i != None:
				q.enqueue(i) 

## Given a tree, where the parent has any number of nodes and each node has a number, 
## return the average of all the nodes on each level in an array. 
def averageValPerLevel(root):
	q = Queue()

	if root == None:
		return None

	q.enqueue(root)

	while not q.isEmpty():
		level = q.length()
		sum = 0
		count = 0
		while level != 0:
			curr = q.dequeue()
			sum += curr.key
			count += 1
			level -= 1
			
			for i in curr.children:
				if i != None:
					q.enqueue(i)

		print(sum/count)

nTree = n_aryTree()
nTree.root = NodeT(1,3)

nTree.root.children[0] = NodeT(2,3)
nTree.root.children[1] = NodeT(3,3)
nTree.root.children[2] = NodeT(4,3)

curr = nTree.root.children[0]
curr.children[0] = NodeT(5,3)
curr.children[1] = NodeT(6,3)
curr.children[2] = NodeT(7,3)

curr = nTree.root.children[2]
curr.children[0] = NodeT(8,3)
curr.children[1] = NodeT(9,3)
curr.children[2] = NodeT(10,3)

curr = nTree.root.children[1]
curr.children[0] = NodeT(11,3)
curr.children[1] = NodeT(12,3)
curr.children[2] = NodeT(13,3)

#levelOrderTraversal(nTree.root)
averageValPerLevel(nTree.root)