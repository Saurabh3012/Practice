G = {
	0: [1, 2],
	1: [2, 3],
	2: [3, 4],
	3: [2],
	4: [5],
	5: [2]
}

start = 0

def DFS_iterative(G, start):
	n = len(G.keys())
	visited = [0 for i in xrange(0, n)]
	visited[start] = 1
	q = []
	q.append(start)

	while len(q)!=0:
		node = q.pop()
		print node,
		for i in G[node]:
			if visited[i] == 0:
				visited[i] = 1
				q.append(i)

v = [0, 0, 0, 0, 0, 0]
def DFS_recursive(G, start, v):
	v[start] = 1
	print start
	for i in G[start]:
		if v[i] == 0:
			DFS_recursive(G, i, v)

# DFS_iterative(G, start)

DFS_recursive(G, start, v)