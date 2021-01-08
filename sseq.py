def main(filename):
	dnastrings = parse_fasta(filename)
	a = dnastrings[0]
	b = dnastrings[1]

	currentbase = -1
	subseqindex = []

	for base in b:
		currentbase += a.index(base) + 2
		subseqindex.append(currentbase)
		
		a = a[a.index(base)+2::]

	print ' '.join(map(str, subseqindex))

def parse_fasta(filename):
	f = open(filename)
	sequences = []
	for line in f:
		if not line.startswith('>'):
			sequences.append(line.rstrip('\n'))
	return sequences

main("rosalind_sseq.txt")
