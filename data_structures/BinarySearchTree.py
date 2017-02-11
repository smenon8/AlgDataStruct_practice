from math import ceil,floor
class Stack:
	def __init__(self):
		self.stack = [0]*1000
		self.head = -1

	def push(self,value):
		self.head += 1
		self.stack[self.head] = value

	def pop(self):
		value = self.stack[self.head]
		self.head -= 1
		return value

	def isEmpty(self):
		if self.head == -1:
			return True
		else:
			return False

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

	def __repr__(self):
		print("Current contents of the queue:")
		return str(self.queue[self.head:self.tail])

	def length(self):
		return self.tail - self.head

class NodeST:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.key = value

	def __repr__(self):
		return str(self.key)

class BinSearchTree:
	def __init__(self):
		self.root = None

	def searchEle(self,val):
		curr = self.root
		while curr != None:
			if curr.key == val:
				print("Element %d found" %val)
				return curr
			else:
				if curr.key < val:
					curr = curr.right
				else:
					curr = curr.left
		print("Element %d not found in the BST" %val)
		return None

def insertEleRec(root,value):
	if root == None: # base case, you have reached the leaf node
		return NodeST(value)
	else:
		if root.key < value:
			root.right = insertEleRec(root.right,value)
		else:
			root.left = insertEleRec(root.left,value)
	return root

# In order traversal of a binary search tree always returns a sorted list
def inOrderTraversal(root):
	if root != None:
		inOrderTraversal(root.left)
		print(root.key)
		inOrderTraversal(root.right)

def BSTnodeDelete(bst,value):
	node = bst.searchEle(value)

	if node.left == None and node.right == None: # leaf node deletion
		print("Node being deleted is leaf node : %d" %node.key)
		return 

	if node.left == None or node.right == None: # single child deletion
		print("Node being deleted has one child %d" %node.key)
		if node.left != None:
			node.key = node.left.key
			node.left = None
		if node.right != None:
			node.key = node.right.key
			node.right = None	
		return 

	if node.left != None and node.right != None: # replace with in order successor's key and delete the in order successor
		print("Node being deleted has both children %d" %node.key)
		temp = node.right
		while temp != None:
			temp = temp.left
		node.key = temp.key

		# steps to delete in order successor
		temp2 = node.right
		while temp2.left != temp:
			temp2 = temp2.left
		temp2.left = None

def findMinEle(root):
	while root.left != None:
		root = root.left
	return root.key

def findMaxEle(root):
	while root.right != None:
		root = root.right
	return root.key

def inOrderTraversalMod(root,lst):
	if root != None:
		inOrderTraversalMod(root.left,lst)
		lst.append(root.key)
		inOrderTraversalMod(root.right,lst)

# Major assumption: We assume that the tree will only have unique values, a tree can have only its left child <= root node. 
# the logic here is to check recursively, if the sub-trees all have their values within the range. 
# The root node should have values between the min_val and max_val. You start with -inf and +inf for the root node. 
def _isBST_rec(root, min_val, max_val):
	if root == None:
		return True

	if root.key >= min_val and root.key <= max_val:
		return _isBST_rec(root.left, min_val, root.key - 1) and _isBST_rec(root.right, root.key + 1, max_val)
	else:
		return False

def isBST_rec(root):
	return _isBST_rec(root, -float('inf'), float('inf'))


# the logic here is to check if the in-order traversal of the tree returns a sorted array.
# Major assumption: We assume that the tree will only have unique values, a tree can have only its left child <= root node. 
def isBST(root):
	lst = []

	inOrderTraversalMod(root,lst)

	curr = lst[0]
	for i in range(1,len(lst)):
		if curr > lst[i]:
			return False
		curr = lst[i]
	return True


def kthSmallEle(root,k):
	lst = []

	inOrderTraversalMod(root,lst)

	return lst[k-1]

def kthEleUsingStack(root,k):
	s = Stack()
	curr = root

	if curr == None: # Base case
		return 

	while curr 	!= None:
		s.push(curr)
		curr = curr.left

	count = 0
	while not s.isEmpty() and count < k:
		curr = s.pop()
		if count == k-1:
			return curr.key
		count += 1

	if root.right != None:
		return kthEleUsingStack(root.right,k-count)


def lowCommonAncestor(root,val1,val2): # assumption val1 and val2 both exist and val1 < val2
	if root == None:
		return

	if val1 < root.key and val2 < root.key:
		return lowCommonAncestor(root.left,val1,val2)

	if val1 > root.key and val2 > root.key:
		return lowCommonAncestor(root.right,val1,val2)
	
	return root

def low_common_ancestor_non_rec(root, val1, val2):
	curr = root
	while curr:
		if val1 <= curr.key <= val2:
			return curr.key 
		elif val1 < curr.key and val2 < curr.key:
			curr = curr.left
		elif val1 > curr.key and val2 > curr.key:
			curr = curr.right

	return None

def buildBSTFromSortedArr(arr):
	if len(arr) == 0:
		return None

	root = NodeST(arr[ceil(len(arr)/2)-1])

	root.left = buildBSTFromSortedArr(arr[0:ceil(len(arr)/2)-1])
	
	root.right = buildBSTFromSortedArr(arr[ceil(len(arr)/2):len(arr)])
	
	return root

def correct_BST(root):
	in_order_arr = []
	inOrderTraversalMod(root, in_order_arr)

	for i in range(len(in_order_arr)-1, 1, -1):
		if in_order_arr[i] < in_order_arr[i-1]:
			first = i-1

	for i in range(len(in_order_arr)-1):
		if in_order_arr[i] > in_order_arr[i+1]:
			second = i+1

	in_order_arr[first], in_order_arr[second] = in_order_arr[second], in_order_arr[first]

	root = buildBSTFromSortedArr(in_order_arr)

	return root

def ceilFromBST(root,arg):
	if root == None:
		return "Empty tree"
	diff = 0
	ceil = root.key
	while root != None:
		if root.key - arg < 0 and root.right.key - arg < 0:
			return ceil
		else:
			if diff < root.key - arg:
				diff = (root.key - arg) 
				ceil = root.key
			if root.key > arg:
				root = root.left
			else:
				root = root.right

# function to compute the level order traversal of a binary tree/binary search tree.
# easily extended to n-ary tree
def levelOrderTraversal(root):
	q = Queue()

	q.enqueue(root)

	while not q.isEmpty():
		level = q.length()
		while level > 0:
			curr = q.dequeue()

			print(str(curr.key) + " ", end = "")

			if curr.left != None:
				q.enqueue(curr.left)

			if curr.right != None:
				q.enqueue(curr.right)

			level -= 1

		print()

def in_order_succ(root, node):
	if node.right: # if node has a right child, then it simply means the succ is in the right sub-tree 
		return findMinEle(node.right)	
	else:
		curr = root
		while curr:
			if curr.key > node.key: # chances that the successor lies in the left of the curr node
				succ = curr
				curr = curr.left
			elif curr.key < node.key : # the successor lies in the right of the curr-node
				curr = curr.right
			else:
				break

		return succ.key
		
# exact converse of in-order predecessor
def in_order_predec(root, node):
	if node.left:
		return findMaxEle(node.left)
	else:
		curr = root
		while curr:
			if curr.key > node.key:
				curr = curr.left
			elif curr.key < node.key:
				predec = curr
				curr = curr.right
			else:
				break
		return predec.key

		
## TEST DRIVER #############
bst = BinSearchTree()

bst.root = NodeST(8)
bst.root.left = NodeST(3)
bst.root.right = NodeST(10)
bst.root.left.left = NodeST(1)
bst.root.left.right = NodeST(6)
bst.root.right.right = NodeST(14)
bst.root.right.right.left = NodeST(13) # node changed previously 13
bst.root.left.right.left = NodeST(4)
bst.root.left.right.right = NodeST(7)

print("Level order traversal")
levelOrderTraversal(bst.root)

print("kth smallest element with k = 9")
print(kthSmallEle(bst.root,5))
print(kthEleUsingStack(bst.root,5))

# node deletion
#BSTnodeDelete(bst,4)
#inOrderTraversal(bst.root)
# print("Celing of 5 from BST")
# var = ceilFromBST(bst.root,5)
# print(var)

bst.searchEle(6)
bst.searchEle(13)

insertEleRec(bst.root,12)
bst.searchEle(12)
inOrderTraversal(bst.root)

insertEleRec(bst.root,0)
bst.searchEle(0)
inOrderTraversal(bst.root)

print("Minimum element in the BST")
print(findMinEle(bst.root))

print("Maximum element in the BST")
print(findMaxEle(bst.root))

print(isBST(bst.root))

print("Lowest common ancestor of node 1 and 7. Expected 3.")
print(lowCommonAncestor(bst.root,1,7))

sortArr = [1,2,3,4,5,6,7,8]

consBST = BinSearchTree()
consBST.root = buildBSTFromSortedArr(sortArr)
print("Construct element from sorted array")
inOrderTraversal(consBST.root)

print("Level order traversal")
levelOrderTraversal(bst.root)