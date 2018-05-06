# this problem uses Kadane's algorithm

def max_sum(A):

	n = len(A)

	max_so_far = 0
	max_ending_here = 0 

	# for array range
	start = 0
	end = 0
	s = 0

	for i in xrange(0, n):
		max_ending_here += A[i]

		if max_ending_here < 0:
			max_ending_here = 0
			s = i+1

		if max_so_far < max_ending_here:
			max_so_far = max_ending_here
			start = s
			end = i

	return max_so_far, start, end

A = [-2, -3, 4, -1, -2, 1, 5, -3]

add, start, end =  max_sum(A)

print add, start, end
