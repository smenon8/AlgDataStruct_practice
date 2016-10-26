## Demonstrating Graphs using linked lists - adjacency list 
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

class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

	def __repr__(self):
		return str(self.__dict__)

class Graph:
	def __init__(self):
		self.adjList = []

	def createNewNode(self,value):
		node = Node(value)
		self.adjList.append(node)

	def addEdge(self,fromVal,toVal):
		for i in range(len(self.adjList)):
			if fromVal == self.adjList[i].value:
				fromInd = i

		curr = self.adjList[fromInd]
		while curr.next != None:
			curr = curr.next
		curr.next = Node(toVal)

	def printNodes(self):
		for i in range(len(self.adjList)):
			curr = self.adjList[i]
			while(curr != None):
				print(str(curr.value) + "-->",end='')
				curr = curr.next
			print()

	def searchNode(self,val):
		for i in range(len(self.adjList)):
			if self.adjList[i].value == val:
				return i
		return None

def BreadthFirstSearch(g,start):
	visited = [False]*len(g.adjList)
	q = Queue()
	indexStart = g.searchNode(start)

	curr = g.adjList[indexStart]
	q.enqueue(curr)
	while not q.isEmpty():
		curr = q.dequeue() # dequeue the first element, will be printed and marked visited

		index = g.searchNode(curr.value) # search where the first element is in the adjacency list
		curr = g.adjList[index]
		
		if not visited[index]: # check if visited, if not print the value of the current node
			visited[index] = True
			print(curr.value)
		
		curr = curr.next
		
		while curr != None:
			q.enqueue(curr) # enqueue all children of current node
			curr = curr.next


g = Graph()

g.createNewNode(1)
g.createNewNode(2)
g.createNewNode(3)
g.createNewNode(4)
g.createNewNode(5)
g.createNewNode(6)
g.createNewNode(7)
g.createNewNode(8)

g.addEdge(1,4)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,6)
g.addEdge(6,7)
g.addEdge(7,8)
g.addEdge(4,5)
g.addEdge(5,7)
g.addEdge(3,4)
g.addEdge(4,3)
g.printNodes()

print("Breadth First Search output")
BreadthFirstSearch(g,1)
