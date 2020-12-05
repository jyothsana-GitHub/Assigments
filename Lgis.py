from itertools import combinations

n = 0
seq = []

with open('rosalind_lgis.txt', 'r') as f:
	n = int(f.readline().strip())
	seq = [int(x) for x in f.readline().strip().split(" ")]

def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)   
    P = [None] * len(seq)

    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        lower = 0
        upper = L

        if seq[M[upper-1]] < seq[i]:
            j = upper

        else:
           
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid-1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower    
        P[i] = M[j-1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j+1)

    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]    


inc = subsequence(seq)
dec = subsequence(seq[::-1])[::-1]

for i in inc:
	print(i, end=" ")
print('\n', end=" ")
for i in dec:
	print(i,end= " ")

print('\n', end=" ")
