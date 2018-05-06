def generateAllSubsets(A):
	bit = len(A)
	for i in range(0, (1<<bit)):
		for j in range(0, bit):
			if ((i& (1<<j))):
				print A[j],
		print

generateAllSubsets(['a','b','c'])