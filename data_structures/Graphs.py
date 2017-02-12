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


class G_node:
	def __init__(self, value):
		self.value = value
		self.adjacents = []

	def add_adjacents(self, *adj_nodes):
		self.adjacents = list(adj_nodes)

	def __repr__(self):
		return str(self.value)

class Graph:
	def __init__(self):
		self.node_list = []

	def add_node(self, node):
		self.node_list.append(node)

	def print_graph(self):
		for node in self.node_list:
			print("%s ->" %node, end = " ")
			print(node.adjacents)	

	def get_num_nodes(self):
		return len(self.node_list)

	def get_index_node_list(self, node):
		for i in range(len(self.node_list)):
			if self.node_list[i] == node:
				return i

def _dfs_helper(G, start_node_idx, visited):
	visited[start_node_idx] = True # 
	start_node = G.node_list[start_node_idx]
	print(start_node,end="->")

	for node in start_node.adjacents:
		idx = G.get_index_node_list(node)
		
		if not visited[idx]: # if not visited, the mark visited and start scanning its adjacents
			_dfs_helper(G, idx, visited)

# the possible modification to this code you can make is to actually do the search! 
def depth_first_search(G, start_node_idx):
	visited = [False] * G.get_num_nodes()

	_dfs_helper(G, start_node_idx, visited)

def breadth_first_search(G, start_node_idx):
	q = Queue()

	visited = [False] * G.get_num_nodes()
	start_node = G.node_list[start_node_idx]
	visited[start_node_idx] = True
	q.enqueue(start_node)

	while not q.isEmpty():
		node = q.dequeue()
		print(node,end="->")
		for adj in node.adjacents:
			adj_idx = G.get_index_node_list(adj)
			if not visited[adj_idx]:
				visited[adj_idx] = True
				q.enqueue(adj)

def _detect_cycle(G, node_idx, visited, rec_stack):
	if not visited[node_idx]:
		visited[node_idx] = True
		rec_stack[node_idx] = True

		curr_node = G.node_list[node_idx]
		for adj in curr_node.adjacents:
			adj_idx = G.get_index_node_list(adj)
			if not visited[adj_idx]:
				return _detect_cycle(G, adj_idx, visited, rec_stack)
			elif rec_stack[adj_idx]:
				return True

		rec_stack[node_idx] = False

		return False

def detect_cycle(G):
	visited = [False] * G.get_num_nodes()
	rec_stack = [False] * G.get_num_nodes()

	for node in G.node_list:
		node_idx = G.get_index_node_list(node)
		has_cycle = _detect_cycle(G, node_idx, visited, rec_stack)

		if has_cycle:
			return True

	return False

def __main__():
	G = Graph()

	a = G_node('a')
	b = G_node('b')
	c = G_node('c')
	d = G_node('d')
	e = G_node('e')
	f = G_node('f')
	g = G_node('g')
	h = G_node('h')
	i = G_node('i')
	j = G_node('j')
	k = G_node('k')

	a.add_adjacents(b,c)
	b.add_adjacents(c)
	c.add_adjacents(g,e,f)
	d.add_adjacents(e)
	e.add_adjacents(d,i,j,f)
	# f.add_adjacents()
	g.add_adjacents(f,a)
	h.add_adjacents(g,j,k)
	i.add_adjacents(j)
	j.add_adjacents(k)
	# k.add_adjacents()


	G.add_node(a)
	G.add_node(b)
	G.add_node(c)
	G.add_node(d)
	G.add_node(e)
	G.add_node(f)
	G.add_node(g)
	G.add_node(h)
	G.add_node(i)
	G.add_node(j)
	G.add_node(k)

	print(G.node_list)

	G.print_graph()

	depth_first_search(G, 4)
	print()
	breadth_first_search(G, 4)
	print()

	# print(G.get_index_node_list(g))
	'''
	Graph Structure as follows:
	a -> [b, c]
	b -> [c]
	c -> [g, e]
	d -> [e]
	e -> [d, i, j]
	f -> []
	g -> [f, a]
	h -> [g, j, k]
	i -> [j]
	j -> [k]
	k -> []
	'''


	G2 = Graph()
	a = G_node('a')
	b = G_node('b')
	# c = G_node('c')
	# d = G_node('d')

	a.add_adjacents(b)
	b.add_adjacents(a)
	# c.add_adjacents(d)
	# d.add_adjacents(b)

	G2.add_node(a)
	G2.add_node(b)
	# G2.add_node(c)
	# G2.add_node(d)
	
	G2.print_graph()

	print(detect_cycle(G))
	print(detect_cycle(G2))

if __name__ == "__main__":
	__main__()