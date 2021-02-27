#graph5.py
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

class Graph:

	# Constructor
    # edges itu list of tuple yang bersisian
    # contoh [(1,2),(1,3)] berarti 1 ngarah ke 2 dan 1 ngarah ke 3
	def __init__(self, edges, N):

		# list dari node yang bertetanggaan
		self.adjList = [[] for _ in range(N)]

		#i inisialisasi derajat masuk dengan 0
		self.indegree = [0] * N

		# add edges to the undirected graph
		for (src1,dest1) in edges: 
			'''harusnya ga ada yg diubah'''

			# add an edge from source to destination
			self.adjList[dest1].append(src1)

			# increment in-degree of destination vertex by 1
			self.indegree[src1] = self.indegree[src1] + 1


# Recursive function to find 
# all topological orderings of a given DAG
def findAllTopologicalOrders(graph, path, discovered, N, map):

	# do for every vertex EXCEPT INDEKS 0
	for v in range(1,N):
		''' INDEKS INI DIMULAI DARI 1 '''

		# proceed only if in-degree of current node is 0 and
		# current node is not processed yet
		if graph.indegree[v] == 0 and not discovered[v]:

			# for every adjacent vertex u of v, 
			# reduce in-degree of u by 1
			for u in graph.adjList[v]:
				graph.indegree[u] = graph.indegree[u] - 1

			# include current node in the path 
			# and mark it as discovered
			path.append(v)
			discovered[v] = True

			# recur
			findAllTopologicalOrders(graph, path, discovered, N, map)

			# backtrack: reset in-degree 
			# information for the current node
			for u in graph.adjList[v]:
				graph.indegree[u] = graph.indegree[u] + 1

			# backtrack: remove current node from the path and
			# mark it as undiscovered
			path.pop()
			discovered[v] = False

	# print the topological order if 
	# all vertices are included in the path
	if len(path) == N-1:
		print(path)
		for i in range(len(path)):
			print('Semester {:<4s} : {}'.format(py_solution().int_to_Roman(i+1), map[path[i]]))         
			#print(map[path[i]])            


def printArrayElement(arr):
    for i in range(len(arr)):
        print(arr[i])

# Print all topological orderings of a given DAG
def printAllTopologicalOrders(graph, map):

	# get number of nodes in the graph
	N = len(graph.adjList)

	# create an auxiliary space to keep track of whether vertex is discovered
	discovered = [False] * N

	# list to store the topological order
	path = []

	# find all topological ordering and print them
	findAllTopologicalOrders(graph, path, discovered, N, map)

# Driver code
if __name__ == '__main__':

	# List of graph edges as per above diagram
	edges = [(1,2),(3,1),(1,4),(3,4),(2,4),(4,5)]
    # BIKIN DICTIONARY DARI SETIAP ANGKA
    # CONTOH : {1 : "Kalkulus", 2 : "Basdat"}


	print("All Topological sorts")

	# Number of nodes in the graph
	N = 5 #termasuk 0
	''' HARUS DIBENERIN N NYA (YANG DIINPUT ASLI+1)'''

	# create a graph from edges
	graph = Graph(edges, N+1)

	# print all topological ordering of the graph
	#printAllTopologicalOrders(graph)

# This code is contributed by Priyadarshini Kumari
