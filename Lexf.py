import math
import itertools

def pe(s,n):
	alpha = list(s.split(" "))
	copy = alpha[:]
	for p in itertools.product(copy, repeat=n):
		print ("".join(p))
	
s = "A B C D"
n = 4
pe(s, n)
