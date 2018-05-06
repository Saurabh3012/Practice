from collections import defaultdict

def frequency(s):
	freq = defaultdict(int)
	for i in s:
		freq[i] += 1  
	return freq

f = frequency("aaakhgdg")

print f.items()
