from Bio.Seq import Seq


DNAstrand = ("ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG")


splice_DNAstrand = (DNAstrand.replace("ATCGGTCGAA", ""))
splice_DNAstrand2 = Seq(splice_DNAstrand.replace("ATCGGTCGAGCGTGT", ""))

Protein = splice_DNAstrand2.translate()
print(Protein)
