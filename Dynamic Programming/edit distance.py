def min_edit_distance(str1, str2):


	m = len(str1) + 1
	n = len(str2) + 1

	l = [[0 for i in xrange(n)] for j in xrange(m)]

	for i in xrange(0, m):
		for j in xrange(0, n):

			if i == 0:
				l[i][j] = j

			if j == 0:
				l[i][j] = i

			if (i != 0) and (j != 0):

				if str1[i-1] == str2[j-1]:

					l[i][j] = l[i-1][j-1] 
				else:
					l[i][j] = 1 + min(l[i-1][j-1], l[i][j-1], l[i-1][j])
	print l[m-1][n-1]			

min_edit_distance("geek", "gesek")
