#Method 1:
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
    
    from Bio import SeqIO

input_file = 'rosalind_lcsm.txt'

with open(input_file) as f:
    fasta_sequences = list(SeqIO.parse(f, 'fasta'))
    sequences = [str(fasta.seq) for fasta in fasta_sequences]

def long_substr(data):
    substr = ''
    if len(data) > 1 and data[0]:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and is_substr(data[0][i: i + j], data):
                    substr = data[0][i: i + j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for dat in data:
        if find not in dat:
            return False
    return True

print(long_substr(sequences))
