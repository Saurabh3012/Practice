def nth_ugly_number(n):
	ugly = [0] * (n+1)
	ugly[0] = 1

	i2 = 0
	i3 = 0
	i5 = 0

	next_multiple_of_2 = ugly[i2]
	next_multiple_of_3 = ugly[i3]
	next_multiple_of_5 = ugly[i5]

	for i in xrange(1, n+1):
		ugly[i] = min( next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 )

		if ugly[i] == next_multiple_of_2:
			i2 += 1
			next_multiple_of_2 = ugly[i2]*2

		if ugly[i] == next_multiple_of_3:
			i3 += 1
			next_multiple_of_3 = ugly[i3]*3

		if ugly[i] == next_multiple_of_5:
			i5 += 1
			next_multiple_of_5 = ugly[i5]*5

	return ugly[n]

print nth_ugly_number(150)		