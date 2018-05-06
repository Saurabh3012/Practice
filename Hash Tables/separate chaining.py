# Assumption: size of our hash map is 7

from collections import defaultdict

item = [23, 25, 24, 26, 28, 29, 31, 34, 35, 78, 65]

def hash_map(num):
	return (num % 7)

def probing(num, i):
	return ((num + (i*i))%7)

def separate_chaining(item):
	d = defaultdict(list)
	for i in item:
		h = hash_map(i)
		d[h].append(i)

	return d

def quadratic_probing(item):
	d = defaultdict(list)
	n = 0
	for i in item:
		h = probing(i, n)
		n = n + 1
		d[h].append(i)

	return d

print separate_chaining(item)
print quadratic_probing(item)