# Binary search inorder traversal asked by Amazon 
# struct Node 
# { 
# int data; 
# Node *right.*left,*random 
# } 

# Tree should be in-order traversal and random node should keep the in-order transversal path.
class Stack:
	def __init__(self):
		self.stack = [0]*10
		self.head = -1
		self.numEle = 0

	def push(self,value):
		self.head += 1
		self.stack[self.head] = value
		self.numEle += 1

	def pop(self):
		value = self.stack[self.head]
		self.head -= 1
		self.numEle -= 1
		return value

	def peep(self):
		return self.stack[self.head]

	def isEmpty(self):
		if self.numEle == 0:
			return True
		else:
			return False

class NodeST:
	def __init__(self,value):
		self.key = value
		self.left = None
		self.right = None
		self.random = None

class BinarySearchTree:
	def __init__(self):
		self.root = None

def inOrder(root):
	if root != None:
		inOrder(root.left)
		print(root.random)
		inOrder(root.right)

def fillRandom(root):
 	s = Stack()

 	while not s.isEmpty():
 		while root != None:
 			s.push(root)
 			root = root.left

 		while not s.isEmpty() and root == None:
 			root = s.pop()
 			root.random = s.peep()
 			root = root.right

def inOrderTraversalUsingStack(root):
	#run1 = True # needed for entering the loop once
	curr = root
	s = Stack()

	while curr != None:
		while curr != None:
			#push(stack,curr)
			s.push(curr)
			curr = curr.left

		while curr == None and not s.isEmpty():
			#print(s.head)
			#stack,curr = pop(stack)
			curr = s.pop()
			print("Current value is %d" %curr.key)
			print("Number of elements in the array is %d" %s.numEle)
			curr.random = s.peep()
			curr = curr.right


bst = BinarySearchTree()

bst.root = NodeST(8)
bst.root.left = NodeST(3)
bst.root.right = NodeST(10)
bst.root.left.left = NodeST(1)
bst.root.left.right = NodeST(6)
bst.root.right.right = NodeST(14)
bst.root.right.right.left = NodeST(13) # node changed previously 13
bst.root.left.right.left = NodeST(4)
bst.root.left.right.right = NodeST(7)


inOrderTraversalUsingStack(bst.root)
fillRandom(bst.root)
print(bst.root.random)

inOrder(bst.root)