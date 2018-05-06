def swap(A, minimum, i):
	temp = A[minimum]
	A[minimum] = A[i]
	A[i] = temp

def SelectionSort(L):

	for i in xrange(0, len(L)-1):
		minimum = i
		for j in xrange(i+1, len(L)):
			if L[j] < L[minimum]:
				minimum = j
		swap(L, i, minimum)

Arr = [9, 0, 4, 2, 0, 1, 6, 8, 2, 1]

Arr1 = [7, 5, 2, 3]
SelectionSort(Arr)
print Arr