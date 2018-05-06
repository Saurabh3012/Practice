def fibonacci(n):
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(0)
print fibonacci(1)
print fibonacci(9)