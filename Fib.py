def rabbits(n, t):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return rabbits(n-1, t) + t*rabbits(n-2, t)


print(rabbits(31, 2))
