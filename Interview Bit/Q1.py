"""

Given a non-negative number represented as an array of digits,

add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

Example:

If the vector has [1, 2, 3]

the returned vector should be [1, 2, 4]

as 123 + 1 = 124.

"""
class SolutionA:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        num = ""
        for i in A:
            num = num + str(i)
        num = int(num)
        num += 1
        ans = []
        while num/10!=0:
            ans.append(num%10)
            num = num/10
        ans.append(num%10)
        ans.reverse()
        return ans


class SolutionB:
	def plusOne(self, A):
		n = len(A) - 1
		if (A[n] + 1) >= 10:
			A[n] = (A[n]+1)%10
			z = A.pop()
			print z
			self.plusOne(A)
		else:
			A[n] = A[n] + 1
		

# obj = SolutionA()
# print obj.plusOne([1,2,3])

objB = SolutionB()
print objB.plusOne([1,2,9])

