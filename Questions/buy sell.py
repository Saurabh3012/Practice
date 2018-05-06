def max_profit(a, s, l):
	maxmum = 0
	for i in range(s, l-1):
		if a[i] < a[i+1]:
			for j in range(i+1, l):
				temp = a[j] - a[i]
				if temp > maxmum:
					maxmum = temp
	return maxmum

price = [5, 2, 0, 1, 7, 8, 3, 11]

t1 = 0
t2 = 0
ans = 0
for i in range(0, len(price)):
	t1 = max_profit(price, 0, i)
	t2 = max_profit(price, i, len(price))
	if ans < ( t1 + t2 ):
		ans = t1 + t2
		print t1 
		print t2

print ans

