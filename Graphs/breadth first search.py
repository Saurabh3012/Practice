G = {
	0: [1, 2],
	1: [3, 2],
	2: [3, 4],
	3: [2],
	4: [5],
	5: [2]
}

start = 0

def BFS(G, start):
	n = len(G.keys())
	visited = [0 for i in xrange(0, n)]
	visited[start] = 1
	q = []
	q.append(start)
	
	while len(q)!=0:
		node = q.pop(0)
		for i in G[node]:
			if visited[i] == 0:
				visited[i] = 1
				q.append(i)


BFS(G, start)
