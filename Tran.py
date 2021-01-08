from scripts import ReadFASTA

DNA1, DNA2 = [fasta[1] for fasta in ReadFASTA('data/rosalind_tran.txt')]

transitions = transversions = 0.0
for i in xrange(len(DNA1)):
	if DNA1[i] ==DNA2[i]:
		pass
	# Check if the nucleotides are in the same purine/pyrimidine group.
	elif DNA1[i] in [['A', 'G'],['C', 'T']][DNA2[i] in ['C', 'T']]:
		transitions += 1
	else:
		transversions +=1

print transitions/transversions
with open('output/031_TRAN.txt', 'w') as output_data:
	output_data.write(str(transitions/transversions))
