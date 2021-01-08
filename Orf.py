data = {
    'TTT':'F',     'CTT':'L',     'ATT':'I',     'GTT':'V',
    'TTC':'F',     'CTC':'L',     'ATC':'I',     'GTC':'V',
    'TTA':'L',     'CTA':'L',     'ATA':'I',     'GTA':'V',
    'TTG':'L',     'CTG':'L',     'ATG':'M',     'GTG':'V',
    'TCT':'S',     'CCT':'P',     'ACT':'T',     'GCT':'A',
    'TCC':'S',     'CCC':'P',     'ACC':'T',     'GCC':'A',
    'TCA':'S',     'CCA':'P',     'ACA':'T',     'GCA':'A',
    'TCG':'S',     'CCG':'P',     'ACG':'T',     'GCG':'A',
    'TAT':'Y',     'CAT':'H',     'AAT':'N',     'GAT':'D',
    'TAC':'Y',     'CAC':'H',     'AAC':'N',     'GAC':'D',
    'TAA':'Stop',  'CAA':'Q',     'AAA':'K',     'GAA':'E',
    'TAG':'Stop',  'CAG':'Q',     'AAG':'K',     'GAG':'E',
    'TGT':'C',     'CGT':'R',     'AGT':'S',     'GGT':'G',
    'TGC':'C',     'CGC':'R',     'AGC':'S',     'GGC':'G',
    'TGA':'Stop',  'CGA':'R',     'AGA':'R',     'GGA':'G',
    'TGG':'W',     'CGG':'R',     'AGG':'R',     'GGG':'G',
}
comp = {
    'A':'T',
    'G':'C',
    'T':'A',
    'C':'G',
}

def rev_comp(seq):
    str = ''
    for i in reversed(seq):
        #if i == 'T':
        #    str += comp['U']
        #else:
            str += comp[i]

    return str


def start_codon_locations(seq):
    final = []
    i = 0 
    while i in range(len(seq)-3):
        if seq[i:i+3] == 'AUG' or seq[i:i+3] == 'ATG':
            final.append(i)
        i += 1
    return final
    
def dna_to_protein(seq):
    proteins = []
    locations = start_codon_locations(seq)
    rev_compliment = rev_comp(seq)
    rev_locations = start_codon_locations(rev_compliment)
    if (len(locations) > 0):
        for location in locations:
            proteins = proteins + convert_to_protein(seq[location:])
    if (len(rev_locations) > 0):
        for rev_loc in rev_locations:
            proteins = proteins + convert_to_protein(rev_compliment[rev_loc:])
    proteins = list(dict.fromkeys(proteins))
    for prot in proteins:
        print(prot)

def convert_to_protein(seq):
    final = []
    codons = [seq[i:i+3] for i in range(0, len(seq), 3)]
    proteins = []
    str = ''
    for codon in codons:
        if len(codon) != 3:
            pass
        else:
            val = data[codon]
            if val != 'Stop':
                str += val
            else:
                proteins.append(str)
                break

    return proteins
    
if __name__ == '__main__':
    seq = """AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""
    dna_to_protein(seq)
