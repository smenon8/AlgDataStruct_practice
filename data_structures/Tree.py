class NodeT:
	def __init__(self,value):
		self.left = None
		self.right = None
		self.value = value

class Tree:
	def __init__(self):
		self.root = None

# functions for tree traversal
# in-order traversal - the natural order, left to right via root
def inOrderTraversal(root):
	if root != None:
		inOrderTraversal(root.left)
		print(root.value)
		inOrderTraversal(root.right)

# pre-order traversal - the order where root is given pre-dominance
def preOrderTraversal(root):
	if root != None:
		print(root.value)
		preOrderTraversal(root.left)
		preOrderTraversal(root.right)

# pre-order traversal - the order where root is given last priority, children first
def postOrderTraversal(root):
	if root != None:
		preOrderTraversal(root.left)
		preOrderTraversal(root.right)	
		print(root.value)

def RecDFS(root): # Same as the logic for pre-order. Thus can be done using Stack too.
	if root == None:
		return
	else:
		print(root.value)
		RecDFS(root.left)
		RecDFS(root.right)

# DFS using stacks
def NonRecDFS(root):
	if root == None:
		return 
	else:
		stck = []
		stck.append(root)
		while len(stck) != 0:
			curr = stck.pop()
			if curr.right != None:
				stck.append(curr.right)

			if curr.left != None:
				stck.append(curr.left)
			
			print(curr.value)
		return

def BFSUsingQ(root):
	queue = []
	curr = root
	i = 0
	## append the root node
	queue.append(curr)

	while curr != None:
		queue.append(curr.left)
		queue.append(curr.right)
		i += 1
		curr = queue[i]

	for i in queue:
		if i != None:
			print(i.value)

def heightFrom(node):
	if node == None: # Base case, you are the leaf node
		return 0
	else:
		return 1 + max(heightFrom(node.left),heightFrom(node.right))

# stack methods - note, these method are built in for lists
def push(arr,num):
	arr.append(num)

def pop(arr):
	l = len(arr)
	ele = arr[l-1]
	arr = arr[:l-1]
	return arr,ele

def inOrderTraversalUsingStack(root):
	#run1 = True # needed for entering the loop once
	curr = root
	stack = []

	while curr != None:
		while curr != None:
			push(stack,curr)
			curr = curr.left

		while curr == None and len(stack) > 0:
			stack,curr = pop(stack)
			print(curr.value)
			curr = curr.right	

def printLevelK(root, k):
	if root == None:
		return 
	else:
		q = [root]
		level = 1
		while level != k and len(q) != 0:
			level += 1
			currLvlNodes = []

			while len(q) != 0:
				currLvlNodes.append(q.pop())

			for node in currLvlNodes:
				if node.left != None:
					q.append(node.left)
				if node.right != None:
					q.append(node.right)

		for node in q:
			print(node.value)

		return

# this function will return a tree given pre-order and in-order traversal
def ConstructTreeInPre(inOrder,preOrder,inStart,inEnd):
	
	if inStart > inEnd:
		return None

	item = preOrder[ConstructTreeInPre.preIndex]
	node = NodeT(item)
	ConstructTreeInPre.preIndex += 1 #global variable

	if inStart == inEnd: # leaf node reached. No more children to this node
		return node

	rightChildIndex = inOrder.index(item) + 1
	leftChildIndex = inOrder.index(item) - 1

	# left sub-tree is the part of the in-order array from start to index of node ele - 1 
	node.left = ConstructTreeInPre(inOrder,preOrder,inStart,leftChildIndex) 
	# right sub-tree is the part of the in-order array from index of node ele + 1 to end
	node.right = ConstructTreeInPre(inOrder,preOrder,rightChildIndex,inEnd)

	return node

# this function will return a tree given pre-order and in-order traversal - method faulty
def ConstructTreeInPost(inOrder,postOrder,inStart,inEnd):
	if inStart > inEnd:
		return None

	item = postOrder[ConstructTreeInPost.postIndex]
	ConstructTreeInPost.postIndex -= 1
	node = NodeT(item)
	

	if inStart == inEnd or ConstructTreeInPost.postIndex <= 0:
		return node


	leftChildIndex = inOrder.index(item) - 1
	rightChildIndex = inOrder.index(item) + 1
	node.left = ConstructTreeInPost(inOrder,postOrder,inStart,leftChildIndex)
	node.right = ConstructTreeInPost(inOrder,postOrder,rightChildIndex,inEnd)

	return node

def getWidth(root,i):
	if root is None:
		return 0
	if i == 1: # root level
		return 1
	else:
	# width of left subtree + width of right subtree
		return getWidth(root.left,i-1)+getWidth(root.right,i-1)


def getMaxWidth(root):
	max = 0
	for i in range(1,heightFrom(root)+1):
		width = getWidth(root,i)
		if max < width:
			max = width

	print("Maximum width of the tree is: %d" %max)

def printKawayFromRoot(root,k):
	if root == None: # to stop running into nodes beyond leaf
		return
	if k == 0: # base case
		print(root.value)
		return
	else:
		printKawayFromRoot(root.left,k-1)
		printKawayFromRoot(root.right,k-1)

def printAncestors(root,ele):
	if root == None:
		return False

	if root.value == ele:
		return True
	else:
		if printAncestors(root.left,ele) == True or printAncestors(root.right,ele) == True:
			print(root.value)
			return True


## TEST DRIVER ####################

t1 = Tree()

t1.root = NodeT(1)
t1.root.left = NodeT(2)
t1.root.right = NodeT(3)
t1.root.left.left = NodeT(4)
t1.root.left.right = NodeT(5)
t1.root.right.left = NodeT(6)
t1.root.right.right = NodeT(7)
t1.root.left.left.left = NodeT(8)
t1.root.right.left.left = NodeT(9)
t1.root.right.left.right = NodeT(10)


print("In order traversal")
inOrderTraversal(t1.root)
print("In order traversal using stack")
inOrderTraversalUsingStack(t1.root)
print("Pre order traversal")
preOrderTraversal(t1.root)
print("Post order traversal")
postOrderTraversal(t1.root)
print("Depth first search")
RecDFS(t1.root)
print("Breadth first search using queue")
BFSUsingQ(t1.root)
print("Height from root")
print(heightFrom(t1.root))

getMaxWidth(t1.root)

print("Nodes k away from the root, where k = 1")
printKawayFromRoot(t1.root,1)

print("Nodes k away from the root, where k = 2")
printKawayFromRoot(t1.root,2)

ConstructTreeInPre.preIndex = 0
inOrder = list('DBEAC')
preOrder = list('ABDEC')
newTree = Tree()
newTree.root = ConstructTreeInPre(inOrder,preOrder,0,len(inOrder)-1)
print("In order traversal of newly constructed tree. Expected DBEAC")
inOrderTraversal(newTree.root)

## Faulty method

postOrder = list('DEBCA')
ConstructTreeInPost.postIndex = len(postOrder) - 1
newTree = Tree()
newTree.root = ConstructTreeInPost(inOrder,postOrder,0,len(inOrder)-1)
print("In order traversal of newly constructed tree. Expected DBEAC")
inOrderTraversal(newTree.root)

print("Print ancestors of elements")
printAncestors(t1.root,5)


