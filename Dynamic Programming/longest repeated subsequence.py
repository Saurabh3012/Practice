def LRS(X):
	l = [[0 for i in range(len(X)+1)] for j in range(len(X)+1)]
	for i in xrange(0, len(X)):
		for j in xrange(0, len(X)):
			if i != j:
				if X[i] == X[j]:
					l[i+1][j+1] += l[i][j] + 1
					print X[i],
				else:
					l[i+1][j+1] = max( l[i][j+1], l[i+1][j] )
		

LRS("AABEBCDD")