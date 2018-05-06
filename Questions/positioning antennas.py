def number_of_antennas(houses, k):
	r = [0] * (max(houses)+1)
	houses.sort()
	for i in houses:
		r[i] = 1
	print r 

	while 









houses = [2, 5, 4, 6, 7, 9, 11, 12]
k = 2

number_of_antennas(houses, k)