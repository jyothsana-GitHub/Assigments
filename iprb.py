import itertools

def dominant_probability(num_homozygous_dominant, num_heterozygous, num_homozygous_recessive):
	total = num_homozygous_dominant + num_heterozygous + num_homozygous_recessive

	recessive_probability = (num_homozygous_recessive / total) * ((num_homozygous_recessive - 1) / (total - 1))
	heterozygous_probability = (num_heterozygous / total) * ((num_heterozygous - 1) / (total - 1))
	hetero_recessive_probability = (num_heterozygous / total) * (num_homozygous_recessive / (total - 1)) + (num_homozygous_recessive / total) * (num_heterozygous / (total - 1))

	recessive_total = recessive_probability + heterozygous_probability * (.25) + hetero_recessive_probability * (.5)
	return (1 - recessive_total)

if __name__ == "__main__":

	result = round(dominant_probability(26 , 29 , 26), 5)
	print (result)
