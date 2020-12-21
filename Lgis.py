#Method1:
def LIS(list):
    n = len(list)
    end = 1
    length = 1
    p = [0 for i in range(n)]
    l = [1 for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            if int(list[j]) < int(list[i]):
                if l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    p[i] = j
        if max(l) == l[i]:
            length = l[i]
            end = i
    result = [0 for i in range(length)]
    add = length - 1
    while add >= 0:
        result[add] = list[end]
        end = p[end]
        add = add - 1
    return result

def LDS(list):
    n = len(list)
    end = 1
    length = 1
    p = [0 for i in range(n)]
    l = [1 for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            if int(list[j]) > int(list[i]):
                if l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    p[i] = j
        if max(l) == l[i]:
            length = l[i]
            end = i
    result = [0 for i in range(length)]
    add = length - 1
    while add >= 0:
        result[add] = list[end]
        end = p[end]
        add = add - 1
    return result

if __name__ == '__main__':
    array = ['5', '1','4','2','3']
    result_i = LIS(array)
    print(str(result_i)[1:-1].replace(',','').replace("'",''))
    result_d = LDS(array)
    print(str(result_d)[1:-1].replace(',', '').replace("'", ''))



#Method 2:
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
