def checkBitSet(n, k):
	return (n & (1<<k))

print checkBitSet(3,2)