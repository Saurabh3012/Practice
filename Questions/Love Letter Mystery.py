""" James found a love letter that his friend Harry has written to his
girlfriend. James is a prankster, so he decides to meddle with the letter. He
changes all the words in the letter into palindromes.

To do this, he follows two rules:

He can only reduce the value of a letter by , i.e. he can change d to c, but he cannot change c to d or d to b.
The letter a may not be reduced any further.
Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations required to convert a given string into a palindrome.


"""

def theLoveLetterMystery(s):
	l = []
	for i in xrange(0, len(s)):
		code = ord(s[i])
		l.append(code)

	size = len(s)
	i = 0
	count = 0
	size = size/2
	while size!=0:
		size = size - 1
		count += abs(l[i] - l[(len(s)-1-i)]) 
		i = i + 1
	return count

print theLoveLetterMystery("abcd")