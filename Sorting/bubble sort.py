def BubbleSort(L):
	n = len(L)
	for i in xrange(0, n-1):
		for j in xrange(0, n-i-1):
			if L[j] > L [j+1]:
				temp = L[j]
				L[j] = L[j+1]
				L[j+1] = temp
	print L

Arr = [9, 0, 2, 4, 6, 8, 2, 1]
BubbleSort(Arr)
