def LCS(X, Y):
	l = [[0 for i in range(len(X)+1)] for j in range(len(Y)+1)]
	for i in xrange(0, len(X)):
		for j in xrange(0, len(Y)):
			if X[i] == Y[j]:
				l[i+1][j+1] += l[i][j] + 1 
			else:
				l[i+1][j+1] = max( l[i][j+1], l[i+1][j] )
		
	print l

A = [3, 10, 2, 1, 20]
B = A[:]
B.sort()

LCS(B, A)